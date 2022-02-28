from MTK.GLOBAL import *
from MTK.widgets.Window import *

class Emptywindow(Window):
    def __init__(self, blur=True, *args, **kwargs):
        super().__init__(blur, *args, **kwargs)
        self.overrideredirect(True)
        self.reenable_blur()