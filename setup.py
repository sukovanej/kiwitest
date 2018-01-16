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
    ],
    data_files=[
        ('/etc/currency_converter/', ['config.ini', "currency_data.txt"])
    ],
    scripts=[
        "scripts/currency_converter",
        "scripts/currency_converter_server"
    ],
    install_requires=[
        'Flask'
    ]
 )
