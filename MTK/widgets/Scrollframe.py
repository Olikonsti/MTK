from tkinter import *
import tkinter.ttk as ttk
import functools
fp = functools.partial


class Scrollframe(ttk.Frame):
    def __init__(self, parent, bg=None, fg=None, show_scrollbar=False, *args, **kw):
        self.border_frame = ttk.Frame(parent)
        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=interior.winfo_reqwidth())

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                # update the inner frame's width to fill the canvas
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        """
        This is linux code for scrolling the window, 
        It has different buttons for scrolling the windows
        
        def _on_mousewheel(event, scroll):
            canvas.yview_scroll(int(scroll), "units")

        def _bind_to_mousewheel(event):
            canvas.bind_all("<Button-4>", fp(_on_mousewheel, scroll=-1))
            canvas.bind_all("<Button-5>", fp(_on_mousewheel, scroll=1))

        def _unbind_from_mousewheel(event):
            canvas.unbind_all("<Button-4>")
            canvas.unbind_all("<Button-5>")
        """


        """
        This is windows code for scrolling the Frame
        """
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        def _bind_to_mousewheel(event):
            canvas.bind_all("<MouseWheel>", _on_mousewheel)
        def _unbind_from_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")



        # create a canvas object and a vertical scrollbar for scrolling it
        if show_scrollbar == False:
            tf = Frame(self.border_frame, width=0)
            tf.pack_propagate(False)
        else:
            tf = Frame(self.border_frame)
            tf.pack(fill=Y, side=RIGHT, expand=FALSE)


        vscrollbar = ttk.Scrollbar(tf, orient=VERTICAL)
        self.vscrollbar = vscrollbar
        vscrollbar.pack(fill=Y, expand=True)
        canvas = Canvas(self.border_frame, bd=0, highlightthickness=0,
                           yscrollcommand=vscrollbar.set)
        self.canvas = canvas
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        vscrollbar.config(command=canvas.yview)

        if bg != None:
            self.canvas.config(bg=bg)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it

        super().__init__(canvas, *args, **kw)
        interior = self
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        interior.bind('<Configure>', _configure_interior)
        canvas.bind('<Configure>', _configure_canvas)
        canvas.bind('<Enter>', _bind_to_mousewheel)
        canvas.bind('<Leave>', _unbind_from_mousewheel)

    def scroll_to_bottom(self):
        self.canvas.yview_moveto(1.0)

    def pack(self, *args, **kw):
        self.border_frame.pack(*args, **kw)
