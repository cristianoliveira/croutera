#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from croutera import version

import os

def is_package(path):
        return (
            os.path.isdir(path) and
            os.path.isfile(os.path.join(path, '__init__.py'))
            )

def find_packages(path, base=""):
    """ Find all packages in path """
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package( dir ):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))
    return packages

def publish():
    """Publish to PyPi"""
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

setup(name='croutera',
      version= version(),
      description='Simple Cli Router Admin',
      long_description=open('README.md').read(),
      url='https://github.com/cristianoliveira/croutera',
      author='Cristian Oliveira',
      author_email='contato@cristianoliveira.com.br',
      license='MIT',
      packages=find_packages('.'),
      install_requires=[
        "requests",
      ],
      scripts=['bin/croutera'],
      zip_safe=False)
