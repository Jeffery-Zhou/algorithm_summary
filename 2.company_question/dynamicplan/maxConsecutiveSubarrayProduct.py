# coding:utf-8
"""
最大连续子数组乘积
"""


def maxProduct(A, l):
    """
    :param A: lst A
    :param l: length of A
    :return:
    """
    maxPro = A[0]
    for i in range(0, l):
        product = 1
        for j in range(i, l):
            product = product * A[j]
            if product > maxPro:
                maxPro = product
    return maxPro


def maxProViaDp(A, l):
    """
    后续连续积=max(之前连续积*当前值,当前值)
    因为当前连续积可以来自与最大和最小之前连续积
    so,当前连续积 = max(最大之前连续积*当前值,最小之前连续积*当前值)
    最大后续连续积 = max(max(最大之前连续积*当前值,最小之前连续积*当前值), 当前值)
    相应的,
    最小后续连续积 = min(min(最大之前连续积*当前值,最小之前连续积*当前值), 当前值)


    难点1:为什么同时保持最大连续积和最小连续积?
    因为存在负负得正的问题,最小连续积在乘以一个负数的时候,会存在最小里,如果后续再碰到负数,会上位。

    :param A:
    :param l:
    :return:
    """
    maxEnd = A[0]
    minEnd = A[0]
    for i in range(1, l):
        # end1, end2 = maxEnd * A[i], minEnd * A[i]
        maxEnd = max(max(maxEnd * A[i], minEnd * A[i]), A[i])
        minEnd = min(min(maxEnd * A[i], minEnd * A[i]), A[i])
        maxResult = max(maxEnd, minEnd)
    return maxResult



A = [1, -2, 0, 2.5, -23, 9, -1]
print maxProduct(A, len(A))
print maxProViaDp(A, len(A))
