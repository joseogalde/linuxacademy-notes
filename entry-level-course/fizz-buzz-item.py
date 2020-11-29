#!/usr/bin/env python3.7

#Implementation of Hands-on Labs for Logical Expressions

number = int(input("Enter an integer value: "))

if number % 5 == 0 and number % 3 == 0:
	print("FizzBuzz")
elif number % 5 == 0:
	print("Buzz")
elif number % 3 == 0:
	print("Fizz")
else:
	print(number)
