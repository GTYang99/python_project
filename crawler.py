# 加載urllib.request套件，作為抓取網站內容用
import urllib.request as req
# 加載Beautifulsoup4套件，作為解析網站內容用
import bs4

# 設定一個變數儲存網址
url = 'https://111declaration.cec.gov.tw'
# 設定一個變數
request = req.Request(url,headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.65'
})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')
# print(data)
root = bs4.BeautifulSoup(data,'html.parser')
diva = root.find_all('a')
# print(diva)
for i in diva:
    if len(i.string) >= 3:
        print(i.string)