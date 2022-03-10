from MTK.GLOBAL import *

class Window(Tk):
    def __init__(self, blur=True, empty=False, start_hidden=False, *args, **kwargs):
        self.blur = blur
        self.start_hidden = start_hidden
        super().__init__(*args, **kwargs)
        self.withdraw()
        self.config(bg="#1c1c1c")
        self.tk.call("source", "MTK/sun-valley.tcl")
        self.tk.call("set_theme", "dark")

        if empty:
            self.overrideredirect(True)

        self.geometry("600x500")
        self.title("MTK GUI")
        self.iconbitmap("MTK/theme/icon.ico")

        if blur:
            enable_blur(self, dark_mode=True)

        self.after(2, self._start_unhide)

    def _start_unhide(self):
        if not self.start_hidden:
            self.deiconify()

    def reenable_blur(self):
        if self.blur:
            enable_blur(self, dark_mode=True)
