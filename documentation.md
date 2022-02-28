# MTK Documentation

 
# Theme

I am using the Sun-Valley-ttk-theme: https://github.com/rdbende/Sun-Valley-ttk-theme

# Fully supported widgets
- Window
- Scrollframe

# Widgets

compatible with tkinter and tkinter.ttk widgets

### MTK.Window(blur=True, \*args, \*\*kwargs)
Inherits from Tk()\
Main window\
blur and black title bar only compatible with Windows 11\
blur needs to be reenabled with window.reenable_blur() after running window.resizeable()

### MTK.Scrollframe(parent, bg=None, fg=None, show_scrollbar=False, *args, **kwargs)
Inherits from ttk.Frame()\
A Scrollframe Widget for Windows with mouse bindings and a optional scrollbar

### MTK.Emptywindow(blur=True, \*args, \*\*kwargs)
Inherits from MTK.Window()\
Main window without title bar\
blur only compatible with Windows 11

### MTK.Console(minimized=True, disable_exec=False)
a console made in tkinter to display log messages\
set disable_exit=True if the user should not be able to execute python code in the console\
`console.log(msg, color="white")` show message in log window\
``console.hide()`` hide console\
``console.show()`` show console
