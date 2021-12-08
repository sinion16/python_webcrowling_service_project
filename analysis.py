# analysis.py

import re


def first_process(list_r):
    return list_r


def second_process(list_r):
    list_t = [list_r[2][0], list_r[2][1]]

    list_p = []
    for i in range(0, len(list_r[2][2])):
        list_p.append(list_r[2][2][i].replace('+', ''))
    list_t.append(list_p)

    list_p = []
    for i in range(0, len(list_t[1])):
        a = int(''.join(re.findall('\d+', list_t[1][i])))
        b = int(''.join(re.findall('\d+', list_r[0][0][1])))
        list_p.append(str(round(a / b * 100, 1)))
    list_t.append(list_p)

    list_p = []
    for i in range(0, len(list_t[2])):
        a = int(''.join(re.findall('\d+', list_t[2][i])))
        b = int(''.join(re.findall('\d+', list_r[0][0][0])))
        list_p.append(str(round(a / b * 100, 1)))
    list_t.append(list_p)

    list_r[2] = list_t
    return list_r


def third_process(list_r):
    return list_r


def fourth_process(list_r):
    return list_r


def fifth_process(list_r):
    list_t = [list_r[5][0], list_r[5][1]]
    list_p = []
    for i in range(0, len(list_r[5][2])):
        list_p.append(list_r[5][2][i].replace('(', '').replace('+', '').replace(')', ''))
    list_t.append(list_p)
    list_r[5] = list_t
    return list_r
