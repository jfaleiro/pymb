#!/usr/bin/env python
#
#    PyMB - Micro-library for micro-benchmarks in Python.
#
#    Copyright (C) 2015 Jorge M. Faleiro Jr.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from setuptools import setup, find_packages
from setuptools_behave import behave_test
from setup_utility import CleanCommand

cmd_classes = {
    'behave_test': behave_test
             }
if CleanCommand:
    cmd_classes['clean'] = CleanCommand

setup(
    name = 'pymb',
    version = '0.0.1',
    description = 'QuantLET - an event driven framework for large scale real-time analytics',
    author='Jorge M. Faleiro Jr.',
    author_email='j@falei.ro',
    url='https://github.com/jfaleiro/pymb',
    download_url='https://github.com/jfaleiro/pymb/tarball/master',
    license = "Affero GPL, see LICENSE.txt for details",
    packages = find_packages(),
    cmdclass=cmd_classes,
    setup_requires=['setupext-janitor'],
    tests_require=['nose','behave>=1.2.5','PyHamcrest'],
    test_suite='nose.collector',
    install_requires=[],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU AFFERO GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ]
)