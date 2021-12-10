# frame.py

import tkinter
from tkinter import *
import crawling
import webbrowser


def view():
    tk.mainloop()


def hide():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()


def request(site, start=0):
    if site == 'seoul':
        seoul_list = crawling.seoul()
        # for i in range(len(seoul_list[0])):
        #     print(seoul_list[0][i])
        # print(seoul_list[1])
        return seoul_list
    if site == 'naver':
        naver_list = crawling.naver(start)
        # for i in range(len(naver_list[0])):
        #     print(naver_list[0][i])
        # print(naver_list[1])
        return naver_list


def refresh(page=0, seoul_list=[], naver_list=[]):

    # seoul sub def ========================= #
    def color(num_list, num):
        num_rank = sorted(num_list)
        rank = num_rank.index(num_list[num])
        if rank <= 1:
            return '#80bf40'
        elif rank <= 3:
            return '#8fbf40'
        elif rank <= 5:
            return '#9fbf40'
        elif rank <= 7:
            return '#afbf40'
        elif rank <= 9:
            return '#bfbf40'
        elif rank <= 11:
            return '#bfaf40'
        elif rank <= 13:
            return '#bf9f40'
        elif rank <= 15:
            return '#bf8f40'
        elif rank <= 17:
            return '#bf8040'
        elif rank <= 19:
            return '#bf7040'
        elif rank <= 21:
            return '#bf6040'
        elif rank <= 23:
            return '#bf5040'
        elif rank <= 25:
            return '#bf4040'

    def back():
        hide()
        frame2.pack()
        frame3.pack()
        button1_1.config(text='새로고침', command=refresh)

    def click1_1():
        hide()
        frame4.pack()
        button1_1.config(text='돌아가기', command=back)

        sub_list = seoul_list[0][2]
        d = 4
        c = 0
        s = 0
        for i in range(0, len(sub_list[0])):
            if c == d:
                c = 0
                s = s + 2
            font_color = color(sub_list[3], i)
            label = Label(frame4, width=12, text=sub_list[0][i],
                          font=('', 12), fg=font_color, borderwidth=0)
            label.grid(row=s, column=c, padx=12, pady=(2, 0))
            if c == 0:
                label.grid(padx=(14, 12))
            if c == d-1:
                label.grid(padx=(12, 14))
            label = Label(frame4, width=12, text=sub_list[2][i] + '명 ' + sub_list[4][i] + '%',
                          font=('', 12), fg=font_color, borderwidth=0)
            label.grid(row=s+1, column=c)
            if i == len(sub_list[0])-1:
                label = Label(frame4, width=12, text='총 합', font=('', 12), borderwidth=0)
                label.grid(row=s, column=c+1, padx=12, pady=(2, 0))
                label = Label(frame4, width=12, text=seoul_list[0][0][0][0] + '명', font=('', 12), borderwidth=0)
                label.grid(row=s+1, column=c+1, padx=12, pady=(0, 4))
            c = c + 1

    def click1_2():
        hide()
        frame5.pack()
        button1_1.config(text='돌아가기', command=back)

        sub_list = seoul_list[0][2]

        d = 4
        c = 0
        s = 0
        for i in range(0, len(sub_list[0])):
            if c == d:
                c = 0
                s = s + 2
            font_color = color(sub_list[3], i)
            label = Label(frame5, width=12, text=sub_list[0][i],
                          font=('', 12), fg=font_color, borderwidth=0)
            label.grid(row=s, column=c, padx=12, pady=(2, 0))
            if c == 0:
                label.grid(padx=(14, 12))
            if c == d-1:
                label.grid(padx=(12, 14))
            label = Label(frame5, width=12, text=sub_list[1][i] + '명 ' + sub_list[3][i] + '%',
                          font=('', 12), fg=font_color, borderwidth=0)
            label.grid(row=s+1, column=c)
            if i == len(sub_list[0])-1:
                label = Label(frame5, width=12, text='총 합', font=('', 12), borderwidth=0)
                label.grid(row=s, column=c+1, padx=12, pady=(2, 0))
                label = Label(frame5, width=12, text=seoul_list[0][0][0][1] + '명', font=('', 12), borderwidth=0)
                label.grid(row=s+1, column=c+1, padx=12, pady=(0, 4))
            c = c + 1

    def click1_3():
        hide()
        frame6.pack()
        button1_1.config(text='돌아가기', command=back)

        sub_list = seoul_list[0][5]

        d = 7
        c = 0
        s = 0
        for i in range(0, len(sub_list[0])):
            if c == d:
                c = 0
                s = s + 3

            if sub_list[0][i] == '1':
                text1 = seoul_list[1][2][1] + '. ' + sub_list[0][i] + '.'
            elif sub_list[0][i] != '':
                text1 = sub_list[0][i] + '.'
            else:
                text1 = ''
            if sub_list[1][i] != '':
                text2 = '총 ' + sub_list[1][i] + '명'
            else:
                text2 = ''
            if sub_list[2][i] != '':
                text3 = sub_list[2][i] + '명'
            else:
                text3 = ''
            label = Label(frame6, width=8, text=text1,
                          font=('', 12), height=1, borderwidth=0)
            label.grid(row=s, column=c, padx=1, pady=(6, 0))
            if c == 0:
                label.grid(padx=(5, 1))
            if c == d-1:
                label.grid(padx=(1, 5))
            label = Label(frame6, width=9, text=text2,
                          font=('', 9), height=1, borderwidth=0)
            label.grid(row=s + 1, column=c)
            label = Label(frame6, width=9, text=text3,
                          font=('', 9), height=1, borderwidth=0)
            label.grid(row=s + 2, column=c)
            if i == len(sub_list[0])-1:
                label.grid(pady=(0, 10))
            c = c + 1

    def reload_0():
        refresh(0, request('seoul'), naver_list)

    def page_1():
        refresh(1, seoul_list, naver_list)
    # ======================================= #

    # naver sub def ========================= #
    def callback(url):
        webbrowser.open_new(url)

    def start_set(start):
        print('start', start)
        refresh(1, seoul_list, request('naver', start))

    def reload_1():
        refresh(1, seoul_list, request('naver'))

    def page_0():
        refresh(0, seoul_list, naver_list)
    # ======================================= #

    if len(seoul_list) == 0:
        seoul_list = request('seoul')
        naver_list = request('naver')

    hide()
    if page == 0:
        frame2.pack()
        frame3.pack()

        button1_1.config(text='새로고침', command=reload_0)
        button1_2.config(text='관련뉴스', command=page_1)
        button1_3.config(command=click1_3)

        label1_1.config(text=naver_list[0][0][:30], font=('', 12, 'underline'), fg='#287bde')
        label1_1.bind("<Button-1>", lambda e: callback(naver_list[1][0]))

        seoul = seoul_list[0][0]
        korea = seoul_list[0][1]

        label = Label(frame2, text=seoul_list[1][0])
        label.grid(row=0, column=0, columnspan=len(seoul[0]))
        for i in range(0, len(seoul)):
            for j in range(0, len(seoul[0])):
                if i == 0:
                    button = Button(frame2, width=6, text=seoul[i][j], font=('', 16, 'bold'), borderwidth=0)
                    button.grid(row=i+1, column=j, padx=3, pady=(9, 3))
                    if j == 0:
                        button.config(font=('', 16, 'bold underline'), command=click1_1)
                    if j == 1:
                        button.config(font=('', 16, 'bold underline'), command=click1_2)
                else:
                    label = Label(frame2, text=seoul[i][j])
                    label.grid(row=i+1, column=j, padx=3, pady=(3, 30))

        label = Label(frame3, text=seoul_list[1][1])
        label.grid(row=0, column=0, columnspan=len(korea[0]))
        for i in range(0, len(korea)):
            for j in range(0, len(korea[0])):
                if i == 0:
                    button = Button(frame3, width=6, text=korea[i][j], font=('', 16, 'bold'), borderwidth=0)
                    button.grid(row=i+1, column=j, padx=3, pady=(9, 3))
                    if j == 3:
                        button.config(padx=46)
                else:
                    label = Label(frame3, text=korea[i][j])
                    label.grid(row=i+1, column=j, padx=3, pady=(3, 30))
    if page == 1:
        frame7.pack()

        button1_1.config(text='새로고침', command=reload_1)
        button1_2.config(text='메인으로', command=page_0)

        widget_list = frame7.grid_slaves()
        for i in widget_list:
            i.destroy()

        # 나중에 제대로
        label = Label(frame7, width=44, text=naver_list[0][0][:30], font=('', 12, 'underline'), fg='#287bde', bg='white', relief='sunken')
        label.grid(row=0, column=0, padx=69, pady=(10, 0))
        label.bind("<Button-1>", lambda e: callback(naver_list[1][0]))
        label = Label(frame7, width=44, text=naver_list[0][1][:30], font=('', 12, 'underline'), fg='#287bde', bg='white', relief='sunken')
        label.grid(row=1, column=0)
        label.bind("<Button-1>", lambda e: callback(naver_list[1][1]))
        label = Label(frame7, width=44, text=naver_list[0][2][:30], font=('', 12, 'underline'), fg='#287bde', bg='white', relief='sunken')
        label.grid(row=2, column=0)
        label.bind("<Button-1>", lambda e: callback(naver_list[1][2]))
        label = Label(frame7, width=44, text=naver_list[0][3][:30], font=('', 12, 'underline'), fg='#287bde', bg='white', relief='sunken')
        label.grid(row=3, column=0)
        label.bind("<Button-1>", lambda e: callback(naver_list[1][3]))
        label = Label(frame7, width=44, text=naver_list[0][4][:30], font=('', 12, 'underline'), fg='#287bde', bg='white', relief='sunken')
        label.grid(row=4, column=0)
        label.bind("<Button-1>", lambda e: callback(naver_list[1][4]))
        label = Label(frame7, width=44, text=naver_list[0][5][:30], font=('', 12, 'underline'), fg='#287bde', bg='white', relief='sunken')
        label.grid(row=5, column=0)
        label.bind("<Button-1>", lambda e: callback(naver_list[1][5]))
        label = Label(frame7, width=44, text=naver_list[0][6][:30], font=('', 12, 'underline'), fg='#287bde', bg='white', relief='sunken')
        label.grid(row=6, column=0)
        label.bind("<Button-1>", lambda e: callback(naver_list[1][6]))
        label = Label(frame7, width=44, text=naver_list[0][7][:30], font=('', 12, 'underline'), fg='#287bde', bg='white', relief='sunken')
        label.grid(row=7, column=0)
        label.bind("<Button-1>", lambda e: callback(naver_list[1][7]))
        label = Label(frame7, width=44, text=naver_list[0][8][:30], font=('', 12, 'underline'), fg='#287bde', bg='white', relief='sunken')
        label.grid(row=8, column=0)
        label.bind("<Button-1>", lambda e: callback(naver_list[1][8]))
        label = Label(frame7, width=44, text=naver_list[0][9][:30], font=('', 12, 'underline'), fg='#287bde', bg='white', relief='sunken')
        label.grid(row=9, column=0, pady=(0, 9))
        label.bind("<Button-1>", lambda e: callback(naver_list[1][9]))

        button_frame = Frame(frame7)
        button_frame.grid(row=10, column=0, pady=(0, 9))

        button = Button(button_frame, text='1', borderwidth=0)
        button.grid(row=0, column=1, padx=5)
        button.config(command=lambda: start_set(1))
        button = Button(button_frame, text='2', borderwidth=0)
        button.grid(row=0, column=2, padx=5)
        button.config(command=lambda: start_set(2))
        button = Button(button_frame, text='3', borderwidth=0)
        button.grid(row=0, column=3, padx=5)
        button.config(command=lambda: start_set(3))
        button = Button(button_frame, text='4', borderwidth=0)
        button.grid(row=0, column=4, padx=5)
        button.config(command=lambda: start_set(4))
        button = Button(button_frame, text='5', borderwidth=0)
        button.grid(row=0, column=5, padx=5)
        button.config(command=lambda: start_set(5))
        button = Button(button_frame, text='6', borderwidth=0)
        button.grid(row=0, column=6, padx=5)
        button.config(command=lambda: start_set(6))
        button = Button(button_frame, text='7', borderwidth=0)
        button.grid(row=0, column=7, padx=5)
        button.config(command=lambda: start_set(7))
        button = Button(button_frame, text='8', borderwidth=0)
        button.grid(row=0, column=8, padx=5)
        button.config(command=lambda: start_set(8))
        button = Button(button_frame, text='9', borderwidth=0)
        button.grid(row=0, column=8, padx=5)
        button.config(command=lambda: start_set(9))


