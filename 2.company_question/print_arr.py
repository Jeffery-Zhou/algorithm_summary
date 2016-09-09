# coding:utf-8
"""
有一个二维数组(n*n),写程序实现从右上角到左下角沿主对角线方向打印。
给定一个二位数组arr及题目中的参数n，请返回结果数组。
测试样例：
[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],4
返回：[4,3,8,2,7,12,1,6,11,16,5,10,15,9,14,13]
"""


class Printer:
    def arrayPrint(self, arr, n):
        queue = []
        arr_flag = [[0 for i in range(n)] for j in range(n)]    # whether pushed
        start = [0, n-1]
        queue.append(start)
        arr_flag[start[0]][start[1]] = 1
        while queue:
            item = queue.pop(0)
            print arr[item[0]][item[1]]
            queue.append()





array = 0
n = 0
p = Printer()
p.arrayPrint()
