# coding:utf-8
"""
字符串编辑距离
"""


def EditDistance(A, B):
    la = len(A)
    lb = len(B)
    dp = [[0 for i in range(0, la + 1)] for j in range(0, lb + 1)]
    for i in range(1, la + 1):
        dp[i][0] = i
    for j in range(1, lb + 1):
        dp[0][j] = j

    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            if A[i - 1] == B[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    return dp[i][j]


str1 = 'ABC'
str2 = 'ABDC'
# print EditDistance(str1, str2)


def levenshtein(first, second):
    if len(first) > len(second):
        first, second = second, first
    if len(first) == 0:
        return len(second)
    if len(second) == 0:
        return len(first)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [range(second_length) for x in range(first_length)]
    # print distance_matrix
    for i in range(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i - 1][j] + 1
            insertion = distance_matrix[i][j - 1] + 1
            substitution = distance_matrix[i - 1][j - 1]
            if first[i - 1] != second[j - 1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
    print distance_matrix
    return distance_matrix[first_length - 1][second_length - 1]

# print levenshtein('GUMBOsdafsadfdsafsafsadfasfadsfasdfasdfs','GAMBOL00000000000dfasfasfdafsafasfasdfdsa')
print levenshtein(str1, str2)