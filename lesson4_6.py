import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("side")
        self.geometry("500x200")
        fm = tk.Frame(self,background="#eeeeee")                                        #給出框架顏色
        tk.Button(fm,text="Top",font=('verdana',20)).pack(side=tk.LEFT,fill=tk.Y)       #讓按鈕填充滿哪個區域(tk.y)
        tk.Button(fm,text="Center",font=('verdana',20)).pack(side=tk.LEFT,fill=tk.Y)
        tk.Button(fm,text="Bottom",font=('verdana',20)).pack(side=tk.LEFT,fill=tk.Y)
        fm.pack(fill=tk.Y,expand=True)                                                  #fm.pack功能需要再學習
        
def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()