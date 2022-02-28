# MTK Documentation

 
# Theme

I am using the Sun-Valley-ttk-theme: https://github.com/rdbende/Sun-Valley-ttk-theme

# Fully supported widgets
- Window
- Scrollframe

# Widgets

compatible with tkinter and tkinter.ttk widgets

### MTK.Window(parent, blur=True, \*args, \*\*kwargs)
Inherits from Tk()\
Main window\
blur and black title bar only compatible with Windows 11\
blur needs to be reenabled with window.reenable_blur() after running:
>window.resize(), window.overrideredirect()

### MTK.Scrollframe(parent, bg=None, fg=None, show_scrollbar=False, *args, **kwargs)
Inherits from ttk.Frame()\
A Scrollframe Widget for Windows with mouse bindings and a optional scrollbar