tk = Tk()
tk.title('corona')
tk.geometry('600x400')


master_frame = Frame(tk, width=600, height=400)
master_frame.pack()


frame1 = Frame(master_frame)
frame1.pack()

button1_1 = Button(frame1, width=6, text='새로고침', font=('', 10))
label1_1 = Label(frame1, width=44, text='기사 제목', bg='white', relief='sunken')
button1_2 = Button(frame1, width=6, font=('', 10))
button1_3 = Button(frame1, width=9, text='코로나 달력', font=('', 10))
button1_1.grid(row=0, column=0, padx=(28, 10), pady=(28, 12), sticky='w')
label1_1.grid(row=0, column=1, pady=(28, 12), sticky='we')
button1_2.grid(row=0, column=2, padx=(10, 28), pady=(28, 12), sticky='e')
button1_3.grid(row=1, column=0, columnspan=3, padx=(10, 28), sticky='e')


frame2 = LabelFrame(master_frame, text=' 서울시 코로나 발생동향 ', labelanchor='n', font=('', 12))
frame2.pack(expand=True, pady=(0, 15))


frame3 = LabelFrame(master_frame, text=' 대한민국 코로나 발생동향 ', labelanchor='n', font=('', 12))
frame3.pack(pady=(0, 15))


frame4 = LabelFrame(master_frame, text=' 지역별 신규 확진자 발생인원/비율 ', labelanchor='n', font=('', 12))


frame5 = LabelFrame(master_frame, text=' 지역별 확진자 발생인원/비율 ', labelanchor='n', font=('', 12))


frame6 = LabelFrame(master_frame, text=' 날짜별 확진자 발생인원 ', labelanchor='n', font=('', 12))


frame7 = LabelFrame(master_frame, text=' 코로나 관련 뉴스 ', labelanchor='n', font=('', 12))


refresh()
tk.mainloop()
