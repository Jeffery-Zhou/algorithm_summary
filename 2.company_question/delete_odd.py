# coding:utf-8


def delete_odd():


    (N, M) = map(lambda i: int(i), raw_input("").strip().split())
    score_lst = map(lambda i: int(i), raw_input("").strip().split())
    for i in range(0, M):
        cmd_lst = raw_input("").strip().split()
        if cmd_lst[0] == 'Q':
            if int(cmd_lst[1]) <= int(cmd_lst[2]):
                print max(score_lst[(int(cmd_lst[1]) - 1):int(cmd_lst[2])])
            else:
                print max(score_lst[(int(cmd_lst[2]) - 1):int(cmd_lst[1])])
        elif cmd_lst[0] == 'U':
            score_lst[int(cmd_lst[1]) - 1] = int(cmd_lst[2])


# while True:
#     try:
#         output()
#     except Exception, e:
#         print e
#         break
