from MTK.GLOBAL import *

class Toplevel(Toplevel):
    def __init__(self, parent, blur=True, empty=False, *args, **kwargs):
        self.blur = blur
        super().__init__(parent, *args, **kwargs)

        self.geometry("600x500+10000+10000")

        if empty:
            self.overrideredirect(True)


        self.title("MTK GUI")
        self.iconbitmap("MTK/theme/icon.ico")

        if blur:
            enable_blur(self, dark_mode=True)

    def reenable_blur(self):
        if self.blur:
            enable_blur(self, dark_mode=True)
