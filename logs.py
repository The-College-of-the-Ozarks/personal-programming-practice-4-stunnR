# logs.py
#
# Outputs the value of g(x) = ln(100-x^2) + sqrt(84 - 5x - x^2) at the input x-value.

import math

def g(x):
    return math.log(100 - x**2) + math.sqrt(84 - 5*x - x**2)

x = input("Input a value for x larger than -10 and less than or equal to 7: ")

# exits program if user enters anything but an number
try:
    x = float(x)
except:
    print("Invalid input. x must be a number.")
    exit()

# if x is within function domain, computes function; else exits program
if (x <= -10) or (x > 7):
    print("Invalid input. x must be larger than -10 and less than or equal to 7.")
else:
    print("g(" + str(x) + ") = " + str(g(x)))
