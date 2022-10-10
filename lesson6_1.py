import tkinter as tk
from tkinter import font
import requests

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('上市公司每月營業收入彙總表')
        tk.Label(self,text='上市公司每月營業收入彙總表',font=('ariel',20)).pack(padx=50,pady=50)
        tk.Button(self,text='下載資料',font=('arial',20),command=self.download).pack(padx=100,pady=50)
        # 在windows界面中,需要使用的參數都需要重新定義,例如這裡的download;def download 需要縮排,因為是視窗裡面的工具;def download(self)的括號內需要給self,self都必須給上,指的是實體物件的參考

    def download(self):
        url = 'https://mopsfin.twse.com.tw/opendata/t187ap05_L.csv'
        response = requests.get(url)                                    #需要先import resquests,才能叫出來用
        with open('上市公司每月營業收入彙總表.csv','wb') as fd:            #下載並存檔的語法
            for chunk in response.iter_content(chunk_size=128):
                fd.write(chunk)
        response.encoding = 'utf-8'                                     #更改文字編碼
        # print(response.text)

def main():
    window = Window()
    window.mainloop()


if __name__ == '__main__':     
    main()
    