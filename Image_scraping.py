import bs4, requests, os

url = 'http://www.grandtech.info/'                  # 上奇資訊網頁
html = requests.get(url)
print("網頁下載中 ...")
html.raise_for_status()                             # 驗證網頁是否下載成功                      
print("網頁下載完成")

destDir = 'out21_25'                                # 設定未來儲存圖片的資料夾
if os.path.exists(destDir) == False:
    os.mkdir(destDir)                               # 建立資料夾供未來儲存圖片

objSoup = bs4.BeautifulSoup(html.text, 'lxml')      # 建立BeautifulSoup物件

imgTag = objSoup.select('img')                      # 搜尋所有圖片檔案
print("搜尋到的圖片數量 = ", len(imgTag))           # 列出搜尋到的圖片數量
if len(imgTag) > 0:                                 # 如果有找到圖片則執行下載與儲存
    for i in range(len(imgTag)):                    # 迴圈下載圖片與儲存
        imgUrl = imgTag[i].get('src')               # 取得圖片的路徑
        print("%s 圖片下載中 ... " % imgUrl)
        finUrl = url + imgUrl                       # 取得圖片在Internet上的路徑
        print("%s 圖片下載中 ... " % finUrl)
        picture = requests.get(finUrl)              # 下載圖片
        picture.raise_for_status()                  # 驗證圖片是否下載成功
        print("%s 圖片下載成功" % finUrl)

        # 先開啟檔案, 再儲存圖片
        pictFile = open(os.path.join(destDir, os.path.basename(imgUrl)), 'wb')
        for diskStorage in picture.iter_content(10240):
            pictFile.write(diskStorage)
        pictFile.close()                            # 關閉檔案