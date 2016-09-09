# -*- coding:utf-8 -*-
"""
在4x4的棋盘上摆满了黑白棋子，黑白两色的位置和数目随机其中左上角坐标为(1,1),右下角坐标为(4,4),现在依次有一些翻转操作，要对一些给定支点坐标为中心的上下左右四个棋子的颜色进行翻转，请计算出翻转后的棋盘颜色。
给定两个数组A和f,分别为初始棋盘和翻转位置。其中翻转位置共有3个。请返回翻转后的棋盘。
测试样例：
[[0,0,1,1],[1,0,1,0],[0,1,1,0],[0,0,1,0]],[[2,2],[3,3],[4,4]]
返回：[[0,1,1,1],[0,0,1,0],[0,1,1,0],[0,0,1,0]]
"""


class Flip:
    def flipChess(self, A, f):
        for i in f:
            x, y = i[0] - 1, i[1] - 1
            Ux, Uy = x - 1, y
            Dx, Dy = x + 1, y
            Lx, Ly = x, y - 1
            Rx, Ry = x, y + 1
            self.check_operate(Ux, Uy, A)
            self.check_operate(Dx, Dy, A)
            self.check_operate(Lx, Ly, A)
            self.check_operate(Rx, Ry, A)
        return A

    def check_operate(self, px, py, A):
        if 0 <= px <= 3 and 0 <= py <= 3:
            if A[px][py] == 0:
                A[px][py] = 1
            else:
                A[px][py] = 0
        else:
            return


# A = [[0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0]]
# f = [[2, 2], [3, 3], [4, 4]]

A = [[0, 1, 0, 0], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 1]]
f = [[2, 3], [4, 2], [2, 3]]

fl = Flip()
fl.flipChess(A, f)
print A
