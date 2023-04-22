import math
import time
from sympy import *

x = Symbol('x')


# Defining Function

def readFunction():
    f = eval(input('Enter the function ='))
    return f


def fun(x0, function):
    fx = lambdify(x, function)
    fx = fx(x0)
    return fx


# Defining derivative of function
def g(x0, function):
    f_prime = function.diff(x)
    gx = lambdify(x, f_prime)
    gx = gx(x0)
    return gx


def fixedPointIteration(func, xo, e, N):
    start = time.perf_counter()
    step = 1
    flag = 1
    condition = True
    xnew = xo
    if g(xnew, func) > 1:
        print("divergent")
        quit()

    while condition:
        xold = xnew
        xnew = fun\
            (xold, func)
        print('Iteration-%d, x1 = %0.9f , error = %0.9f' % (step, xnew, abs(xnew - xold)))
        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(float(xnew - xold)) > e
    if flag == 1:
        print('\nRequired root is: %0.8f' % xnew)
    else:
        pass

    end = time.perf_counter()
    elapsedtime = end - start
    print('The execution time of the above program is : %f ' % elapsedtime)


if __name__ == '__main__':
    func = readFunction()
    xo = float(input('Enter Guess: '))
    e = float(input('Tolerable Error: '))
    N = int(input('Maximum Iteration: '))

    fixedPointIteration(func, xo, e, N)
