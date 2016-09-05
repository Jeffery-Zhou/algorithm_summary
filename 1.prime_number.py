# coding:utf-8
import math


def prime_solve(n):
    """
    output all the prime number from 1 to n
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

print prime_solve(10)

