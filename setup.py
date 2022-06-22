from setuptools import setup

setup(
    name = 'spiderpen',
    packages = ['spiderpen'],
    version = '0.0.9',
    description = 'Python library to control a complementary model of the LEGO Boost 17101 set',
    long_description = '',
    author = 'Valentin Burillier',
    author_email = '',
    url = 'https://github.com/valentin-burillier/spiderpen',
    keywords = ['LEGO', 'ROBOTICS'],
    requires=['pylgbst'],
)
