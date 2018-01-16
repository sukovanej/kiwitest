#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Currency',
    version='0.1',
    description='Kiwi test project',
    author='Milan Suk',
    author_email='Milansuk@email.cz',
    packages=[
        "currency",
        "currency.symbol",
        "currency.converter"
    ]
 )
