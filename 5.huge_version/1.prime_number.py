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
    solution:类似于第一种,当n被小于sqrt(n)整除时,会根据sqrt(n)删除它的倍数
    :param n:
    :return:
    """
    lst = [0]*(n+1)
    lst_output = []
    opt_num = 0
    i = 2
    while i * i <= n:
        print i
        if lst[i]:
            continue
        j = 2
        while i * j <= n:
            lst[i*j] = 1
            opt_num += 1
            j += 1
        i += 1
    index = 1
    for i in lst[1:]:

        if i:
            pass
        else:
            lst_output.append(index)
        index += 1

    return lst_output

print prime_solve_2(15)
