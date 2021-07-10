import sys

from .errors import ArgumentError

def main():
    #if len(sys.argv) < 2:
    #    raise ArgumentError("too few arguments")
    # assertions evaluates a conditions, it raises an Assertion Error if the condition is False with the given message
    # take care to use assertions bc when compiling bytecode with the flag -O (optimize) the assertions in the code will be erased

    assert len(sys.argv) >= 2, "too few arguments"
    print(f"Name is {sys.argv[1]}")
