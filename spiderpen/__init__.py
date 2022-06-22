import numpy as np
import matplotlib.pyplot as plt
from pylgbst.comms.cpygatt import BlueGigaConnection
from pylgbst.hub import MoveHub

class Plotter(MoveHub):
    def __init__(self, L_Gi, L_Di, lenght, height=None, connection=None):
        if connection is None:
            connection = BlueGigaConnection()
            connection.connect(hub_name="LEGO Move Hub")
        super(Printer, self).__init__(connection)
        
        self.motor_G = self.motor_A
        self.motor_D = self.motor_B
        self.motor_GD = self.motor_AB
        self.motor_pen = self.motor_external
        
        self.value_D, self.value_G, self.value_B = 0, 0, 0
        self.motor_D.subscribe(self.__callback_D)
        self.motor_G.subscribe(self.__callback_G)
        self.button.subscribe(self.__callback_B)

        # constantes
        self.T = 0.15 # épaisseur du ruban
        self.R = 12 # rapport de réduction
        self.r = 7.5/2 # rayon du treuil en mm
               
        self.write = False
        self.calibration(L_Gi, L_Di, lenght, height)
        self.new_drawing()
    
    def __callback_D(self, value):
        self.value_D = value
    def __callback_G(self, value):
        self.value_G = value
    def __callback_B(self, value):
        self.value_B = value
    
    def new_drawing(self):
        # variables théoriques
        self.write_ = True
        self.angle = 0
        self.x_, self.y_ = 0, 0
        self.instructions = np.array([[0, 0, 0],
                                      [0, 0, 1]], object)
    
    def calibration(self, L_Gi, L_Di, lenght, height=None):
        self.L_tot = 1.37 * 10**3 # longueur de cable LTD = 1.44
        self.L = lenght * 10**3 # distance entre les 2 pts d'accroche en mm
        self.L_G = L_Gi * 10**3
        self.L_D = L_Di * 10**3
        
        # détermination de la zone de dessin
        self.y_max = np.sqrt(self.L_tot**2 - self.L**2)
        if self.y_max > height * 10**3 - 250:
            self.y_max = height * 10**3 - 250
        self.y_min = self.L*0.29 # 0.2 : max et 1/np.sqrt(12)=0.289 : force corde = 1 poid 
        self.x_min = 80
        self.x_max = self.L - 80
        
        # déterminer t_Gi et t_Di
        self.t_Gi = 2*np.pi*(-self.r + np.sqrt(self.r**2 + self.T/np.pi*(self.L_tot - self.L_G)))/self.T * self.R
        self.t_Di = 2*np.pi*(-self.r + np.sqrt(self.r**2 + self.T/np.pi*(self.L_tot - self.L_D)))/self.T * self.R
        
        self.X_i, self.Y_i = self.get_position()

        
    def get_position(self): # fonctionne avec y > 0 
        # lire capteurs
        t_G = self.t_Gi + self.value_G/180*np.pi
        t_D = self.t_Di - self.value_D/180*np.pi
        
        # position des treuils
        a_G = t_G/self.R
        a_D = t_D/self.R
        
        # longueurs des cables
        self.L_G = self.L_tot - a_G*(self.r + self.T*a_G/4/np.pi)
        self.L_D = self.L_tot - a_D*(self.r + self.T*a_D/4/np.pi)
        
        self.x = (self.L_G**2 - self.L_D**2 + self.L**2)/self.L/2
        self.y = np.sqrt(self.L_G**2 - self.x**2)
        
        if self.write:
            self.X.append(self.x)
            self.Y.append(self.y)
            
        return self.x, self.y
    
    _normalize = staticmethod(lambda x_v, y_v : np.array([x_v, y_v])/np.sqrt(x_v**2 + y_v**2))
    
    def get_speed(self, x_f, y_f, x_u, y_u):
        # vitesse du robot
        c = ((x_f - self.x)*y_u + (self.y - y_f)*x_u)/10 # coefficient de correction de trajectoire
        self.dx, self.dy = self._normalize(x_u + c*y_u, y_u - c*x_u)*self.r/self.R
        
        # vitesse des cables
        self.dL_G = (self.y*self.dy + self.dx*self.x)/self.L_G
        self.dL_D = (self.y*self.dy + self.dx*(self.x-self.L))/self.L_D
                        
    def move(self, x_f, y_f, x_i=None, y_i=None, stop=True):
        if x_i == None or y_i == None:
            x_i, y_i = self.x, self.y
        x_u, y_u = self._normalize(x_f - x_i, y_f - y_i)
        
        self.get_position()
        
        while (x_f - self.x)*x_u + (y_f - self.y)*y_u > 2:
            # ajuster vitesse du treuil quand on s'approche de la position finale
            self.get_speed(x_f, y_f, x_u, y_u)

            # vitesse du treuils 
            da_G = self.dL_G/np.sqrt(self.r**2 + self.T/np.pi*(self.L_tot - self.L_G))
            da_D = self.dL_D/np.sqrt(self.r**2 + self.T/np.pi*(self.L_tot - self.L_D))

            # vitesse des moteurs
            dt_G = da_G*self.R
            dt_D = da_D*self.R

            # activer moteurs
            self.motor_GD.start_speed(-dt_G, dt_D)
            
            self.get_position()
        
        if stop:
            self.stop()
         
    def move_pen(self, write):
        self.write = write
        self.motor_pen.goto_position(150*write, speed=0.15) # up : 0 et down : -110

    def stop(self):
        self.dx, self.dy = 0, 0
        self.dL_G, self.dL_D = 0, 0
        
        self.motor_GD.timed(0)

    def home(self):
        # retour a la pos ini 
        self.led.set_color(6) # vert

        self.move_pen(False)
        
        self.move(self.X_i, self.Y_i)
        
        self.motor_G.goto_position(0, speed=0.2)
        self.motor_D.goto_position(0, speed=0.2)
        
        self.led.set_color(3) # bleu
            
          
    def up(self):
        if self.write_:
            self.write_ = False
            self.go_to()
    
    def down(self):
        if self.write_ != 1:
            self.write_ = True
            self.go_to()
    
    def right(self, angle=90):
        self.left(-angle) 
    
    def left(self, angle=90):
        self.angle += angle
        self.angle = -((-self.angle-180)%360 - 180) # met l'angle entre ]-180; 180]
    
    def half_turn(self):
        self.left(180)
    
    def setheading(self, angle=0):
        self.angle = angle
    
    def forward(self, d=10):
        a = self.angle/180*np.pi
        self.go_to(self.x_ + np.cos(a)*d, self.y_ + np.sin(a)*d)
    
    def backward(self, d=10):
        self.forward(-d)
    
    def save_position(self):
        self.backup = (self.instructions[-1, 0], self.instructions[-1, 1], self.angle) # (x_, y_, angle)
        
    def load_position(self):
        x_, y_, self.angle = self.backup
        self.go_to(x_, y_)
    
    def setx(self, x_):
        self.go_to(x_=x_)
        
    def sety(self, y_):
        self.go_to(y_=y_)
     
    def go_to(self, x_=None, y_=None):
        x_ = self.x_ if x_ is None else x_
        y_ = self.y_ if y_ is None else y_
            
        if self.x_ != x_ or self.y_ != y_ or self.write_ != self.instructions[-1, -1]:
            self.x_, self.y_ = x_, y_
            self.instructions = np.concatenate((self.instructions, np.array([[x_, y_, int(self.write_)]], object)), axis=0)
       
    def isdown(self):
        return self.write_
    
    def pos(self):
        return self.x_, self.y_
    
    def xcor(self):
        return self.x_
    
    def ycor(self):
        return self.y_
    
    def heading(self):
        return self.angle
    
    def circle(self, radius, angle=360, n=None, d_max=1): # d_ max valeur max du coté du polygone
        if n == None:
            n = int(np.pi*angle/180*radius/d_max) + 1
        elif n*radius < 0:
            n *= -1
        a, d = angle/n, radius*np.pi*angle/180/n

        self.left(a/2)
        for i in range(abs(n)-1):
            self.forward(d)
            self.left(a)
        self.forward(d)
        self.left(a/2)
        
    def change_color(self):
        write_ = self.write_
        self.up()
        self.write_ = 2
        self.go_to()
        if write_:
            self.down()
        else:
            self.up()
             
    def show(self):
        X_, Y_ = self.instructions[self.instructions.T[-1]==True].T[:-1]
        
        plt.axis('equal')
        plt.plot(X_, Y_)
        plt.show()
        
    def path(self):       
        plt.figure(figsize=(9, 9*(self.y_max - self.y_min)/(self.x_max - self.x_min)))
        
        plt.ylim((self.y_max, self.y_min))
        plt.xlim((self.x_min, self.x_max))
        
        plt.plot(self.X_, self.Y_)
        plt.scatter(self.X, self.Y, c='orange', s=5)
        
        plt.show() 
        
    def _center(self):      
        self.Y_ -= (self.Y_.max() + self.Y_.min())/2
        self.X_ -= (self.X_.max() + self.X_.min())/2
    
    def _fill(self, factor=1): # combler       
        delta_x_ = 2*np.abs(self.X_).max()
        delta_y_ = 2*np.abs(self.Y_).max()
        delta_x = self.x_max - self.x_min
        delta_y = self.y_max - self.y_min
        
        c = min(delta_x/delta_x_, delta_y/delta_y_)*factor
        self.X_ *= c
        self.Y_ *= c

    def _adapt(self):
        self.X_ += (self.x_max + self.x_min)/2
        self.Y_ *= -1
        self.Y_ += (self.y_max + self.y_min)/2
    
    _check = lambda self : self.X_.max() <= self.x_max and self.X_.min() >= self.x_min and self.Y_.max() <= self.x_max and self.Y_.min() >= self.y_min
    
    def draw(self, center=True, fill_factor=0.9):
        if self.instructions[-1, -1]: # leve le crayon a la fin
            self.up()
            
        # historique des positions...
        self.X, self.Y = [], [] # ...déssinées        
        self.X_, self.Y_ = self.instructions.T[:2] # ...théoriques
        
        if center:
            self._center() # centrage du dessin      
        if fill_factor:
            self._fill(factor=fill_factor) # comble espace vide
            self._adapt()
        else:
            self._adapt()
            if not(self._check()): # verifie si le dessin rentre dans la zone de dessin
                return 'Ca depasse chef !'
              
        
        self.led.set_color(6) # vert
        x_i, y_i = None, None
        for x_f, y_f, write in self.instructions:
            if write == 2:
                self.stop()
                self.led.set_color(9) # rouge
                while not(self.value_B):
                    pass
                self.led.set_color(6) # vert
                time.sleep(2)
            elif self.write != write:
                self.stop()
                self.move_pen(write)
            else:
                self.move(x_f, y_f, x_i, y_i, stop=False)
                x_i, y_i = x_f, y_f
                
        self.stop()
        self.led.set_color(3) # bleu
        self.new_drawing()        
