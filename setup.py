#!/usr/bin/python


from setuptools import setup
from setuptools import find_packages


setup(
    # scripts=['bin/funniest-joke'],
    entry_points={
        'console_scripts': 'funniest-joke=funniest.command_line:main'
    },
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
