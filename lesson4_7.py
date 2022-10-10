import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("side")
        self.geometry("500x200")
        fm = tk.Frame(self,background="#eeeeee")
        tk.Button(fm,text="Top",font=('verdana',20)).pack(side=tk.LEFT,expand=True)         #expand是擴展到layer的區域
        tk.Button(fm,text="Center",font=('verdana',20)).pack(side=tk.LEFT,expand=True)
        tk.Button(fm,text="Bottom",font=('verdana',20)).pack(side=tk.LEFT,expand=True)      
        fm.pack(fill=tk.BOTH,expand=True)                                                   #fill是另一塊區域
        


def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()