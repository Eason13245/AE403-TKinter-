import tkinter as tk

window = tk.Tk()
window.geometry('300x300')
window.title("單選按鈕")

t = tk.StringVar()
t2 = tk.StringVar()

def selection (): 
    label.config(text = 'I love' + t.get() + ", at " + t2.get() + ".")

label = tk.Label(window, bg ='#F00', text = 'have not chosen')
label.pack()

radio1 = tk.Radiobutton(window, text = 'Minecraft Python', variable = t, value = ' to play minecraft', command = selection )
radio1.pack()

radio2 = tk.Radiobutton(window, text = 'Animes', variable = t, value = ' to watch animes', command = selection )
radio2.pack()

radio3 = tk.Radiobutton(window, text = 'Reading', variable = t, value = ' to read novels', command = selection)
radio3.pack()

radio4 = tk.Radiobutton(window, text = 'Home', variable = t2, value = ' home', command = selection)
radio4.pack()

radio5 = tk.Radiobutton(window, text = 'School', variable = t2, value = ' school', command = selection)
radio5.pack()

window.mainloop()