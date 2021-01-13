from functools import reduce

domain = [1, 2, 3, 4, 5]

# f(x) = a * x + b
a = 2
b = 3

# map
lambda_lineal = lambda x: a*x+b
our_range = map(lambda_lineal, domain)
print(list(our_range)) #[5, 7, 9, 11, 13]

#filter
lambda_div_by_three = lambda x: (a*x+b) % 3 == 0
threes = filter(lambda_div_by_three, domain)
print(list(threes)) #9

#reduce
the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)

#sorted
words = ['Monday', 'Jose', 'raspberry', 'super8', 'noteBook']
print("Sorting by default")
print(sorted(words))

print("Sorting with a lambda key")
print(sorted(words, key=lambda s: s.lower()))

print("Sorting with a method")
words.sort(key=str.lower, reverse=True)
print(words)

# "something".lower() is the same as str.lower("something")

