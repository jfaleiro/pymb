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
import timeit
import gc

def profile(f, enable_gc=True, warm_ups=0, repeat=10, loops=10, trace=True):
    def micros(secs):
        return secs * 1000000.0
    def log(msg, flag):
        if flag:
            print msg
            
    if enable_gc:
        setup = 'gc.enable()'
    else:
        setup = 'gc.disable()'
    timer = timeit.Timer(f, setup=setup)
    if warm_ups > 0:
        log('warming up, %d cycles' % warm_ups, trace)
        secs = timer.timeit(warm_ups)
        log('warmed up %s secs' % secs, trace)
    log('benchmarking %d repetitions' % repeat, trace)
    r = []
    for i in xrange(repeat):
        secs = timer.timeit(loops)
        log('iteration %d: %f usecs for %d loops, %f umicros per loop' % (i, secs, loops, micros(secs / float(loops))), trace)
        r.append(secs)
    minimum = min(r)
    maximum = max(r)
    average = sum(r) / float(len(r))
    log('stats: (min=%f, max=%f, avg=%f) usecs for %d loops' % (minimum, maximum, average, loops), trace)
    stats = dict(min=minimum, max=maximum, avg=average)
    return r, stats
