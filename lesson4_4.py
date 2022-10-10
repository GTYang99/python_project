import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("side")
        tk.Button(self,text="Top").pack(side=tk.LEFT)           #利用pack方法,將按鈕排成橫向
        tk.Button(self,text="Center").pack(side=tk.LEFT)
        tk.Button(self,text="Bottom").pack(side=tk.LEFT)

def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()