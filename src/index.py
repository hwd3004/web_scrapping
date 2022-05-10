import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from custom_util.index import cc


def init():
    try:
        executable_path = ChromeDriverManager().install()
        # executable_path = '/usr/src/chrome/chromedriver'
        cc("executable_path", executable_path)
        service = ChromeService(executable_path)
        cc("service", service)

        url = ["http://naver.com", "https://www.kogl.or.kr/recommend/recommendDivView.do?recommendIdx=39741&division=img",
               "http://192.168.56.1:5500/220420/work/main.html"]

        options = webdriver.ChromeOptions()

        cc("options", options)

        options.add_argument('--window-size=1920,1080')
        # options.add_argument('--start-maximized')
        options.add_argument('headless')
        options.add_argument("--disable-gpu")
        options.add_argument('incognito')  # 시크릿 모드

        # headless를 제거한 값이 필요
        options.add_argument(
            "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36")
        options.add_argument("Accept-Language=ko-KR,ko")

        options.add_argument('--no-sandbox')

        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(service=service, options=options)

        driver.get(url[2])

        # 접속하는데 걸리는 시간이 있을 수 있으므로 시간 대기
        time.sleep(3)

        html = driver.page_source
        print(html)

        # while True:
        #     pass
    except Exception as e:
        print("ERROR ERROR ERROR")
        print(e)
    finally:
        print("finally")
        driver.quit()


init()
