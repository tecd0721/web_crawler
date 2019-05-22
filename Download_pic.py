import requests

def download_pic(url, path):
    pic = requests.get(url)          #Get讀取網頁_使用 GET 對圖片連結發出請求
    path += url[url.rfind('.'):]     #取檔案名稱_'.'之後做切片
    f = open(path, 'wb')             #創建檔案_以指定的路徑建立檔案
    f.write(pic.content)             #寫入圖片內容屬性到檔案
    f.close()                        #關閉檔案

# 貼上src屬性中的路徑
url = "https://ichef.bbci.co.uk/news/624/cpsprodpb/EC63/production/_104451506_kiwivictoire.jpg" 
pic_path = "download"                #設定圖片的儲存名稱和路徑
download_pic(url, pic_path)
