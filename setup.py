#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import setuptools

import os
from os.path import join
from glob import glob
import sys

with open('README.md') as readme_file:
    readme = readme_file.read()

install_requirements = [
    'jsonschema==3.0.0b3'
]

# Required to run setup.py:
setup_requirements = ['pytest-runner', ]

test_requirements = [
    'pytest',
]

# Possibly required by developers of plecos:
dev_requirements = [
    'bumpversion',
    'twine',
]

setuptools.setup(
    author="leucothia",
    author_email='devops@oceanprotocol.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Ocean tool for validating asset metadata.",
    extras_require={
        'test': test_requirements,
        'dev': dev_requirements + test_requirements,
    },
    install_requires=install_requirements,
    license="Apache Software License 2.0",
    long_description="An [Ocean Protocol](https://oceanprotocol.com) utility library to validate asset metadata.",
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='ocean',
    package_data={'plecos': ['samples/*', 'schemas/*']},
    name='plecos',
    packages=['plecos'],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/oceanprotocol/plecos',
    version='0.8.0',
    zip_safe=False,
)
