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


def get_user_agent(driver):
    user_agent = driver.execute_script('return navigator.userAgent')
    print(user_agent)
