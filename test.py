
from tkinter import Button, Tk


class MainWin(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.buttons = {}
        self.dat = ["A", "B", "C", "D"]
        self.init_widgets()

    def init_widgets(self):
        for i, d in enumerate(self.dat):
            btn = Button(
                self,
                width=10,
                text=f"{i}-{d}",
                command=lambda x=i: self.on_click(x),
            )
            btn.grid(row=i, column=0)
            self.buttons[i] = btn

    def on_click(self, i):
        print(f"{i} clicked")


if __name__ == "__main__":
    app = MainWin(None)
    app.mainloop()