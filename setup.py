#!/usr/bin/env python
from distutils.core import setup

setup(
    name='sfin2ledger',
    version='0.1.0',
    description='SimpleFIN to Ledger formatter',
    author='Matt Haggard',
    author_email='matt@simplefin.org',
    packages=[],
    py_modules=['sfin2ledger'],
    package_data={},
    install_requires=[
        'argparse',
        'six',
    ],
    scripts=[
        'sfin2ledger',
    ]
)
