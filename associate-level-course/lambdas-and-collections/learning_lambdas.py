def square(num):
    return num * num

square_lambda = lambda num: num * num
copy_of_lambda = lambda num: num * num


assert square(7) == square_lambda(7)
assert id(square_lambda) != id(copy_of_lambda)
