import MTK

f = MTK.Window()


y = MTK.Button(f, text="YEET")
y.pack(padx=100, pady=100)

d = MTK.Scrollframe(f, show_scrollbar=False)
d.pack()

for i in range(10):
    MTK.Button(d, text="YEEE").pack(padx=10, pady=10)

f.mainloop()