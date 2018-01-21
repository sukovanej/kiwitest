#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Forex',
    version='0.1',
    description='Forex rate getter',
    author='Milan Suk',
    author_email='Milansuk@email.cz',
    packages=[
        'forex_getter',
    ],
    scripts=[
        'scripts/forex_server'
    ],
    install_requires=[
        "forex-python",
        "redis"
    ]
 )
