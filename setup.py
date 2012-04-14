#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

setup(name='docimp',
    version='0.1.1',
    url='https://github.com/macropin/docimp',
    packages=['docimp',],
    install_requires=['couchdbkit', 'lorem_pdf'],
    dependency_links = [
            "https://github.com/macropin/django-lorem-pdf/tarball/master#egg=lorem_pdf"
        ],
    )
