from cProfile import label
import tkinter as tk

class click(tk.Tk):                                                     #這段要導入tkinter中的Tk功能，下面的mainloop才會能夠執行
    def __init__(self):
        super().__init__()                                              #物件導向的都需要有這句，才能夠正確執行。目前猜測是繼承class中的tk.Tk功能
        fm = tk.Frame
        self.title=('Button Windows!')
        label = tk.Label(self,text='Hello world!')
        tk.Button(text='BUTTON1',font=('ariel',20),padx=10,pady=20).grid(row=0,column=1,padx=10,pady=20)
        tk.Button(text='BUTTON2',font=('ariel',20)).grid(row=1,column=1,padx=10,pady=20)
        tk.Button(text='BUTTON3',font=('ariel',20)).grid(row=2,column=1,padx=10,pady=20)
        tk.Button(text='BUTTON4',font=('ariel',20)).grid(row=0,column=2,padx=10,pady=20)
        tk.Button(text='BUTTON5',font=('ariel',20)).grid(row=1,column=2,padx=10,pady=20)
        tk.Button(text='BUTTON6',font=('ariel',20)).grid(row=2,column=2,padx=10,pady=20)
def main():
    window = click()
    window.mainloop()

if __name__ == '__main__':
    main()