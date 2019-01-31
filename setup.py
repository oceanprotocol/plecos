#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

# from setuptools import setup
from setuptools import setup
import os
from os.path import join
from glob import glob

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

# Installed by pip install squid-py
# or pip install -e .
install_requirements = [
    'jsonschema==3.0.0b3'
]

# Required to run setup.py:
setup_requirements = ['pytest-runner', ]

test_requirements = [
    'pytest',
]

# Possibly required by developers of squid-py:
dev_requirements = [
    'bumpversion',
    'pkginfo',
    'twine',
    'watchdog',
]

docs_requirements = [
    'Sphinx',
    'sphinxcontrib-apidoc',
]

packages = []
for d, _, _ in os.walk('plecos'):
    if os.path.exists(os.path.join(d, '__init__.py')):
        packages.append(d.replace(os.path.sep, '.'))
        print("Added {}".format(d))

setup(
    author="leucothia",
    author_email='devops@oceanprotocol.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="🐳 Ocean/JSON parsing tool for DDO and metadata.",
    extras_require={
        'test': test_requirements,
        'dev': dev_requirements + test_requirements + docs_requirements,
        'docs': docs_requirements,
    },
    install_requires=install_requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='ocean',
    name='plecos',
    # packages=packages,
    packages=packages,
    # package_data = {'plecos' : files },
    data_files=[
        ('.', glob('schemas/*.json')),
        ('.', glob('samples/*.json')),
    ],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/oceanprotocol/squid-py',
    version='0.0.2',
    zip_safe=False,
)