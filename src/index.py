import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


def cc(name: str, data):
    try:
        print("=============================================================")
        print(name)
        print("-------------------------------------------------------------")
        print(data)
        print("=============================================================")
    except Exception as e:
        print("def cc error")
        print(e)


try:
    executable_path = ChromeDriverManager().install()
    service = ChromeService(executable_path)

    url = ["http://naver.com", "https://www.kogl.or.kr/recommend/recommendDivView.do?recommendIdx=39741&division=img",
           "http://192.168.56.1:5500/220420/work/main.html"]

    options = webdriver.ChromeOptions()

    options.add_argument('--window-size=1920,1080')
    options.add_argument('--start-maximized')
    options.add_argument('headless')
    options.add_argument('incognito')  # 시크릿 모드

    driver = webdriver.Chrome(service=service, options=options)

    headers = {
        "User-Agent": driver.execute_script('return navigator.userAgent'),
        "Accept-Language": "ko-KR,ko"
    }

    driver.get(url[2])

    # 접속하는데 걸리는 시간이 있을 수 있으므로 시간 대기
    time.sleep(3)

    # html = driver.page_source
    # print(html)


except Exception as e:
    print(e)
finally:
    print("finally")
    # driver.quit()
