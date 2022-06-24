from setuptools import setup

setup(
    name = 'spiderpen',
    packages = ['spiderpen'],
    version = '0.0.10',
    description = 'Python library for controlling a plotter model complementary to the LEGO Boost 17101 set',
    long_description = '',
    author = 'Valentin Burillier',
    author_email = '',
    url = 'https://github.com/valentin-burillier/spiderpen',
    keywords = ['LEGO', 'ROBOTICS'],
    requires=['pylgbst'],
)
