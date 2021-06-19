#!/usr/bin/env python

def greeter(prefix):
    def greet(name):
        print(f"{prefix} {name}")
        # this is the most private way to define variables like prefix and name
        # the return statement will return the function (which is also an object)
    return greet

hello = greeter("Hello,")
goodbye = greeter("Good bye,")

hello("Jose")
goodbye("Eren")
