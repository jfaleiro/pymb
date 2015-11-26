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
from behave import *  # @UnusedWildImport
from hamcrest import *  # @UnusedWildImport

from microbench import profile

@given(u'a simple lambda function')  # @UndefinedVariable
def step_impl(context):
    context.function = lambda: 1 + 1

@when(u'benchmarking on "{repeat:n}" repeats and "{loop:n}" loops')  # @UndefinedVariable
def step_impl(context, repeat, loop):  # @DuplicatedSignature
    context.results, context.stats = profile(lambda: 1 + 1, repeat=repeat, loops=loop)
    
@then(u'should yield "{repeat:n}" number of results')  # @UndefinedVariable
def step_impl(context, repeat):  # @DuplicatedSignature
    assert_that(len(context.results), equal_to(repeat))
    
@then(u'min <= avg <= max')  # @UndefinedVariable
def step_impl(context):  # @DuplicatedSignature
    assert_that(context.stats['min'] <= context.stats['avg'] <= context.stats['max'])


