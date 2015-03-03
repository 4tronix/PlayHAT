#!/usr/bin/env python
from setuptools import setup, find_packages, Extension
setup(
name = 'playhat',
version = '0.1',
author = 'Gareth Davies',
url = 'https://github.com/4tronix/PlayHAT',
description = """PlayHAT Python library""",
py_modules = [ 'strandtest' ],
install_requires = ['rpi_ws281x >= 1.0.1'],
)
