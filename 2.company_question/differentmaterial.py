# coding:utf-8
"""

"""
import sys


all_lst = []
for line in sys.stdin:
    if line:
        lst = raw_input("").strip().split()
        all_lst.extend(lst)
    else:
        break
# print len(set(all_lst))


def check_method_2():
    all_lst = []
    if not sys.stdin.isatty():      # isatty() -> bool.  True if the file is connected to a TTY device.
        print "Have data!"
        for line in sys.stdin:
            print line
            lst = raw_input("").strip().split()
            all_lst.extend(lst)
        print 'end'
    else:
        print "No data"
    return len(set(all_lst))

check_method_2()

def output():
    all_lst = []
    try:
        lst = raw_input("").strip().split()
        print lst
        all_lst.extend(lst)
        print all_lst
    finally:
        exit()





while True:
    try:
        output()
    except Exception, e:
        print e
        break

