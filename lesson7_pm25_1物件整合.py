import tkinter as tk
import csv
import requests                                                     #這些方法都可以在code前先引用
from io import StringIO  

class Windows(tk.Tk):
    def __init__(self,county):                                      #在物件中多加一個county參數，先宣告這個物件
        self.county = county                                        #讓底下的實體能夠等同於物件的county
        print(county)                                               #該物件的目的，列印conty
        super().__init__()
        for county_str in self.county:                              #增加一個按鈕功能，按鈕內容包括使用for迴圈遍歷過self.county，並儲存在county_str中，
            tk.Button(self,text=county_str).pack(side=tk.LEFT)      #按鈕內容文字採用for迴圈遍歷完的值，輸入進去


def main():
    county = get_county()                                           #主要執行get_county這支程式，並把這個結果回傳給county
    windows = Windows(county)                                       #視窗介面
    windows.mainloop()                                              #結束Windows必須執行這個

def get_county():                
    url = "https://data.epa.gov.tw/api/v2/stat_p_115?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate desc&format=CSV"
    response = requests.get(url)
    response.encoding = "utf-8"                                  
    with StringIO(response.text) as like_file:
        csv_reader = csv.reader(like_file)
        csv_list = list(csv_reader)
    county_set = set()                                               #建立一個空set
    for item in csv_list:                                               #遍歷csv_list這個文件中的item
        county_set.add(item[1])                                         #將遍歷過的item加到新創的set,此時重複的縣市會被刪除，set數據結構特性
    county_set.remove('item2')                                          #移除不是縣市的語句
    county_set.remove('總計')                                           #移除不是縣市的語句2
    county = list(county_set)                                           #將set轉為list
    return county


if __name__ == '__main__':
    main()