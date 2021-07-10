import sys
import random

try:
    print(f"Received argument {sys.argv[1]}")
    args = sys.argv
    random.shuffle(args)
    print(f"Ranom argument {args[0]}")
except IndexError as err:
    print(f"Error: no arguments, please provide at least one argument")
except NameError as err:
    print(f"Error: random module not loaded")
else:
    #this is only executed if no exception were raised in try
    print("Inside of 'else': no exception has been raised")
finally:
    #this ALWAYS is executed (no matter if there was an exception or not)
    # the only way it does not is by finishing the program with sys.exit() inside the except block
    print("Inside of 'finally': we have reach the final of our program")


