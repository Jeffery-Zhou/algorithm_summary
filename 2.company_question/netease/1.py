# coding:utf-8


def output():
    N = int(raw_input(""))
    sum = 0
    for i in range(1, N+1):
        sum += maxFactor(i)
    return sum


def maxFactor(num):
    if num % 2 == 1:
        return num
    else:
        count = int(num/2)
        while count > 1:
            if num % count == 0 and count % 2 == 1:
                # print "maxFactor:", count
                break
            count -= 1
        return count

print output()

# while True:
#     try:
#         print output()
#     except Exception, e:
#         print e
#         break
