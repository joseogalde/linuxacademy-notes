#!/usr/bin/env python3.7

#Implementation of Hands-on Lab 

message = input("Enter a message: ")

print("Lowercase: {}".format(message.lower()))
print("Uppercase: {}".format(message.upper()))
print("Capitalized: {}".format(message.capitalize()))
print("Title Case: {}".format(message.title()))

words = message.split(' ')
print("Words: {}".format(words))

sorted_words = sorted(words)

print("Alphabetic First Word: {}".format(sorted_words[0]))
print("Alphabetic Last Word: {}".format(sorted_words[-1]))
