from MTK.GLOBAL import *
import MTK

from MTK.GLOBAL import *
from MTK.widgets.Window import *
from MTK.widgets.Scrollframe import *
from MTK.widgets.Popup import *

class Console(Window):
    def __init__(self, title="MTK Console", minimized=True, disable_exec=False):
        super().__init__(blur=True)
        if minimized:
            self.hide()
        self.update()
        self.geometry("800x560")
        self.minimized = minimized
        menubar = Menu(self)
        self.config(menu=menubar)
        _menu = Menu(menubar)
        _menu.add_command(label='Export log to file', command=self.export)
        menubar.add_cascade(label="Options", menu=_menu)
        self.update()
        self.log_list = []

        self.update()

        self.title(title)
        self.scrollarea = Scrollframe(self, show_scrollbar=True)
        self.scrollarea.pack(expand=True, fill=BOTH)
        self.bottom_frame = Frame(self)
        self.bottom_frame.pack(fill=X, side=BOTTOM)
        self.command_entry = ttk.Entry(self.bottom_frame, font="Consolas 11")
        self.command_entry.pack(side=LEFT, fill=X, expand=True)
        self.run_button = ttk.Button(self.bottom_frame, text="Enter", command=self.run)
        self.run_button.pack(side=RIGHT, padx=5, pady=5)
        if disable_exec:
            self.command_entry.insert(0, "Input disabled")
            self.command_entry["state"] = DISABLED
            self.run_button["state"] = DISABLED


        self.protocol('WM_DELETE_WINDOW', self.hide)
        self.show_on_update = False
        self.update()
        self.update_task()

    def export(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".log")
        if f is None:
            return
        text = ""
        for i in self.log_list:
            text += f"{i}\n"
        f.write(text)
        f.close()
        Popup(self, title="Info", text="File saved")

    def run(self):
        try:
            exec(self.command_entry.get())
        except Exception as e:
            self.log(f"CONSOLE_ERROR: {e}")

    def update_task(self):
        if self.show_on_update:
            self.show()
            self.show_on_update = False
        self.after(100, self.update_task)

    def log(self, msg, color="white"):
        f = Frame(self.scrollarea)
        f.pack(fill=X)
        secondsSinceEpoch = time.time()
        timeObj = time.localtime(secondsSinceEpoch)
        timestamp = '%d-%d-%d %d:%d:%d> ' % (timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year, timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec)
        TK.Label(f, text=timestamp, wraplength=self.winfo_width() - 30, justify=LEFT, font="Consolas 11").pack(side=LEFT)
        TK.Label(f, text=msg, wraplength=self.winfo_width()-200, justify=LEFT, font="Consolas 11", fg=color).pack(side=LEFT)
        self.log_list.append(f"{timestamp}>> {msg}")
        if not self.minimized:
            self.update()
            self.scrollarea.scroll_to_bottom()

    def prep_show_on_update(self):
        self.show_on_update = True

    def hide(self):
        self.minimized = True
        self.withdraw()
        image = Image.open("MTK/theme/icon.ico")
        menu = [pystray.MenuItem('Show Console', self.prep_show_on_update)]
        icon = pystray.Icon("name", image, "MTK Console", menu=menu)
        icon.run_detached()
        self.icon = icon

    def show(self, icon=None):
        self.icon.stop()
        self.minimized = False
        self.deiconify()
        self.overrideredirect(False)
        self.reenable_blur()
        self.scrollarea.scroll_to_bottom()