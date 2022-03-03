from MTK.GLOBAL import *

class Window(Tk):
    def __init__(self, blur=True, empty=False, *args, **kwargs):
        self.blur = blur
        super().__init__(*args, **kwargs)

        self.tk.call("source", "MTK/sun-valley.tcl")
        self.tk.call("set_theme", "dark")

        if empty:
            self.overrideredirect(True)

        self.geometry("600x500")
        self.title("MTK GUI")
        self.iconbitmap("MTK/theme/icon.ico")

        if blur:
            enable_blur(self, dark_mode=True)

    def reenable_blur(self):
        if self.blur:
            enable_blur(self, dark_mode=True)
