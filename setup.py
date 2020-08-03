from distutils.core import setup
from setuptools import find_packages

with open("requirement.txt") as file:
    requirement = file.readlines()

setup(
    name="curses-pong",
    version="1.0",
    description="Pong game in terminal using ncurses",
    author="zazbone",
    author_email="coczaz@gmail.com",
    packages=find_packages(),
    install_requires=requirement
)
