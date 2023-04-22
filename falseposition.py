import time


def falseposition(func, a, b, tolerence):
    start = time.perf_counter()

    def f(x):
        f = eval(func)
        return f
    # exp**-x*(3.2*sin(x)-0.5*cos(x))
    i = 0
    xr = (a * f(b) - b * f(a)) / (f(b) - f(a))
    error = abs(xr)

    while error > tolerence:
        xr_after = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(a) * f(b) >= 0:
            print("false position not valid")
            quit()
        if f(xr_after) * f(a) < 0:
            error = abs(xr_after - b)
            b = xr_after
            i = i + 1
        elif f(xr_after) * f(b) < 0:
            error = abs(xr_after - a)
            a = xr_after
            i = i + 1
        print('Iteration-%d, xr = %0.6f  , error= %0.6f ' % (i, xr_after, error))

    print('the root is %f ' % xr_after)
    end = time.perf_counter()
    elapsedtime = end - start
    print("The execution time of the above program is : ", elapsedtime)


if __name__ == '__main__':
    func = input("Enter Function\n")
    first_Number = int(input("enter first number\n"))
    second_Number = int(input("enter second number\n"))
    tolerence = float(input('Tolerable Error: '))

falseposition(func, first_Number, second_Number, tolerence)
