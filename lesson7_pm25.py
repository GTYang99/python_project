import tkinter as tk
import csv
import requests                                 #這些方法都可以在code前先引用
from io import StringIO  

class Windows(tk.Tk):
    def __init__(self):
        super().__init__()


def main():
    windows = Windows()
    county = get_county()
    print(county)                             #county是個變數，不需要給上括號"print(county)"
    windows.mainloop()                          #結束Windows必須執行這個

def get_county():                
    url = "https://data.epa.gov.tw/api/v2/stat_p_115?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate desc&format=CSV"
    response = requests.get(url)
    response.encoding = "utf-8"                                  
    with StringIO(response.text) as like_file:
        csv_reader = csv.reader(like_file)
        csv_list = list(csv_reader)
    county_set = set()                              #建立一個空set
    for item in csv_list:                           #遍歷csv_list這個文件中的item
        county_set.add(item[1])                     #將遍歷過的item加到新創的set,此時重複的縣市會被刪除，set數據結構特性
    county_set.remove('item2')                      #移除不是縣市的語句
    county_set.remove('總計')                       #移除不是縣市的語句2
    county = list(county_set)                       #將set轉為list
    return county


if __name__ == '__main__':
    main()