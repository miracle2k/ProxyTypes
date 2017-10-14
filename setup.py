#!/usr/bin/env python
"""Distutils setup file"""

from setuptools import setup

# Metadata
PACKAGE_NAME = "ProxyTypes"
PACKAGE_VERSION = "0.9"


def get_description():
    # Get our long description from the documentation
    f = file('README.txt')
    lines = []
    for line in f:
        if not line.strip():
            break     # skip to first blank line
    for line in f:
        if line.startswith('.. contents::'):
            break     # read to table of contents
        lines.append(line)
    f.close()
    return ''.join(lines)


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description="General purpose proxy and wrapper types",
    long_description = open('README.txt').read(),
    url = "http://cheeseshop.python.org/pypi/ProxyTypes",
    author="Phillip J. Eby",
    author_email="peak@eby-sarna.com",
    license="PSF or ZPL",
    test_suite = 'test_proxies',
    py_modules=['ProxyTypes'],
)

