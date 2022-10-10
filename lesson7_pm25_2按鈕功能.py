import tkinter as tk
import csv
import requests                                                     
from io import StringIO  

class Windows(tk.Tk):
    def __init__(self,county):                                      
        super().__init__()
        self.county  = county
        self.title("空氣品質指標(AQI)概況")                                                             #增加視窗名稱
        tk.Label(self,text="空氣品質指標(AQI)概況",font=("arial",16,"bold")).pack(padx=20,pady=50)      #增加按鈕標題
        mainFrame = tk.Frame(self)                                                                     #增加按鈕框架
        # 增加按鈕功能
        for index,county_str in enumerate(self.county):
            btn = tk.Button(mainFrame,text=county_str,font=("arial",16),padx=10,pady=10).grid(row=index//3,column= index%3,padx=10,pady=10)
            # 按鈕按照讀出來的"名稱(county_str)"排列，排列方式對照index對"3"的商與餘數排列
            btn.bind("<Button>",self.buttonclick)
            btn.grid(row=index//3,column= index%3,padx=10,pady=10)
            # 自己寫的，不知道為何這段沒有跟btn有同樣的屬性(bind、grid沒有變色)
        mainFrame.pack()

    def buttonclick(self,event):
        print('button click')
        county_name = event.widget['text']
        print(county_name)


def main():
    county = get_county()                                           
    windows = Windows(county)                                       
    windows.mainloop()                                              

def get_county():                
    url = "https://data.epa.gov.tw/api/v2/stat_p_115?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate desc&format=CSV"
    response = requests.get(url)
    response.encoding = "utf-8"                                  
    with StringIO(response.text) as like_file:
        csv_reader = csv.reader(like_file)
        csv_list = list(csv_reader)
    county_set = set()                                               
    for item in csv_list:                                               
        county_set.add(item[1])                                         
    county_set.remove('item2')                                         
    county_set.remove('總計')                                          
    county = list(county_set)                                           
    return county


if __name__ == '__main__':
    main()