from MTK.GLOBAL import *
from MTK.widgets.Toplevel import *

class Emptytoplevel(Toplevel):
    def __init__(self, parent, blur=True, *args, **kwargs):
        super().__init__(parent, blur, *args, **kwargs)
        self.overrideredirect(True)
        self.reenable_blur()