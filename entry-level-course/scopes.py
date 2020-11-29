y = 5

def set_x(z):
    x = z
    global y	# we are saying that we will use the y variable that is outside
    global a	# With global you can create variables inside a function
    y = x
    a = 7

print("y before set_x:", y)

set_x(10)
print("y after set_x:", y)
print("a after set_x:", a)
