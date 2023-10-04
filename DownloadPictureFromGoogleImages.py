#---下載Google圖片
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def surfGooglePicture(driver,xpath,save_path):
    
    #---處理例外狀況
    try:
        #---設定headers，headers可以在Google搜尋what is my user agnet獲得
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'}

        #---將瀏覽器視窗設定為最大化
        #driver.maximize_window()

        #---將瀏覽器滑到網頁底端，加入這行可讓Google圖片下方隱藏的圖片繼續出現
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

        #---找到第一個圖片的連結
        c1 = driver.find_element(By.XPATH, xpath) # 

        #---建立ActionChains
        actions = ActionChains(driver)

        #---對連結按一下，加入這個動作是因為在Google圖片要使用按一下才會出現大圖的連結
        actions.click(c1).perform()

        #---取得大圖的連結
        c1_link = c1.get_attribute('href')

        #---從連結取出jpg等圖片的連結
        if c1_link.find('jpg') != -1: c1_link = c1_link.split('imgurl=')[1].split('jpg')[0]+'jpg' # 格式整理
        elif c1_link.find('png') != -1: c1_link = c1_link.split('imgurl=')[1].split('png')[0]+'png' # 格式整理
        elif c1_link.find('jpeg') != -1: c1_link = c1_link.split('imgurl=')[1].split('jpeg')[0]+'jpeg' # 格式整理
        elif c1_link.find('&tbnid') != -1: c1_link = c1_link.split('imgurl=')[1].split('&tbnid')[0] # 格式整理

        #---印出目前的連結
        print('old_link:',c1_link)

        #---對連結做16進制轉ASCII轉換
        #---將目前的連結用'%'分隔成一個一個元素
        a = c1_link.split('%')

        #---初始化一個新的連結
        new_url = ''

        #---對每個元素做ASCII轉換
        for i in a:

            #---如果元素的長度超過2
            if len(i) > 2:
                try:
                    #---將元素前2個字元做ASCII轉換，後面不變
                    i1 = bytearray.fromhex(i[:2]).decode()
                    i2 = i[2:]
                    output = i1 + i2
                except:output = i
            else:
                #---對2個字元做ASCII轉換
                try:output = bytearray.fromhex(i).decode()
                except:output = i

            #---重新合成新的連結
            new_url = new_url + output

        #---印出新的連結
        print('new_link:',new_url)


        #---排除掉lookaside連結，這些連結無法儲存圖片，這類型的連結包含FB和IG
        if new_url.find('lookaside') == -1:

            #---下載圖片
            img = requests.get(new_url, headers=headers, timeout=4) 

            #---如果回傳碼正確
            if img.status_code == 200:

                #---寫入圖片的二進位碼，將圖片儲存在save_path
                with open(rf"{save_path}", "wb") as file: file.write(img.content) 

            #---如果回傳失敗，印出失敗碼
            else:print('status code is ',img.status_code, 'Fail')

        #---如果連結帶有lookasode，印出無法下載
        else:print('圖片網址帶有lookaside，無法下載')

    #---發現例外狀況，印出錯誤訊息
    except Exception as e:
        print(str(e))
        pass

#---程式開始---

#---貼上Google圖片搜尋的網址
url = str(input('請貼上要下載的Google圖片網址，或是要搜尋的內容: '))

#---貼上圖片下載的路徑，如果不輸入會使用預設的資料夾
save_path = str(input('請貼上要下載的資料夾路徑: ')) or 'C:/Users/This PC/Pictures/Saved Pictures'

#---隱藏視窗
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#---啟動chromedriver，這個動作會開啟一個新的chrome瀏覽器
driver = webdriver.Chrome('chromedriver',options=options)

#---檢查url，如果貼上的不是網址(沒有找到https)
if url.find('https:') == -1:
    driver.get('https://www.google.com.tw/imghp')
    text = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
    sumit = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button')
    actions = ActionChains(driver)
    actions.send_keys_to_element(text,url).send_keys_to_element(sumit,Keys.ENTER).send_keys_to_element(sumit,Keys.ENTER).perform()
    
else:driver.get(url)

#---開始下載第一種類型的XPATH
for i in range(1,101):
    print('i=',i)
    xpath = f"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{i}]/a[1]"
    surfGooglePicture(driver,xpath,f'{save_path}/pic_{i}.jpg')

#---開始下載第二種類型的XPATH
for j in range(51,101):
    for i in range(1,101):
        print('j=',j,' i=',i)
        xpath = f"/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[{j}]/div[{i}]/a[1]"
        surfGooglePicture(driver,xpath,f'{save_path}/pic_{j}_{i}.jpg')

#driver.close()
