import tkinter as tk
window = tk.Tk()
window.title("Menu")
window.geometry("500x500")

#主選單(選單列)
menubar = tk.Menu(window)

#子選單(第二層)
filemenu = tk.Menu(menubar,tearoff = False)
filemenu.add_command(label="開新遊戲")
filemenu.add_command(label="作弊指令")
filemenu.add_separator() #分隔線
filemenu.add_command(label = "EXIT")
#設定好子選單(第二層)視窗後，再包進主選單(選單列)內
menubar.add_cascade(label="檔案",menu = filemenu)

#第二個子選單(第二層)
filemenu2 = tk.Menu(menubar,tearoff=False)
filemenu2.add_command(label="遊戲設定")
filemenu2.add_command(label="畫面設定")
menubar.add_cascade(label="設定",menu=filemenu2)

#選項(第二個子選單)->進階設定->第三層選單(submenu)
submenu = tk.Menu(menubar,tearoff=False)
submenu.add_command(label="遊戲優化")
submenu.add_command(label="攻擊敵人")
#設定好第三層選單(submenu)視窗後，再包進第二個子選單內
filemenu2.add_cascade(label="進階設定",menu=submenu)

filemenu3 = tk.Menu(menubar,tearoff=False)
filemenu3.add_command(label="靈敏度")
filemenu3.add_command(label="聲音調整")
menubar.add_cascade(label="輔助設定",menu=filemenu2)

submenu2 = tk.Menu(menubar,tearoff=False)
submenu2.add_command(label="光影")
submenu2.add_command(label="畫質")
filemenu3.add_cascade(label="畫面設定",menu=submenu)

filemenu4 = tk.Menu(menubar,tearoff=False)
filemenu4.add_command(label="搖桿操作")
menubar.add_cascade(label="操作設定",menu=filemenu2)

submenu3 = tk.Menu(menubar,tearoff=False)
submenu3.add_command(label="鍵盤操作")
filemenu4.add_cascade(label="鍵盤設定",menu=submenu)


#修改window屬性，把我們設定好的menu放進去
window.config(menu=menubar)

#開始跑視窗
window.mainloop()