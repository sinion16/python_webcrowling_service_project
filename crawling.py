# # crowling.py
#
# import bs4
# import urllib.request
# from tkinter import *
# from tkinter import ttk
# import analysis
#
#
# # def refresh(site, start=1):
# #     if site == 'seoul' or site == 'all':
# #         url = 'https://www.seoul.go.kr/coronaV/coronaStatus.do'
# #         web_page = urllib.request.urlopen(url)
# #         result = bs4.BeautifulSoup(web_page, 'html.parser')
# #         return result
# #     if site == 'naver' or site == 'all':
# #         url = 'https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&start=' + str(start) + '1'
# #         web_page = urllib.request.urlopen(url)
# #         result = bs4.BeautifulSoup(web_page, 'html.parser')
# #         return result
#
#
# def seoul():
#     # result = refresh('seoul')
#     url = 'https://www.seoul.go.kr/coronaV/coronaStatus.do'
#     web_page = urllib.request.urlopen(url)
#     result = bs4.BeautifulSoup(web_page, 'html.parser')
#
#     list_a = []
#     list_b = []
#
#     # 서울시 확진자 발생동향
#     list_t = []
#     list_n = []
#     i_c = 0
#     for i in range(0, 4):
#         if i == 0 or i == 2:
#             i_c = 2
#         elif i == 1 or i == 3:
#             i_c = 1
#
#         for j in range(0, i_c):
#             for k in range(0, 2):
#                 selector = result.select_one('div.status-seoul > div > div:nth-of-type(' + str(i + 1) +
#                                              ') > div:nth-of-type(' + str(j + 1) +
#                                              ') > p:nth-of-type(' + str(k + 1) + ')').text
#                 if k == 0:
#                     list_t.append(selector)
#                 elif k == 1:
#                     list_n.append(selector)
#     list_a.append([list_t, list_n])
#
#     # 대한민국 발생동향
#     list_t = []
#     list_n = []
#     for i in range(0, 5):
#         for j in range(0, 2):
#             selector = result.select_one('div.status-korea > div > div > div:nth-of-type(' + str(i + 1) +
#                                          ') > p:nth-of-type(' + str(j + 1) + ')').text
#             if j == 0:
#                 list_t.append(selector)
#             elif j == 1:
#                 list_n.append(selector)
#     list_a.append([list_t, list_n])
#
#     # 지역별 신규 확진자 현황
#     list_t = []
#     list_n = []
#     list_s = []
#     for i in range(0, 6):
#         for j in range(0, 13):
#             if i == 0 or i == 3:
#                 selector = result.select_one('tbody > tr:nth-child(' + str(i + 1) +
#                                              ') > th:nth-child(' + str(j + 1) + ')').text
#                 list_t.append(selector)
#             elif i == 2 or i == 5:
#                 selector = result.select_one('tbody > tr:nth-child(' + str(i + 1) +
#                                              ') > td:nth-child(' + str(j + 1) + ')').text
#                 list_n.append(selector)
#     list_a.append([list_t, list_n])
#
#     # 지역별 확진자 현황
#     list_t = []
#     list_n = []
#     for i in range(0, 6):
#         for j in range(0, 13):
#             if i == 0 or i == 3:
#                 selector = result.select_one('tbody > tr:nth-child(' + str(i + 1) +
#                                              ') > th:nth-child(' + str(j + 1) + ')').text
#                 list_t.append(selector)
#             elif i == 1 or i == 4:
#                 selector = result.select_one('tbody > tr:nth-child(' + str(i + 1) +
#                                              ') > td:nth-child(' + str(j + 1) + ')').text
#                 list_n.append(selector)
#     list_a.append([list_t, list_n])
#
#     analysis.run(list_a)
#
#     selector = result.select_one('div.status-seoul > h4 > span').text
#     list_b.append(selector)
#     selector = result.select_one('div.status-korea > h4 > span').text
#     list_b.append(selector)
#
#     return list_a, list_b


# crowling_run.py

import bs4
import urllib.request
from tkinter import *
from tkinter import ttk


# def refresh(site, start=1):
#     if site == 'seoul' or site == 'all':
#         url = 'https://www.seoul.go.kr/coronaV/coronaStatus.do'
#         web_page = urllib.request.urlopen(url)
#         result = bs4.BeautifulSoup(web_page, 'html.parser')
#         return result
#     if site == 'naver' or site == 'all':
#         url = 'https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&start=' + str(start) + '1'
#         web_page = urllib.request.urlopen(url)
#         result = bs4.BeautifulSoup(web_page, 'html.parser')
#         return result


