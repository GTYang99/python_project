import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Event")
        fm = tk.Frame(self,background="#eeeeee")            #利用tk.Frame製作一個frame框架
        fm.pack(expand=True,fill=tk.BOTH,padx=20,pady=20)
        fm.bind('<Any-Enter>',self.enter)                   #建立一個進出點檢查

    def enter(self,event):                                  #建立一個事件,檢查進入frame的x與y座標
        print(f"enter Frame: x={event.x}, y={event.y}")

def main():
    window = Window()    
    window.mainloop()

if __name__ == '__main__':
    main()