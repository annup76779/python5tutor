import tkinter as Tk



win = Tk.Tk()
btn = Tk.Button(win, text="button", command = lambda: call())
btn.pack()


win.mainloop()