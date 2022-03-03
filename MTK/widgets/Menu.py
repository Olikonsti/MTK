from MTK.GLOBAL import *
from MTK.widgets.Toplevel import *





class Menu(Toplevel):
    def __init__(self, window, text, command=None, menus=[]):
        super().__init__(window, empty=True)
        self.text = text
        self.window = window
        self.menus=[]
        self.bounds=[0, 0, 0, 0]
        self.in_border = True
        self.height = 0
        self.width = 50
        for i in menus:
            m_btn = Button(self, text=i.text).pack()
            self.height+= 50
            if len(i.menus) > 0:
                m_btn.config(command=i.open)


    def openat(self, x, y):
        self.grab_set()
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.bounds = [x, y, x + self.width, y + self.height]
        self.bind("<Button-1>", self.update_task)

    def open(self):
        self.grab_set()
        x = self.window.winfo_pointerx()
        y = self.window.winfo_pointery()
        #x = x + self.window.winfo_x()
        #y = y + self.window.winfo_y()
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.bounds = [x, y, x+self.width, y+self.height]
        self.bind("<Button-1>", self.update_task)

    def update_task(self, event=None):
        if self.window.winfo_pointerx() < self.bounds[0] or self.window.winfo_pointerx() > self.bounds[2]:
            self.close()
        else:
            if self.window.winfo_pointery() <  self.bounds[1] or self.window.winfo_pointery() > self.bounds[3]:
                self.close()
            else:
                self.in_border = True

    def close(self):
        self.in_border = False
        self.destroy()