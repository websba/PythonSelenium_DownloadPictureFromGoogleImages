# PythonSelenium_DownloadPictureFromGoogleImages

這個Python程式可以用來下載Google圖片裡面所搜尋到的圖片

比如我在Google圖片搜尋: 可愛貓貓

這個程式可以將搜尋結果的圖片，而且是來源圖片，非縮圖，下載到電腦

執行程式之後只需輸入2個參數

參數1_先輸入: '想搜尋的內容' 或是 '貼上Google圖片搜尋結果的網址'

參數2_再輸入: 圖片想放置的路徑

輸入完後，圖片便會自動開始下載

# 環境設置

記得下載 chromedriver.exe，這個要跟Python程式 (DownloadPictureFromGoogleImages.py) 放在同一個資料夾

比如在桌面新增一個資料夾叫123，將chromedriver.exe和 DownloadPictureFromGoogleImages.py 放進去

# 可以使用bat打開python

新增一個bat檔，取名叫 DownloadPictureFromGoogleImages.bat

bat檔裡面寫一行:
python C:\Users\This PC\Desktop\123\DownloadPictureFromGoogleImages.py

之後只要點兩下bat後，就可以執行了

# 如果遇到不能使用的狀況

1. chromedriver版本錯誤，要到chrome瀏覽器檢查版本，比如到chrome://settings/help 可以看到目前使用的是117.版本

![image](https://github.com/websba/PythonSelenium_DownloadPictureFromGoogleImages/assets/134906281/32ae2816-7920-4e9d-a4d7-ab68acd2c3e1)

2. xpath錯誤導致圖片無法取得，這個就需要自行修改xpath的程式碼，有兩處:

xpath = f"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{i}]/a[1]"

xpath = f"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{j}]/div[{i}]/a[1]"
