from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject
import math
import time
from sympy import *

x = Symbol('x')


class Methods(QObject):
    output_signal = pyqtSignal(list)
    method_name_signal = pyqtSignal(str)

    def readFunction(self, input_eqn):
        f = eval(str(input_eqn))
        return f

    # return the result of the input equation
    def f(self, input_x, input_equation):
        x = input_x
        return eval(input_equation)

    def fun(self, x0, function):
        fx = lambdify(x, function)
        fx = fx(x0)
        print("fx:", fx)
        return fx

    # Defining derivative of function
    def g(self, x0, function):
        f_prime = function.diff(x)
        print("fprime:", f_prime)
        gx = lambdify(x, f_prime)
        gx = gx(x0)
        print("gx:", gx)
        return gx

    # bisection Method
    def bisection(self, input_eq, left, right, epsilon, max_iteration):
        output_list = []
        x0 = float(left)
        x1 = float(right)
        e = float(epsilon)
        print("epsilon", e)
        old_value = 0
        self.method_name_signal.emit('BISECTION')

        if self.f(x0, input_eq) * self.f(x1, input_eq) > 0.0:
            output_list = ['Given guess values do not bracket the root.']
            self.output_signal.emit(output_list)
        else:
            time_start = time.time()
            step = 1
            condition = True
            while condition:
                x2 = (x0 + x1) / 2
                error = abs(x2 - old_value)
                output = "Iteration: " + str(step) + " x2 = " + str(x2) + " f(x2) = " + str(
                    self.f(x2, input_eq)) + " error:" + str(abs(x2 - old_value)) + '\n'
                output_list.append(output)
                print("x0, x1 , x2, old_value, error", x0, x1, x2, old_value, abs(x2 - old_value))
                if self.f(x0, input_eq) * self.f(x2, input_eq) < 0:
                    x1 = x2
                else:
                    x0 = x2
                # if step == 1:
                #     old_value = x2
                #     print()

                if step >= max_iteration:
                    break
                step = step + 1

                condition = abs(x2 - old_value) > e
                print("condition", condition)
                old_value = x2
            time_end = time.time()
            execution_time = time_end - time_start
            req_root = 'Required Root is ' + str(x2)
            output_list.append(req_root)
            execut_time = 'execution time is:{}' + str(execution_time)
            output_list.append(execut_time)
            self.output_signal.emit(output_list)

    def falsePosition(self, input_eq, a, b, tolerence, max_iteration):
        self.method_name_signal.emit('False Position')
        output_list = []
        start = time.perf_counter()
        i = 0
        xr = (a * self.f(b, input_eq) - b * self.f(a, input_eq)) / (self.f(b, input_eq) - self.f(a, input_eq))
        error = abs(xr)
        if self.f(a, input_eq) * self.f(b, input_eq) >= 0:
            output_list = ['false position not valid']
            self.output_signal.emit(output_list)
        else:
            step = 1
            while error > tolerence:
                xr_after = (a * self.f(b, input_eq) - b * self.f(a, input_eq)) / (
                        self.f(b, input_eq) - self.f(a, input_eq))
                if self.f(xr_after, input_eq) * self.f(a, input_eq) < 0:
                    error = abs(xr_after - b)
                    b = xr_after
                    i = i + 1
                elif self.f(xr_after, input_eq) * self.f(b, input_eq) < 0:
                    error = abs(xr_after - a)
                    a = xr_after
                    i = i + 1
                # print('Iteration-%d, xr = %0.6f  , error= %0.6f ' % (i, xr_after, error))
                output = " Iteration- " + str(i) + " xr = " + str(xr_after) + " error" + str(error) + '\n'
                output_list.append(output)
                step = step + 1
                if step >= max_iteration:
                    flag = 0
                    break


            # print('the root is %f ' % xr_after)
            end = time.perf_counter()
            elapsedtime = end - start
            # print("The execution time of the above program is : ", elapsedtime)
            req_root = 'Required Root is ' + str(xr_after)
            output_list.append(req_root)
            execut_time = 'execution time is:' + str(elapsedtime)
            output_list.append(execut_time)
            self.output_signal.emit(output_list)
        # pass

    def fixedPoint(self, functio, xo, e, N):
        # fun = sympify(functio)
        # print("type of :", type(fun))
        func = self.readFunction(functio)
        self.method_name_signal.emit('Fixed Point')
        output_list = []
        start = time.perf_counter()
        step = 1
        flag = 1
        condition = True
        xnew = xo
        if self.g(xnew, func) > 1:
            output_list = ['divergent']
            print("gx:", self.g(xnew, func))
            self.output_signal.emit(output_list)
        else:

            while condition:
                xold = xnew
                xnew = self.fun(xold, func)
                # print('Iteration-%d, x1 = %0.9f , error = %0.9f' % (step, xnew, abs(xnew - xold)))
                output = "Iteration- " + str(step) + " x1 = " + str(xnew) + " error" + str(abs(xnew - xold)) + '\n'
                output_list.append(output)

                step = step + 1

                if step >= N:
                    flag = 0
                    break

                condition = abs(float(xnew - xold)) > e
            if flag == 1:
                # print('\nRequired root is: %0.8f' % xnew)
                req_root = 'Required Root is ' + str(xnew)
                output_list.append(req_root)
            else:
                final = '\nNot Convergent.'
                output_list.append(final)

            end = time.perf_counter()
            elapsedtime = end - start
            # print('The execution time of the above program is : %f ' % elapsedtime)
            execut_time = 'execution time is:{}' + str(elapsedtime)
            output_list.append(execut_time)
            self.output_signal.emit(output_list)

    def newtonRaphson(self, funci, x0, tolerance, N):
        print("nr func", funci)
        func = self.readFunction(funci)
        self.method_name_signal.emit('newton Raphson')
        output_list = []
        step = 1
        flag = 1
        condition = True
        start = time.time()
        while condition:
            if self.g(x0, func) == 0.0:
                output_list = ['Divide by zero error!']
                self.output_signal.emit(output_list)
                break

            x1 = x0 - self.fun(x0, func) / self.g(x0, func)

            error = abs(x1 - x0)
            # print('Iteration-%d, xi = %0.6f xi+1 = %0.6f and error = %0.6f' % (step, x0, x1, error))
            output = "Iteration- " + str(step) + ' xi: ' + str(x0) + ' xi+1: ' + str(x1) + " error: " + str(
                error) + '\n'
            output_list.append(output)

            condition = error >= tolerance
            x0 = x1
            step = step + 1
            if step >= N:
                flag = 0
                break

        if flag == 1:
            # print('\nRequired root is: %0.8f' % x1)
            req_root = 'Required Root is ' + str(x1)
            output_list.append(req_root)
        else:
            final = '\nNot Convergent.'
            output_list.append(final)
        end = time.time()
        elapsedtime = end - start
        execut_time = 'execution time is:' + str(elapsedtime)
        output_list.append(execut_time)
        self.output_signal.emit(output_list)

    def secant(self, func, x0, x1, tolerance, N):
        start = time.time()
        # print("nr func", funci)
        fun = self.readFunction(func)
        self.method_name_signal.emit('Secant')
        output_list = []
        step = 1
        condition = True
        while condition:
            if self.fun(x0, fun) == self.fun(x1, fun):
                output_list = ['Divide by zero error!']
                self.output_signal.emit(output_list)
                break

            x2 = x0 - (x1 - x0) * self.fun(x0, fun) / (self.fun(x1, fun) - self.fun(x0, fun))
            error = abs(x2 - x1)
            output = "Iteration- " + str(step) + " xi-1= " + str(x0) + " xi =" + str(x1) + " xi+1 = " + str(
                x2) + " error:" + str(error) + '\n'
            output_list.append(output)

            condition = error >= tolerance

            x0 = x1
            x1 = x2
            step = step + 1

            if step >= N:
                final = '\nNot Convergent.'
                output_list.append(final)
                break

        req_root = "Required Root is" + str(x2)
        output_list.append(req_root)
        end = time.time()
        elapsedtime = end - start
        execut_time = 'execution time is:' + str(elapsedtime)
        output_list.append(execut_time)
        self.output_signal.emit(output_list)
