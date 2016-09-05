# coding:utf-8
import math


def prime_solve_1(n):
    """
    solution: n一旦发现被小于sqrt(n)的数整除就被排除
    :param lst: {index:the number}->{0:not a prime 1: a prime}
    :return:
    """
    lst = []
    for i in range(3, n + 1):
        flag = True
        j = 2
        while j * j <= i:
            if i % j == 0:
                flag = False
                break
            j += 1
        if flag:
            lst.append(i)
    return lst

print prime_solve_1(10)


def prime_solve_2(n):
    """
    solution:
    :param n:
    :return:
    """

