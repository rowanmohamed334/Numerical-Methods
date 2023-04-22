from lib2to3 import refactor
import math
import time
from sympy import *

x = Symbol('x')


# Defining Function

def readFunction():
    f = eval(input('Enter the function ='))
    return f


def f(x0, function):
    fx = lambdify(x, function)
    fx = fx(x0)
    return fx


# Defining derivative of function
def g(x0, function):
    f_prime = function.diff(x)
    gx = lambdify(x, f_prime)
    gx = gx(x0)
    return gx


# Implementing Newton Raphson Method

def newtonRaphson(fun, x0, tolerance, N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True

    while condition:
        if g(x0, fun) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0, fun) / g(x0, fun)

        error = abs(x1 - x0)
        print('Iteration-%d, xi = %0.6f xi+1 = %0.6f and error = %0.6f' % (step, x0, x1, error))

        condition = error > tolerance
        x0 = x1
        step = step + 1
        if step > N:
            flag = 0
            break

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Input Section
fun = readFunction()
# test = str(fun)
# test_2 = sympify(test)
# print("func", type(test))
# print("func", type(test_2))
# Note: You can combine above three section like this
x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))

start = time.time()
# Starting Newton Raphson Method
newtonRaphson(fun, x0, e, N)
end = time.time()
print("Elapsed time = ", end - start)


# --------------------------------------------------------------------------------------------------------
# Implementing Secant Method

def secant(fun, x0, x1, tolerance, N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if f(x0, fun) == f(x1, fun):
            print('Divide by zero error!')
            break

        x2 = x0 - (x1 - x0) * f(x0, fun) / (f(x1, fun) - f(x0, fun))
        error = abs(x2 - x1)
        print('Iteration-%d, xi-1=%0.6f  , xi = %0.6f , xi+1 =%0.6f  and error = %0.6f' % (step, x0, x1, x2, error))

        condition = error > tolerance

        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('Not Convergent!')
            break

    print('\nRequired root is: %0.8f' % x2)


# Input Section
fun = readFunction()
print("func", type(fun))

# Note: You can combine above three section like this
x0 = float(input('Enter First Guess: '))
x1 = float(input('Enter Second Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))

start = time.time()
# Starting Secant Method
secant(fun, x0, x1, e, N)
end = time.time()
print("Elapsed time =", end - start)
