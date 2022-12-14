# 按鈕功能返回縣市

import tkinter as tk
import requests
from io import StringIO
import csv

class Window(tk.Tk):
    def __init__(self,county):
        super().__init__()
        self.county  = county
        self.title("空氣品質指標(AQI)概況")
        tk.Label(self,text="空氣品質指標(AQI)概況",font=("arial",20,"bold")).pack(padx=20,pady=50)
        mainFrame = tk.Frame(self)
        # 加入按鈕功能；並使用 enumerate() 函式來同時輸出索引與元素；設置一個參數btn作為按鈕，
        for index,county_str in enumerate(self.county):
            btn = tk.Button(mainFrame,text=county_str,font=("arial",16),padx=10,pady=10)
            # Bind是用來將控制元件事件與控制元件做繫結的，表示按了按鈕出現那些內容
            btn.bind("<Button>",self.buttonClick)
            btn.grid(row=index//3,column= index%3,padx=10,pady=10)
        mainFrame.pack()

    def buttonClick(self,event):
        print("button click")
        county_name = event.widget["text"]
        print(county_name)

def main():
    county = get_county()
    window = Window(county)    
    window.mainloop()

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
    county_set.remove("item2")
    county_set.remove("總計")
    county = list(county_set)
    return county

if __name__ == "__main__":
    main()