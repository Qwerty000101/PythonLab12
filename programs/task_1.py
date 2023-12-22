#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from functools import lru_cache
import matplotlib.pyplot as plt
import timeit


def factorial_bad(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_bad(n - 1)


@lru_cache
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_bad(n - 1)


def fib_bad(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_bad(n-1)+fib_bad(n-2)


@lru_cache
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def fib_iteration(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


def factorial_iteration(n):
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


if __name__ == '__main__':
    y_fib_iteration = []
    y_fib_bad = []
    y_fib = []

    y_factorial_iteration = []
    y_factorial_bad = []
    y_factorial = []
    x = [i for i in range(0,16)]

    i = 0
    while i != 16:
        time_fib_bad = ((timeit.timeit(lambda: fib_bad(i),
                                       number = 100000))/100000)
        y_fib_bad.append(time_fib_bad)

        time_fib = (timeit.timeit(lambda: fib(i), number = 100000))/100000
        y_fib.append(time_fib)

        time_fib_iteration = ((timeit.timeit(lambda: fib_iteration(i),
                                             number = 100000))/100000)
        y_fib_iteration.append(time_fib_iteration)


        time_factorial = ((timeit.timeit(lambda: factorial(i),
                                         number = 100000))/100000)
        y_factorial.append(time_factorial)

        time_factorial_bad = ((timeit.timeit(lambda: factorial_bad(i),
                                             number = 100000))/100000)
        y_factorial_bad.append(time_factorial_bad)

        time_factorial_iteration = ((timeit.timeit(lambda: factorial_iteration(i),
                                                    number = 100000))/100000)
        y_factorial_iteration.append(time_factorial_iteration)

        i += 1

    plt.figure(figsize=(10,6))
    plt.figure(1)
    plt.title("Функции для нахождения чисел Фибоначчи")
    plt.plot(x,y_fib_bad, color="red")
    plt.plot(x,y_fib,color="lime")
    plt.plot(x,y_fib_iteration,color="green")
    plt.xlabel("n")
    plt.ylabel("Время работы")
    plt.legend(['Рекурсивная функция', 'Рекурсивная функция с декоратором',
                'Итеративная функция'])

    plt.figure(figsize=(10,6))
    plt.figure(2)
    plt.title("Функции для нахождения факториала")
    plt.legend("")
    plt.plot(x,y_factorial,color="lime")
    plt.plot(x, y_factorial_bad, color="red")
    plt.plot(x, y_factorial_iteration, color="green")
    plt.xlabel("n")
    plt.ylabel("Время работы")
    plt.legend(['Рекурсивная функция с декоратором', 'Рекурсивная функция',
                'Итеративная функция'])
    plt.show()