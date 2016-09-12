# coding:utf-8
import math

def output():
    C_2 = int(raw_input(""))
    c = math.sqrt(C_2)
    sum = 0
    if c == int(c):
        sum += 4
        for i in range(1, int(c)):
            b = math.sqrt(C_2-i*i)
            if b == int(b):
                sum += 4
    return sum


print output()

# while True:
#     try:
#         print output()
#     except Exception, e:
#         print e
#         break
