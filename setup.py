from distutils.core import setup
from setuptools import find_packages

with open("requirement.txt", 'r') as file:
    requirement = file.readlines()
with open("LICENSE.txt", 'r') as file:
    license = file.read()

setup(
    name="curses-pong",
    version="1.0",
    description="Pong game in terminal using ncurses",
    author="zazbone",
    author_email="coczaz@gmail.com",
    packages=find_packages(),
    install_requires=requirement,
    license=license
)
