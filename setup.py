#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

# from setuptools import setup
# from setuptools import setup
import setuptools

import os
from os.path import join
from glob import glob
import sys

with open('README.md') as readme_file:
    readme = readme_file.read()

# with open('HISTORY.md') as history_file:
#     history = history_file.read()

# Installed by pip install squid-py
# or pip install -e .
install_requirements = [
    'jsonschema==3.0.0b3'
]

# Required to run setup.py:
# setup_requirements = ['pytest-runner', ]
#
# test_requirements = [
#     'pytest',
# ]

# # Possibly required by developers of squid-py:
# dev_requirements = [
#     'bumpversion',
#     'pkginfo',
#     'twine',
#     'watchdog',
# ]
#
# docs_requirements = [
#     'Sphinx',
#     'sphinxcontrib-apidoc',
# ]

# data_files = [
#         ('plecos', glob('schemas/*.json')),
#         ('plecos', glob('samples/*.json')),
#     ],
# print("Data files:")
# for df in data_files:
#     print(df)


def get_data_files():
    """Get data files in share/jupyter"""
    raise "Not used..."
    data_files = []
    ntrim = len(here + os.path.sep)

    for (d, dirs, filenames) in os.walk(share_jupyterhub):
        data_files.append((
            d[ntrim:],
            [ pjoin(d, f) for f in filenames ]
        ))
    return data_files

def get_package_data(package_name='plecos'):
    """Get package data

    (mostly alembic config)
    """

    package_data = {}
    package_data[package_name] = [
        'samples/*',
        'schemas/*',
    ]
    return package_data

#
# print('sys.prefix',sys.prefix)
# source_folder = 'schemas'
# tgt_path = 'schemas'
# print("Adding all files in /{}".format(source_folder))
# data_files = list()
# for fpath in glob(os.path.join(source_folder, '**/*')):
#     print("\t Adding",fpath)
#     data_files.append((tgt_path, [fpath]))
#
# source_folder = 'samples'
# tgt_path = 'samples'
# print("Adding all files in /{}".format(source_folder))
# for fpath in glob(os.path.join(source_folder, '**/*')):
#     print("\t Adding",fpath)
#     data_files.append((tgt_path, [fpath]))
# #
# # data_files = [   (  'plecos'   in   glob(os.path.join(schema_folder, '**/*'))   )  ]
# print(data_files)
# sample_folder = 'samples'
# print("Adding all files in /{}".format(schema_folder))
# data_files = list()
# for fpath in glob(os.path.join(schema_folder, '**/*')):
#     data_files.append(schema_tgt_path, fpath)
# # install_folder = 'lib/python3.6/site-packages/plecos/samples'
# # print("Adding all files in /{}".format(sample_folder))
# # data_files.append(   (   'plecos', glob(os.path.join(sample_folder, '**/*'))   ))
#
# print("data_files:")
# for df_tuple in data_files:
#     print("\t", df_tuple )


# packages = []
# for d, _, _ in os.walk('plecos'):
#     if os.path.exists(os.path.join(d, '__init__.py')):
#         packages.append(d.replace(os.path.sep, '.'))
#         print("Added {}".format(d))
# !!!! Note MANIFEST.in does not affect binary distributions such as wheels. !!!!!
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
    description="🐳 Ocean/JSON parsing tool for DDO and metadata.",
    # extras_require={
    #     'test': test_requirements,
    #     'dev': dev_requirements + test_requirements + docs_requirements,
    #     'docs': docs_requirements,
    # },
    install_requires=install_requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='ocean',
    package_data=get_package_data(),
    name='plecos',
    # packages=packages,
    packages=['plecos'],
    # package_dir={'plecos': 'src/plecos'},
    # data_files=data_files,
    # package_data = {'plecos' : files },
    # package_data=data_files,
    # setup_requires=setup_requirements,
    # test_suite='tests',
    # tests_require=test_requirements,
    url='https://github.com/oceanprotocol/plecos',
    version='0.7.1',
    zip_safe=False,
)
