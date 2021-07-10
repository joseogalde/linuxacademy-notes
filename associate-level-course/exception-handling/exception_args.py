class ExampleError(Exception):
    pass

def bad_function():
    raise ExampleError("this is a message", 1, 2, "boom", ["lala","lolo"])

try:
    bad_function()
except ExampleError as err:
    message, x, y, *other = err.args
    print(message)
    print(x + y)
    print(other)
