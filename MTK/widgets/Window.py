from MTK.GLOBAL import *

class Window(Tk):
    def __init__(self, blur=True, darktitlebar=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tk.call("source", "MTK/sun-valley.tcl")
        self.tk.call("set_theme", "dark")
        self.title("MTK_GUI")
        self.iconbitmap("MTK/theme/icon.ico")



        if blur:
            enable_blur(self, dark_mode=True)
