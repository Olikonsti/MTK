# MTK Documentation

 
# Theme

I am using the Sun-Valley-ttk-theme: https://github.com/rdbende/Sun-Valley-ttk-theme

# Fully supported widgets
- Window
- Scrollframe

# Widgets

compatible with tkinter and tkinter.ttk widgets

### MTK.Window(blur=True, empty=False, start_hidden=False, \*args, \*\*kwargs)
Inherits from Tk()\
empty=True removes title bar\
Main window\
blur and black title bar only compatible with Windows 11\
blur needs to be reenabled with window.reenable_blur() after running window.resizeable()\

### MTK.Toplevel(parent, blur=True, empty=False \*args, \*\*kwargs)
Inherits from Toplevel()\
empty=True removes title bar\
a secondary window for a main window\
blur only compatible with Windows 11



### MTK.Scrollframe(parent, bg=None, fg=None, show_scrollbar=False, *args, **kwargs)
Inherits from ttk.Frame()\
A Scrollframe Widget for Windows with mouse bindings and a optional scrollbar

### MTK.Console(title="MTK Console", minimized=True, disable_exec=False)
Inherits from MTK.Window()\
a console made in tkinter to display log messages\
set disable_exit=True if the user should not be able to execute python code in the console\
`console.log(msg, color="white")` show message in log window\
``console.hide()`` hide console\
``console.show()`` show console

### MTK.Popup(parent)
Inherits from MTK.Toplevel()\
creates a popup message that disables the parents window controls\
add buttons to popup by using popup.bottom_bar as their parent

### MTK.Menubar(menus=[])

### MTK.Menu()


