import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="Python-app",
    version="0.0.1",
    author="Amit Joshi",
    author_email="notesforamit@gmail.com",
    description="An easy and funny example of a Python package",
    long_description="My_own_Python_package contains a funny game for calculating the result of arithmetic operations applied to an unknow number given by the player",
    long_description_content_type="text/markdown",
    url="https://github.com/Git-foramit/Python-app",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)