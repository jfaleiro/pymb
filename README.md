# pymb
Micro-library for micro-benchmarks in Python: a micro-layer on top of timeit. (Hopefully!) macro helpful.

## Installation

```
git clone https://github.com/jfaleiro/pymb.git
cd pymb
```

Sanity checks
```
python setup.py behave_test
```

## Use

To profile any function just pass it as an argument to the profile function
```python
import microbench as mb
mb.profile(lambda: [str(i) for i in range(1000)])
```
Will execute a number of repetitions, each iteration executing function a number of loops
```
benchmarking 10 repetitions
iteration 0: 0.005507 usecs for 10 loops, 550.699234 umicros per loop
iteration 1: 0.007690 usecs for 10 loops, 768.995285 umicros per loop
(..)
iteration 9: 0.005019 usecs for 10 loops, 501.894951 umicros per loop
stats: (min=0.002169, max=0.008162, avg=0.004702) usecs for 10 loops
Out[5]: 
([0.005506992340087891,
  0.007689952850341797,
(...)
  0.005018949508666992],
 {'avg': 0.004702186584472657,
  'max': 0.00816202163696289,
  'min': 0.002168893814086914})
```

## Tests, use cases, etc

Recorded as features, look under pymb/features for details, e.g.
```
(py27)jorge@ubuntu:~/githubremote/pymb$ behave
```
```
Feature: profiling a function # features/runtime.feature:20

  Scenario Outline: profiling yields correct number of parameters -- @1.1   # features/runtime.feature:28
    Given a simple lambda function                                          # features/steps/steps.py:25 0.000s
    When benchmarking on "1" repeats and "1" loops                          # features/steps/steps.py:29 0.000s
    Then should yield "1" number of results                                 # features/steps/steps.py:33 0.000s

  Scenario Outline: profiling yields correct number of parameters -- @1.2   # features/runtime.feature:29
    Given a simple lambda function                                          # features/steps/steps.py:25 0.000s
    When benchmarking on "3" repeats and "5" loops                          # features/steps/steps.py:29 0.000s
    Then should yield "3" number of results                                 # features/steps/steps.py:33 0.000s
```




