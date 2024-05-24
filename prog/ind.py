#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# С использованием многопоточности для заданного значения x
# найти сумму ряда S с точностью члена ряда по
# абсолютному значению E = 10e-7 и произвести сравнение
# полученной суммы с контрольным значением функции
# для двух бесконечных рядов.

from math import cos, fabs, log, pi, sin
from threading import Thread

EPS = 10e-7


# 11 Вариант
def sum_1(target, x):

    a = sin(x)
    S, k = a, 2
    # Найти сумму членов ряда.
    while fabs(a) > EPS:
        coef = 2 * k - 1
        a = sin(coef * x) / coef
        S += a
        k += 1

    target[0] = S
    print(pi / 4)


# 12 Вариант
def sum_2(target, x):

    a = cos(x)
    S, k = a, 2
    # Найти сумму членов ряда.
    while fabs(a) > EPS:
        a = cos(k * x) / k
        S += a
        k += 1

    target[1] = S
    print(-log(2 * sin(x / 2)))


def main():
    part_of_rows = [0, 0]

    th1 = Thread(target=sum_1, args=(part_of_rows, pi / 2))
    th2 = Thread(target=sum_2, args=(part_of_rows, pi))

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print(f"Результат {part_of_rows}")


if __name__ == "__main__":
    main()
