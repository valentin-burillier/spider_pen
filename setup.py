from setuptools import setup

setup(
    name = 'spiderpen',
    packages = ['spiderpen'],
    version = '0.1.0',
    description = 'Python library for controlling a plotter model complementary to the LEGO Boost 17101 set',
    long_description = '',
    author = 'Valentin Burillier',
    author_email = 'burillier.v@gmail.com',
    url = 'https://github.com/valentin-burillier/spiderpen',
    keywords = ['LEGO', 'ROBOTICS'],
    requires=['pylgbst'],
)
