import spiderpen as sp

p = sp.Plotter(lenght=, height=)

Dx = (p.x_max - p.x_min)/2
Dy = (p.y_max - p.y_min)/2

p.clear()

p.change_color()
p.forward(Dx)
p.forward(Dx)
p.left()
p.forward(Dy)
p.forward(Dy)
p.left()
p.forward(Dx)
p.forward(Dx)
p.left()
p.forward(Dy)
p.left()
p.forward(Dx)

# p.show()

p.connect(L_Gi=, L_Di=)

p.draw(fill_factor=1.0)

p.path()

p.disconnect()

print('L_G =', p.L_G, '; L_D =', p.L_D)
print('Dx =', Dx, '; Dy =', Dy)