def seoul():

    def reset():
        list_t.remove()
        list_n.remove()


    # result = refresh('seoul')
    url = 'https://www.seoul.go.kr/coronaV/coronaStatus.do'
    web_page = urllib.request.urlopen(url)
    result = bs4.BeautifulSoup(web_page, 'html.parser')

    list_a = []
    list_b = []

    # 발생동향 서울시 크롤링
    list_t = []
    list_n = []
    i_c = 0
    for i in range(0, 4):
        if i == 0 or i == 2:
            i_c = 2
        elif i == 1 or i == 3:
            i_c = 1

        for j in range(0, i_c):
            for k in range(0, 2):
                selector = result.select_one('div.status-seoul > div > div:nth-of-type(' + str(i + 1) +
                                             ') > div:nth-of-type(' + str(j + 1) +
                                             ') > p:nth-of-type(' + str(k + 1) + ')').text
                if k == 0:
                    list_t.append(selector)
                elif k == 1:
                    list_n.append(selector)
    list_a.append([list_t, list_n])

    # 발생동향 대한민국 크롤링
    list_t = []
    list_n = []
    for i in range(0, 5):
        for j in range(0, 2):
            selector = result.select_one('div.status-korea > div > div > div:nth-of-type(' + str(i + 1) +
                                         ') > p:nth-of-type(' + str(j + 1) + ')').text
            if j == 0:
                list_t.append(selector)
            elif j == 1:
                list_n.append(selector)
    list_a.append([list_t, list_n])
    # print('range05 02 list', list_a)

    # 발생동향 자치구별 크롤링
    list_t = []
    list_n = []
    for i in range(0, 6):
        for j in range(0, 13):
            if i == 0 or i == 3:
                selector = result.select_one('tbody > tr:nth-child(' + str(i + 1) +
                                             ') > th:nth-child(' + str(j + 1) + ')').text
                list_t.append(selector)
                # print('list_t : ', list_t)
            elif i == 2 or i == 5:
                selector = result.select_one('tbody > tr:nth-child(' + str(i + 1) +
                                             ') > td:nth-child(' + str(j + 1) + ')').text
                list_n.append(selector)
                # print('list_n ; ', list_n)
    list_a.append([list_t, list_n])
    # print('range06 013 list', list_a)

    # 발생동향 연령대별 크롤링
    list_t = []
    list_n = []
    list_p = []
    for i in range(1, 10):
        selector = result.select_one('div.table-scroll > table > thead > tr > th:nth-child(' +
                                     str(i + 1) + ')').text
        print(selector)
        list_t.append(selector)
        for j in range(1, 3):
            selector = result.select_one('div.table-scroll > table > tbody > tr:nth-child(' +
                                         str(j) + ') > td:nth-child(' +
                                         str(i + 1) + ')').text
            if j == 1:
                list_n.append(selector)
            if j == 2:
                list_p.append(selector)
    list_a.append([list_t, list_n, list_p])

    selector = result.select_one('div.table-scroll > table.tstyle-status-day > thead > tr > th:nth-child(1)').text
    # move-cont1 > div:nth-child(4) > div:nth-child(7) > table > thead > tr > th:nth-child(2)
    print(selector)
    # 발생동향 검사 및 확진자별 크롤링
    list_t = []
    list_n = []
    for i in range(0, 4):
        if i == 0:
            for j in range(0, 8):
        # elif i == 1:
        #     for j in range(1, 10):
        #         selector = result.select_one('tbody > tr:nth-child(' + str(i) +
        #                                     ') > td:nth-child(' + str(j + 1) + ')').text
        #         list_n.append(selector)
        #         print('검사 및 확진자별 list_n : ', list_n)
        #
        # elif i == 2:
        #     for j in range(0, 9):
        #         selector = result.select_one('tbody > tr:nth-child(' + str(i+1) +
        #                                      ') > td:nth-child(' + str(j + 1) + ')').text


                list_n.append(selector)
    list_a.append([list_t, list_n])

    selector = result.select_one('div.status-seoul > h4 > span').text
    list_b.append(selector)
    selector = result.select_one('div.status-korea > h4 > span').text
    list_b.append(selector)

    return list_a, list_b

