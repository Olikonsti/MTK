from MTK.GLOBAL import *

class Window(Tk):
    def __init__(self, blur=True, *args, **kwargs):
        self.blur = blur
        super().__init__(*args, **kwargs)
        self.geometry("600x500")
        self.tk.call("source", "MTK/sun-valley.tcl")
        self.tk.call("set_theme", "dark")
        self.title("MTK GUI")
        self.iconbitmap("MTK/theme/icon.ico")

        if blur:
            enable_blur(self, dark_mode=True)

    def reenable_blur(self):
        if self.blur:
            enable_blur(self, dark_mode=True)
