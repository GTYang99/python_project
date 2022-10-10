import tkinter as tk

class Window(tk.Tk):                                    #使用tk中Tk的功能
    def __init__(self):
        super().__init__()                              #繼承init父類別的內容
        self.title("Hello! Tkinnter")                   #可以寫進def裡面直接使用windows中的方法
        label = tk.Label(self,text="Hello Tkinter!")    #何時使用self. 何時不使用需要學習?
        label.pack(padx=100, pady=50)                   #pack為最基礎的布局方式;padx = padding,

def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()   
