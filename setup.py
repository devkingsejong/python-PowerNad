#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path
import os

setup(
    name    = 'powernad', 
    version = '0.8.0',
    packages=find_packages(),
    author = 'devkingsejong',
    author_email = 'devkingsejong@gmail.com', 
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='Easy to use naver ad to python',
    url = 'https://github.com/devkingsejong/python-PowerNad',
    description = 'Easy to use naver ad to python',
)