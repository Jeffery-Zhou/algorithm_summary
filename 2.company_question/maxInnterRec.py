# -*- coding:utf-8 -*-
"""
有一个直方图，用一个整数数组表示，其中每列的宽度为1，求所给直方图包含的最大矩形面积。比如，对于直方图[2,7,9,4],它所包含的最大矩形的面积为14(即[7,9]包涵的7x2的矩形)。
给定一个直方图A及它的总宽度n，请返回最大矩形面积。保证直方图宽度小于等于500。保证结果在int范围内。
测试样例：
[2,7,9,4,1],5
返回：14
"""


class MaxInnerRec:
    def countArea(self, A, n):
        B = [0 for i in range(n)]  # 存储每条 以当前高为宽的面积
        for i in range(0, n):
            increase_count = 1
            for j in range(i + 1, n):
                print A[j], A[i]
                if A[j] >= A[i]:
                    increase_count += 1
                else:
                    break
            for j in range(i-1, -1, -1):
                print A[j], A[i]
                if A[j] >= A[i]:
                    increase_count += 1
                else:
                    break

            print i, j, increase_count

            B[i] = increase_count * A[i]
            print "i", i, "count", increase_count, "rec", B[i]
        return max(B)


# A = [2, 7, 9, 4, 1]
# n = 5
# A = [281, 179, 386, 165, 88, 500]
# n = 6
A = [511, 211, 745, 720, 81, 48]
n = 6
mir = MaxInnerRec()
print mir.countArea(A, n)
