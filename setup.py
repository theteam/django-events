from setuptools import setup, find_packages

setup(
    name = 'events',
    version = '0.1',
    url = 'https://github.com/theteam/django-events',
    license = '',
    description = '',
    author = 'The Team',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
