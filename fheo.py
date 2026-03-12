import math

def validate_positive(func):
    def inner(num):
        if(num<=0):
            print('ValueError: Input must be a positive number')
        else:
            func(num)
    return(inner)
def square_root(x):
    print(math.sqrt(x))


f1=validate_positive(square_root)
inp=float(input())
f1(inp)


