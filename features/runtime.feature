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
Feature: profiling a function

	Scenario Outline: profiling yields correct number of parameters
	 Given a simple lambda function
	  When benchmarking on "<repeats>" repeats and "<loops>" loops
	  Then should yield "<repeats>" number of results
	  Examples:
	  | repeats	| 	loops	|
	  |		1	|		1	|
	  |		3	|		5	|
	  |		10	|	500,000	|
	  
	Scenario Outline: profiling yields reasonable stats
	 Given a simple lambda function
	  When benchmarking on "<repeats>" repeats and "<loops>" loops
	  Then min <= avg <= max 
	  Examples:
	  | repeats	| 	loops	|
	  |		10	|	500,000	|
	  |		1	|	5		|
	  |		15	|	1		|
	  