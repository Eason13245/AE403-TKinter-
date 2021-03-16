import tkinter as tk

import tkinter.messagebox

window = tk.Tk()

window.title("我的第一個GUI程式")

window.geometry('300x300')

def clickMe():
        tkinter.messagebox.showinfo(title='提示', message= '好累')

label = tk.Label(window,text="我的GUI", bg= "#567", fg = "#BFC")

label.pack()

entry = tk.Entry(window, width = 20)

entry.pack()

button = tk.Button(window, text = "按鈕", command = clickMe)

button.pack()

window.mainloop()
