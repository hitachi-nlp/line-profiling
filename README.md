# Line Profiling
A thin wrapper of [line-profiler](https://github.com/rkern/line_profiler) to suppress `Not found` exception on `@profile` decorator when the program is called without using the line-profiler.

## Installation
```sh
pip install line_profiling@git+https://github.com/hitachi-nlp/line-profiling.git@main

```

## How to use.
```
import line_profiling

@profile
def count(N=10000):
    s = 0
    for i in range(0, N):
        s += i
    return i

count()
```
