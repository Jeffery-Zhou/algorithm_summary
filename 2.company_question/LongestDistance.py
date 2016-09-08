# coding:utf-8
"""
有一个长为n的数组A，求满足0≤a≤b<n的A[b]-A[a]的最大值。
给定数组A及它的大小n，请返回最大差值。
测试样例：
[10,5],2
返回：0
[1,2,7,3,1,5,8,9],8
"""


class LongestDistance:
    def getDis(self, A, n):
        diff_lst = [A[i+1] - A[i] for i in range(0, n-1)]
        max_diff = 0
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if i + 1 <= j:
                    temp = sum(diff_lst[i:j])
                    if max_diff < temp:
                        max_diff = temp
        return max_diff


def output():
    input_str = raw_input("")
    n = int(input_str[-1])
    lst = map(lambda i: int(i), input_str[0:-2].replace('[', '').replace(']', '').split(','))

    diff_lst = [lst[i+1] - lst[i] for i in range(0, n-1)]
    max_diff = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if i+1 <= j:
                temp = sum(diff_lst[i:j])
                if max_diff < temp:
                    max_diff = temp
    return max_diff


print output()

#
# while True:
#     try:
#         output()
#     except Exception, ex:
#         print ex
#         break
