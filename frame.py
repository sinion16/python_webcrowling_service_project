# frame.py

import tkinter
from tkinter import *
import crawling


global page
page = 0


def view():
    tk.mainloop()


def hide():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()


def refresh():
    global page

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

        sub_list = list[0][2]
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
            label = Label(frame4, width=12, text=sub_list[2][i] + '명 ' + sub_list[4][i] + '%',
                          font=('', 12), fg=font_color, borderwidth=0)
            label.grid(row=s+1, column=c)
            if i == len(sub_list[0])-1:
                label = Label(frame4, width=12, text='총 합', font=('', 12), borderwidth=0)
                label.grid(row=s, column=c+1, padx=12, pady=(2, 0))
                label = Label(frame4, width=12, text=list[0][0][0][0] + '명', font=('', 12), borderwidth=0)
                label.grid(row=s+1, column=c+1, padx=12, pady=(0, 4))
            c = c + 1

    def click1_2():
        hide()
        frame5.pack()
        button1_1.config(text='돌아가기', command=back)

        sub_list = list[0][2]

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
            label = Label(frame5, width=12, text=sub_list[1][i] + '명 ' + sub_list[3][i] + '%',
                          font=('', 12), fg=font_color, borderwidth=0)
            label.grid(row=s+1, column=c)
            if i == len(sub_list[0])-1:
                label = Label(frame5, width=12, text='총 합', font=('', 12), borderwidth=0)
                label.grid(row=s, column=c+1, padx=12, pady=(2, 0))
                label = Label(frame5, width=12, text=list[0][0][0][1] + '명', font=('', 12), borderwidth=0)
                label.grid(row=s+1, column=c+1, padx=12, pady=(0, 4))
            c = c + 1

    def click1_3():
        hide()
        frame6.pack()
        button1_1.config(text='돌아가기', command=back)

        sub_list = list[0][5]

        d = 7
        c = 0
        s = 0
        for i in range(0, len(sub_list[0])):
            if c == d:
                c = 0
                s = s + 3

            if sub_list[0][i] == '1':
                text1 = list[1][2][1] + '. ' + sub_list[0][i] + '.'
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
            label = Label(frame6, width=9, text=text1,
                          font=('', 12), height=1, borderwidth=0)
            label.grid(row=s, column=c, pady=(6, 0))
            label = Label(frame6, width=9, text=text2,
                          font=('', 9), height=1, borderwidth=0)
            label.grid(row=s + 1, column=c)
            label = Label(frame6, width=9, text=text3,
                          font=('', 9), height=1, borderwidth=0)
            label.grid(row=s + 2, column=c)
            if i == len(sub_list[0])-1:
                label.grid(pady=(0, 10))
            c = c + 1

    button1_1.config(text='새로고침')

    if page == 0:
        hide()
        frame2.pack()
        frame3.pack()
        button1_3.config(command=click1_3)

        list = crawling.seoul()
        # for i in range(len(list[0])):
        #     print(list[0][i])
        # print(list[1])

        seoul = list[0][0]
        korea = list[0][1]

        label = Label(frame2, text=list[1][0])
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

        label = Label(frame3, text=list[1][1])
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


tk = Tk()
tk.title('corona')
tk.geometry('600x400')


master_frame = Frame(tk, width=600, height=400)
master_frame.pack()


frame1 = Frame(master_frame)
frame1.pack()

button1_1 = Button(frame1, width=6, text='새로고침', font=('', 10), command=refresh)
label1_1 = Label(frame1, width=42, text='뉴스제목', font=('', 12), bg='white', relief='sunken')
button1_2 = Button(frame1, width=6, text='더 보 기', font=('', 10), command='')
button1_3 = Button(frame1, width=9, text='코로나 달력', font=('', 10))
button1_1.grid(row=0, column=0, padx=(40, 10), pady=(28, 12))
label1_1.grid(row=0, column=1, pady=(28, 12))
button1_2.grid(row=0, column=2, padx=(10, 40), pady=(28, 12))
button1_3.grid(row=1, column=0, columnspan=3, padx=(10, 40), sticky='e')


frame2 = LabelFrame(master_frame, text=' 서울시 코로나 발생동향 ', labelanchor='n', font=('', 12))
frame2.pack(expand=True, pady=(0, 15))


frame3 = LabelFrame(master_frame, text=' 대한민국 코로나 발생동향 ', labelanchor='n', font=('', 12))
frame3.pack(pady=(0, 15))


frame4 = LabelFrame(master_frame, text=' 지역별 신규 확진자 발생인원/비율 ', labelanchor='n', font=('', 12))


frame5 = LabelFrame(master_frame, text=' 지역별 확진자 발생인원/비율 ', labelanchor='n', font=('', 12))


frame6 = LabelFrame(master_frame, text=' 날짜별 확진자 발생인원 ', labelanchor='n', font=('', 12))

refresh()
tk.mainloop()
