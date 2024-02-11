import numpy as np

def mmod_func(number):
    """
    multiple by two
    """
    return number*2

def mmod_funcA(number):
    """
    multiple by two
    """
    return number*2

print("I am outside")
yy = 10

if __name__ == "__main__":
    print("I am inside")
    input = 18
    res = mmod_funcA(input)
    print(res)
    print(res == 36)
    assert res == input*2