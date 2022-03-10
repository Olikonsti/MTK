import MTK

f = MTK.Window()

d = MTK.Console(minimized=True, disable_exec=True)

for i in range(100):
    d.log("TestMessage", color="green")


y = MTK.Button(f, text="open console", command=d.show)
y.pack(padx=100, pady=100)

d = MTK.Scrollframe(f, show_scrollbar=True)
d.pack()

def op_m():
    m = MTK.Menu(f, text="MAIN",
                 menus=[
                     MTK.Menu(f, text="YEET!", command=lambda: print("yeee")),
                     MTK.Menu(f, text="YEET!", command=lambda: print("yeee2")),
                     MTK.Menu(f, text="MENU!", menus=
                                    [
                                        MTK.Menu(f, text="YT!", command=lambda: print("yeee3")),
                                        MTK.Menu(f, text="YT!", menus=
                                                 [
                                                     MTK.Menu(f, text="YT!", command=lambda: print("yeee3")),
                                                 ]),
                                    ]
                              )
                 ]
            )
    m.open()

for i in range(50):
    MTK.Button(d, text="YEEE", command=op_m).pack(padx=1, pady=1)



f.mainloop()