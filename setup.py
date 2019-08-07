#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

setup(name='pymediator',
      version='0.1.0',
      description='Simple but powerful python mediator pattern library',
      author='Alberto Sola',
      author_email='albsolac@gmail.com',
      packages=find_packages(
          exclude=[
              'tests'
          ]
      ),
      url='https://github.com/pirobtumen/pymediator',
      # packages=['distutils', 'distutils.command'],
      )
