import profiler


@profile
def count(N=10000):
    s = 0
    for i in range(0, N):
        s += i
    return i

count()
