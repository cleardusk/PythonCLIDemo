#!/usr/bin/python


from setuptools import setup
from setuptools import find_packages


setup(
    scripts=['bin/funniest-joke'],
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
