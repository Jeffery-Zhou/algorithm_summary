# coding:utf-8
"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
solution:
3 + 1 =
-------
0 1 1
0 0 1
-------

result: 每一位的xor(异或,同0异1)
0 1 0
carry: 与之后的只有都为1时的左边那位需要进位,所有&之后<<1

"""


def calculate(a, b):
    result = a ^ b
    carry = (a & b) << 1
    if carry:
        return calculate(result, carry)
    else:
        return result


print calculate(1, 100)
