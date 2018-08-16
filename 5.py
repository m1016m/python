from selenium import webdriver
 


chrome_path = "./chromedriver" #chromedriver.exe執行檔所存在的路徑
web = webdriver.Chrome(chrome_path)
web.get('http://www.baidu.com/')
def get():
    conf, engine = Connect('conf.yaml')  # 獲取配置文檔的內容
    loginname = conf.get('loginname')
    password = conf.get('password')

    loginname = list(loginname.values())
    password = list(password.values())
    with open('cookies.pkl', 'wb') as f:
        for i in range(len(password)):  # 將每個賬號的cookies保存下來.
            try:
                driver = webdriver.Chrome()
                driver.set_window_size(1124, 850)  # 防止得到的WebElement的狀態is_displayed為False，即不可見
                driver.get("http://www.weibo.com/login.php")
                time.sleep(5)
                #自動點擊並輸入用户名
                driver.find_element_by_xpath('//*[@id="loginname"]').clear()
                driver.find_element_by_xpath('//*[@id="loginname"]').send_keys(loginname[i])
                driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').clear()

                time.sleep(2)
                #自動點擊並輸入登錄的密碼
                driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(
                    password[i])
                driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    
                #輸入驗證碼
                driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input').send_keys(
                    input("輸入驗證碼： "))

                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
            except Exception as e:
                print("驗證碼輸入錯誤,請重新輸入!")
                driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input').send_keys(
                    input("輸入驗證碼： "))
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
            cookies = driver.get_cookies()
            pickle.dump(cookies, f)#串行化cookies對象
def execute_times(driver):
    dynamic = []
    T = []
    d = re.compile(r'og"><div class="weibo-text">(.*?)<', re.S)  # 匹配動態
    t = re.compile(r'<span class="time">(.*?)<', re.S)  # 匹配動態發佈時間
 
 #返回滾動高度
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 滑動一次
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 等待加載
        time.sleep(random.random())

        # 計算新的滾動高度並與上一個滾動高度進行比較
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    html = driver.page_source

    dynamic += re.findall(d, html)
    T += re.findall(t, html)
    return dynamic, T #返回用户所有動態信息和動態發佈時間列表
opt = webdriver.ChromeOptions()  # 創建chrome參數對象
opt.set_headless()  # 把chrome設置成無頭模式，不論windows還是linux都可以，自動適配對應參數
driver = webdriver.Chrome(options=opt)#不制定options選項則是普通有頭瀏覽器