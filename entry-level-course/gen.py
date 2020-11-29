def gen_range(stop, start = 1, step = 1):
    number = start
    while number <= stop:
        yield number
        number += step

def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a
