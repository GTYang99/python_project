import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Event")
        fm = tk.Frame(self,background="#eeeeee")
        btn = tk.Button(fm,text="Click Me")                     #創建一個按鈕
        btn.bind("<Button-1>",self.enter)                       #使用.bind做一個測試點右鍵
        btn.pack(expand=True,fill=tk.BOTH)                      #button大小設計
        fm.pack(expand=True,fill=tk.BOTH,padx=20,pady=20)       #Frame大小設計

    def enter(self,event):
        print(f"enter Frame: x={event.x}, y={event.y}")         #讀取座標工具
        


def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()