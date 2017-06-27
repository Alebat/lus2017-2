from __future__ import print_function
from sys import argv

with open(argv[1]) as f:
    wrong = False
    list = []
    for i, l in enumerate(f):
        t = l.strip().split("\t")
        if len(t) > 1:
            if t[-2][0] in "BO":
                if wrong:
                    for a, b, c in list:
                        print(a, " " * (25 - len(a)), b, " " * (25 - len(b)), c)
                wrong = False
                list = [(t[0], t[-2], t[-1])]
            if t[-2][0] == "I":
                list.append((t[0], t[-2], t[-1]))
            if t[-2] != t[-1]:
                wrong = True
