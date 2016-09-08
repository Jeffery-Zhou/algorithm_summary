# coding:utf-8
"""
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。
如何删除才能使得回文串最长呢？输出需要删除的字符个数。
输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.
对于每组数据，输出一个整数，代表最少需要删除的字符个数。
---------------------------
abcda
google


---------------------------
2
2
"""


def isPlalindrome(s):
    l = len(s)
    if l == 0:
        return True
    if l == 1:
        return True
    if s[0] == s[-1]:
        isPlalindrome(s[1:-1])
    else:
        return False


def isPlalindrome2(s):
    l = len(s)
    if l == 0:
        return True
    if l == 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPlalindrome2(s[1:-1])


print isPlalindrome2('121')


def isPalindrome3(s):
    if len(s) == 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome3(s[1:-1])


def lcs(a, b):
    lena = len(a)   #
    lenb = len(b)   #
    c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]     # 构造记录lcs长度的matric
    flag = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]  # 构造问题由哪个子问题求解而来
    # c和flag的第一行和第一列都为0
    for i in range(1, lena+1):      # 1~lena
        for j in range(1, lenb+1):  # 1~lenb
            if a[i-1] == b[j-1]:    # 因为string从0开始,所以需要-1
                c[i][j] = c[i-1][j-1] + 1
                flag[i][j] = 'ok'
            elif c[i][j-1] > c[i-1][j]:
                c[i][j] = c[i][j-1]
                flag[i][j] = 'left'
            else:
                c[i][j] = c[i-1][j]
                flag[i][j] = 'up'
    return c, flag


def printLcs(flag, a, i, j):
    if i == 0 or j == 0:
        return
    if flag[i][j] == 'ok':
        printLcs(flag, a, i - 1, j - 1)
        # print(a[i - 1], end='')
        print a[i-1]
    elif flag[i][j] == 'left':
            printLcs(flag, a, i, j - 1)
    else:
        printLcs(flag, a, i - 1, j)


a = 'ABCBDAB'
b = 'BDCABA'
c, flag = lcs(a, b)

for i in c:
    print(i)
print('')
for j in flag:
    print(j)
print('')
printLcs(flag, a, len(a), len(b))
print('')
