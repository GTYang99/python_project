import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("side")
        fm = tk.Frame(self)         #定義一個fm使用tk.Frame功能
        tk.Button(fm,text="Top",font=('verdana',20)).pack(side=tk.TOP)
        tk.Button(fm,text="Center",font=('verdana',20)).pack(side=tk.LEFT)
        tk.Button(fm,text="Bottom",font=('verdana',20)).pack(side=tk.RIGHT)
        #tk.Button(按鈕來自於tk中自帶的功能),裡面的參數使用fm功能,所以先輸入fm,再修改按鈕內容,需要學習
        fm.pack()

def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()