from setuptools import setup

setup(
    name = 'spiderpen',
    packages = ['spiderpen'],
    version = '0.0.1',
    description = 'Python library to control a complementary model of the LEGO Boost 17101 set',
    author = 'Valentin Burillier',
    author_email = '',
    url = 'https://github.com/valentin-burillier/spiderpen',
    keywords = ['LEGO', 'ROBOTICS'],
    requires=['pylgbst'],
)
