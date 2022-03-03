from MTK.GLOBAL import *

from MTK.widgets.Toplevel import *

class Popup(Toplevel):
    def __init__(self, parent, title, text):
        super().__init__(parent, empty=True)
        self.parent = parent

        self.geometry(f"400x200+{self.parent.winfo_x()+int(self.parent.winfo_width()/2-200)}+{self.parent.winfo_y()+int(self.parent.winfo_height()/2-100)}")
        self.update()
        self.parent.lift()
        title_bar = Frame(self)
        title_bar.pack(fill=X)
        Label(title_bar, text=title, font="Helvetica 13").pack(side=LEFT)
        self.close_btn = Button(title_bar, text="X", command=self.close).pack(side=RIGHT, padx=1, pady=1)
        Label(self, text=text, wraplength=300, font="Helvetica 10").pack(anchor=W, padx=10, pady=3, side=LEFT)
        self.bottom_bar = Frame(self)
        self.bottom_bar.pack(side=BOTTOM, fill=X)
        #Button(self.bottom_bar, text="Ok").pack(side=RIGHT, padx=4, pady=4)

        self.grab_set()
        self.config(bd=1, highlightthickness=1, highlightbackground="#2e2e2e", highlightcolor="#2e2e2e")
        self.protocol('WM_DELETE_WINDOW', self.close)

        self.update_task()


    def update_task(self):
        try:
            self.geometry(f"{self.winfo_width()}x{self.winfo_height()}+{self.parent.winfo_x()+int(self.parent.winfo_width()/2-self.winfo_width()/2)}+{self.parent.winfo_y()+int(self.parent.winfo_height()/2-self.winfo_height()/2)}")
            self.lift()
            self.upd_task_obj = self.after(100, self.update_task)
        except:
            pass


    def close(self):
        self.parent.grab_release()
        self.destroy()

