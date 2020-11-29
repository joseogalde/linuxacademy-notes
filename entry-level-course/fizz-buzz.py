#!/usr/bin/env python3.7

# Implementation of Fizz-Buzz game. The user input gives an integer number
# and the program has to sequentially print the fizz-buzz value of all the integers between [1, number_provided_by_the_user]. If a number is multiply of 3 is "Fizz", if is mutiple of 5 is "Buzz", and if it is both it is "FizzBuzz"

print("Fizz Buzz Game...")

number = int(input("How many values should we process: "))

fizz_index = [i for i in range(number) if i % 3 == 0 and not i % 5 == 0]
buzz_index = [i for i in range(number) if i % 5 == 0 and not i % 3 == 0]
fizzbuzz_index = [i for i in range(number) if i % 5 == 0 and i % 3 == 0]


for i in range(1, number + 1):
    if i in fizz_index:
        print("Fizz")
    elif i in buzz_index:
        print("Buzz")
    elif i in fizzbuzz_index:
        print("FizzBuzz")
    else:
        print(i)

