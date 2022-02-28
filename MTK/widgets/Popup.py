from MTK.GLOBAL import *
from MTK.widgets.Emptytoplevel import *

class Popup(Emptytoplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grab_set()
        self.resizable(False, False)
        self.reenable_blur()
        self.config(bd=1, highlightthickness=1, highlightbackground="#2e2e2e", highlightcolor="#2e2e2e")
        self.protocol('WM_DELETE_WINDOW', self.close)
        self.geometry("400x200")
        self.update()
        self.parent.lift()
        self.update_task()


    def update_task(self):
        self.geometry(f"{self.winfo_width()}x{self.winfo_height()}+{self.parent.winfo_x()+int(self.parent.winfo_width()/2-self.winfo_width()/2)}+{self.parent.winfo_y()+int(self.parent.winfo_height()/2-self.winfo_height()/2)}")
        self.lift()
        self.after(10, self.update_task)
^^

    def close(self):
        self.parent.grab_release()
        self.destroy()

