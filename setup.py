import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Intx",
    version="0.0.1",
    author="Lars Van Cauter",
    author_email="larsvancauter@gmail.com",
    description="An extension to the base type int with some handy functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SH4D0WKING/Intx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent", ],
    python_requires='>=3.6')
