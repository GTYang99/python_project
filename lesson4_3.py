import tkinter as tk

class Window(tk.Tk):                                    #使用tk中Tk的功能
    def __init__(self):
        super().__init__()                              #繼承init父類別的內容
        self.title("side")
        tk.Button(self,text="Top").pack()               #原始參數是垂直的
        tk.Button(self,text="Center").pack()
        tk.Button(self,text="Bottom").pack()


def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()   
