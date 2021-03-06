from functools import reduce

domain = [1, 2, 3, 4, 5]

# f(x) = a * x + b
a = 2
b = 3

# map
lambda_lineal = lambda x: a*x+b
our_range = map(lambda_lineal, domain) # map() applies a lambda function to a collection 
print(list(our_range)) #[5, 7, 9, 11, 13]

#filter
lambda_div_by_three = lambda x: (a*x+b) % 3 == 0
threes = filter(lambda_div_by_three, domain) # filter() uses a lambda function that returns True or False values and returns the values that are True 
print(list(threes)) #9

#reduce
the_sum = reduce(lambda acc, num: acc + num, domain, 0) # reduce takes an iterable with an initial value and itares over that collection using the lambda provided
print(the_sum)

#sorted
print("Words")
words = ['Monday', 'Jose', 'raspberry', 'super8', 'noteBook']
print(words);

print("Sorting by default")
print(sorted(words))

print("Sorting with a lambda key")
print(sorted(words, key=lambda s: s.lower())) # when using a lambda for key, it will change the comparison value that will use to perform the sorting algorithm

print("Sorting with a method")
words.sort(key=str.lower, reverse=True) # here we want to pass the function as an objetct, therefore we cannot make use of parenthesis like lower(), so we use str.lower which is an object and were are not calling the function of the string.
# reverse requieres a boolean value
print(words)

# "something".lower() is the same as str.lower("something")

