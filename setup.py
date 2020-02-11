#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='dpkg_list_json',
    version='0.0.1',
    py_modules=['dpkg_list_json'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'dpkg_list_json = dpkg_list_json:main',
        ],
    },
)
