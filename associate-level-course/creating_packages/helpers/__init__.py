# this file could be empty, it is necessary to exist only to specify that this is a package
# we can also initialize our modules variables here
# this is the first code that runs with our package
# example to allow extract_upper function for everybody that imports our package
__all__ = ['extract_upper']

from .strings import *
