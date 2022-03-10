from MTK.GLOBAL import *
from MTK.widgets.Toplevel import *





class Menu(Toplevel):
    def __init__(self, window, text, command=None, menus=[]):
        super().__init__(window, empty=True)
        self.text = text
        self.window = window
        self.x = 0
        self.y = 0
        self.parent_menu = None
        self.menus=menus
        self.bounds=[0, 0, 0, 0]
        self.in_border = True
        self.height = 0
        self.width = 200
        for i in menus:
            m_btn = Button(self, text=i.text)
            m_btn.pack(fill=X)
            self.height+= 33
            if len(i.menus) > 0:
                m_btn.config(command=lambda: i._open_by_topmenu(self, m_btn.winfo_y()))
                m_btn["text"] = m_btn["text"]
            else:
                m_btn.config(command=i.command)

    def openat(self, x, y):
        try:
            self.grab_set()
        except:
            self.__init__(self.window, self.text, self.command, self.menus)
            self.grab_set()
        self.x = x
        self.y = y
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.bounds = [x, y, x + self.width, y + self.height]
        self.bind("<Button-1>", self.update_task)

    def _update_binds(self):
        print("updating binds")
        self.window.bind("<Button-1>", self.update_task)
        self.bind("<Button-1>", self.update_task)
        if self.parent_menu != None:
            self.parent_menu._update_binds()

    def open(self):
        print("opening...")
        x = self.window.winfo_pointerx()
        y = self.window.winfo_pointery()
        self.openat(x, y)

    def _open_by_topmenu(self, menu, y_off):
        #self.update_task()
        self.openat(menu.x+menu.winfo_width(), menu.y+y_off)
        self.parent_menu = menu

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

        if self.parent_menu != None:
            self.parent_menu.update_task()
            self.parent_menu._update_binds()

