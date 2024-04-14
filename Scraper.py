import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import schedule
import time

# 通用格式的爬蟲
def type1_scraper(url):
    # 配置 WebDriver
    options = Options()
    options.add_argument('--disable-gpu')  # 禁用 GPU 加速
    options.add_argument('--headless')  # 無頭模式
    service = Service(executable_path='D:\chromedriver\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(5)  # 給予頁面充足的時間來加載 JavaScript

        # 使用 Selenium 的查找方法
        gym_flow = driver.find_element(By.ID, "gym_on").text or 0
        pool_flow = driver.find_element(By.ID, "swim_on").text or 0

    finally:
        driver.quit()  # 確保無論如何都能關閉瀏覽器

    return gym_flow, pool_flow

# 北投
def beitou_scraper():
    url = 'https://www.btsport.org.tw/zh-TW/onsitenum'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        gym_flow = soup.find('h3', class_='gym_flow')
        gym_current = gym_flow.find('span', class_='flow_number').text.strip()

        pool_flow = soup.find('h3', class_='swimming_flow')
        pool_current = pool_flow.find('span', class_='flow_number').text.strip()

        return gym_current, pool_current
    return 0, 0

# 士林
def shihlin_scraper():
    url = 'https://www.slsc-taipei.org/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        gym_flow = soup.find('li', id='data1')
        gym_current = gym_flow.find('span', class_='number').text or 0

        pool_flow = soup.find('li', id='data2')
        pool_current = pool_flow.find('span', class_='number').text or 0
        return gym_current, pool_current
    return 0, 0

# 內湖
def neihu_scraper():
    url = 'https://nhsc.cyc.org.tw/'
    gym_flow, pool_flow = type1_scraper(url)

    return gym_flow, pool_flow

# 南港
def nangang_scraper():
    url = 'https://ngsc.cyc.org.tw/'
    gym_flow, pool_flow = type1_scraper(url)

    return gym_flow, pool_flow

# 信義
def xinyi_scraper():
    url = 'https://api.teamxports.com/XPORTS-API'
    params = {
        'region': 'xysc',
        'action': 'z1'
    }
    gym_flow, pool_flow = 0,0
    # 游泳池
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()  # 將 JSON 響應解析為字典
        pool_flow = data.get('Now', 0)

    params['action'] = 'z2'
    # 健身房
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()  # 將 JSON 響應解析為字典
        gym_flow = data.get('Now', 0)

    return gym_flow, pool_flow

# 大同
def datong_scraper():
    url = 'https://www.dtsc-wdyg.com.tw/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        gym_current = soup.find('div', class_='pcount').find('div', class_='notice').text or 0
        pool_current =  soup.find_all('div', class_='pcount')[1].find('div', class_='notice').text or 0

        return gym_current, pool_current
# 中山
def zhongshan_scraper():
    url = 'https://cssc.cyc.org.tw/'
    gym_flow, pool_flow = type1_scraper(url)
    return gym_flow, pool_flow

# 文山
def wenshan_scraper():
    url = 'https://wssc.cyc.org.tw/'
    gym_flow, pool_flow = type1_scraper(url)
    return gym_flow, pool_flow

# 中正
def zhongzheng_scraper():
    url = 'https://www.tpejjsports.com.tw/zh-TW/onsitenum'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        gym_flow = soup.find('h3', class_='gym_flow')
        gym_current = gym_flow.find('span', class_='flow_number').text.strip()

        pool_flow = soup.find('h3', class_='swimming_flow')
        pool_current = pool_flow.find('span', class_='flow_number').text.strip()

        return gym_current, pool_current
    return 0, 0

# 大安
def daan_scraper():
    url = 'https://www.daansports.com.tw/zh_TW/onsitenum'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        gym_flow = soup.find('li', id='flow_gym')
        gym_current = gym_flow.find('span', class_='stadium-info_number').text.strip() or 0

        pool_flow = soup.find('li', id='flow_swimming')
        pool_current = pool_flow.find('span', class_='stadium-info_number').text.strip() or 0

        return gym_current, pool_current
    return 0, 0

scarper_dict = {
    1: beitou_scraper,
    2: shihlin_scraper,
    3: neihu_scraper,
    4: nangang_scraper,
    5: xinyi_scraper,
    6: datong_scraper,
    7: zhongshan_scraper,
    8: zhongzheng_scraper,
    9: daan_scraper,
    10: wenshan_scraper

}
def fetch_data():
    for id, scraper in scarper_dict.items():
        gym_current, swimming_current = scraper()
        print(f"場館：{id}")
        print(f"健身房當前人數：{gym_current}")
        print(f"游泳池當前人數：{swimming_current}")
        print("=====================================")


# def job():
#     print("Fetching data...")
#     fetch_data()
#     print("Data fetched successfully!")
#
#
# # 設定每小時整點執行 job 函數
# schedule.every().hour.at(":22").do(job)
#
# # 讓程式一直運行
# while True:
#     schedule.run_pending()
#     time.sleep(30)  # 每30秒檢查一次

fetch_data()