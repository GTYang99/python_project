import tkinter as tk

class Window(tk.Tk):
    # 建構式
    def __init__(self,codes):
        # 繼承父類別的必寫內容
        super().__init__()
        # 建立實體屬性的參考(不確定名稱對不對?)
        self.codes = codes
        self.title("各縣市7天天氣預測")
        print(self.codes)
        tk.Label(self,text="各縣市7天天氣預測", font=('arial', 20)).pack(padx=80, pady=50)
        # 新增按鈕框架(ButtonFrame)，引用tk功能中的框架屬性(tk.Frame)，屬性內容必須寫上self(固定寫法)
        ButtonFrame = tk.Frame(self)
        # 按鈕的設置
        # 4.迴圈遍歷dict，將items設置成類別外的輸入
        # 5.items(dict)會回傳兩個內容，引數索引與引數內容，回傳到cities
        for index,cities in enumerate(self.codes.items()):            
            cname,ename= cities
            # 1.新增按鈕並給予屬性
            # 2.名稱來自於迴圈中dict的cname與ename
            # 3.按鈕排列使用grid，列、行分別設計的算法(餘數、商)排列
            # 6.使用變數(btn)，將原本設置的按鈕內容賦予過去
            btn = tk.Button(ButtonFrame,text=f"{cname}\n{ename}",padx=20,pady=10,width=5)
            # 7.由於變數改變，grid屬性需要跟在變數後(python中固定用法)
            btn.grid(column=index % 4,row=index // 4)
            # 8.新增一個bind方法，當按下按鈕時候('<Button>')，會啟動另一個物件(def btnClick)功能
            btn.bind('<Button>',self.btnClick)
        ButtonFrame.pack()
        
        # # 一、這裡開始要在按鈕下方建立一個顯示回傳值的區域(關閉)
        # # 1.新建一個變數放回傳值內容的"標題"
        # displayFrame = tk.LabelFrame(self,text="台北-Taiwan")
        # # 2.新建一個按鈕，顯示回傳值
        # btn = tk.Button(displayFrame,text=f"HELLO",padx=20,pady=10,width=5)
        # # 似乎是回傳值顯示範圍的一個巢狀寫法
        # # 每個物件都要透過pack做結尾
        # btn.pack()
        # displayFrame.pack()

        # 二、新建一個會改變內容的frame
        # 1.外圍新建一個框架(chage_content_frame)包住要改變的內容範圍
        self.chage_content_frame = tk.Frame(self)                                               #新增五時增加self.
        # 2. 中間是上一段(一)原本的內容
        # self.displayFrame = tk.LabelFrame(chage_content_frame,text="台北-Taiwan")             # 新增三時關閉(1/3)
        # btn = tk.Button(self.displayFrame,text=f"HEllo",padx=20,pady=10,width=5).pack()      # 新增三時關閉(2/3)
        # self.displayFrame.pack()                                                              # 新增三時關閉(3/3)
        self.chage_content_frame.pack()                                                         #新增五時增加self.

    # 新增的物件(def btnClick)功能，self必須要寫，event是常數
    def btnClick(self,event):
        # 新增btn事件常數的widget功能
        btn = event.widget
        # btn事件觸發時，將按鈕中的內容(text)回傳給btn_text
        btn_text = btn['text']
        # print(btn_text)                                                                       # 新增三時關閉(1/2)
        # 會改變內容的frame，需要用destroy做畫面去除的動作
        # self.displayFrame.destroy()                                                           # 新增三時關閉(2/2)

        # 三、將改變內容修改為輸出縣市名稱，並增加新的一個類別(class DisplayFrame)
        # 1.按鈕觸發時，會將文字分割，並傳入變數(nameList)，分割的文字，分別用串列index存成cname與ename
        nameList = btn_text.split()
        cname = nameList[0]
        ename = nameList[1]
        # 變數存入數據後，傳到類別DisplayFrame作使用，(變數回傳方法，學習點)
        print(f'{cname}-{ename}')
        # displayName = DisplayFrame(cname=cname,ename=ename)                         ##新增五時關閉
        
        # 五、增加顯示區域回傳縣市的功能，新增六時關閉
        # displayFrame = DisplayFrame(self.chage_content_frame,cname=cname,ename=ename)
        # displayFrame.pack()

        # 六、原功能未將上次點選跳出畫面去除，新增該功能
        if hasattr(self, 'displayFrame'):
            self.displayFrame.destroy()
        self.displayFrame = DisplayFrame(self.chage_content_frame,cname=cname,ename=ename)
        self.displayFrame.pack()

# 四、增加新的一個類別(class DisplayFrame)
class DisplayFrame(tk.LabelFrame):
    def __init__(self,master,cname,ename):                                          #新增五時增加master
        super().__init__(master)
        self.cname = cname
        self.ename = ename
        print(self.cname)
        print(self.ename)        
        # tk.Button(self,text="Hello!").pack()                                        #新增六十修改為引用外部傳入參數(傳到本類別的cname)
        tk.Button(self,text=self.cname,padx=20,pady=10).pack()

def main():
    tw_county_names = {"台北":"Taipei",
                   "台中":"Taichung",
                   "基隆":"Keelung",
                   "台南":"Tainan",
                   "高雄":"Kaohsiung",
                   "新北":"New Taipei",
                   "宜蘭":"Yilan",
                   "桃園":"Taoyuan",
                   "嘉義":"Chiayi",
                   "新竹":"Hsinchu",
                   "苗栗":"Miaoli",
                   "南投":"Nantou",
                   "彰化":"Changhua",
                   "雲林":"Yunlin",
                   "屏東":"Pingtung",
                   "花蓮":"Hualien",
                   "台東":"Taitung",
                   "金門":"Kinmen",
                   "澎湖":"Penghu",
                   "連江":"Lienchiang"
                   }
    # 學習點，建立類別(class)後，需要建立實體(def)，將類別執行的成果回傳給實體
    # 使用了引數名稱的呼叫
    window = Window(codes=tw_county_names)
    window.mainloop()

if __name__ == "__main__":
    main()