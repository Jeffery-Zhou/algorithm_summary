# coding:utf-8

"""
1,2,3,4
1,3,2,4
"""
def output():
    lst = map(lambda i: int(i), raw_input("").strip().split(','))
    l = len(lst)
    lst.insert(0, 0)
    result_lst = []
    if l%2 == 0:
        m = l/2
        print m
        for i in range(1, m+1):
            print m+i, 2*i
            result_lst[m+i] = lst[2*i]
            result_lst[i] = lst[2*i-1]

    # 去除0
    result_lst.pop(0)
    print result_lst
    return result_lst


output()

while True:
    try:
        output()
    except Exception, e:
        print e
        break
