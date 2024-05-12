from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def poster():
    email = "khaimovedan1901@gmail.com"
    password = "iiRhzxyhenEd"
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.satirikon.ru/lichnyj-kabinet/avtorizaciya/")
        driver.maximize_window()
        sleep(0.5)
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/div[2]/div/main/div/div/div/div/div[1]/div/form/div[1]/input").send_keys(
            email)
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/div[2]/div/main/div/div/div/div/div[1]/div/form/div[2]/input").send_keys(
            password)
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/div[2]/div/main/div/div/div/div/div[1]/div/form/button/span[1]").click()
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/header/div/a[1]/span[1]").click()
        sleep(0.25)
        driver.execute_script('window.scrollTo(0, 450)')
        sleep(0.5)
        driver.save_screenshot("choice.png")
    except Exception as ex:
        print(ex)
        return 0
    finally:
        driver.close()
        driver.quit()


def first_event():
    email = "khaimovedan1901@gmail.com"
    password = "iiRhzxyhenEd"
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.satirikon.ru/lichnyj-kabinet/avtorizaciya/")
        driver.maximize_window()
        sleep(0.5)
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/div[2]/div/main/div/div/div/div/div[1]/div/form/div[1]/input").send_keys(
            email)
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/div[2]/div/main/div/div/div/div/div[1]/div/form/div[2]/input").send_keys(
            password)
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/div[2]/div/main/div/div/div/div/div[1]/div/form/button/span[1]").click()
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/header/div/a[1]/span[1]").click()
        sleep(0.25)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div[2]/div/main/div/section/div/div[2]/div[1]/div/button/span[1]').click()
        sleep(5)
        driver.save_screenshot("first.png")
    except Exception as ex:
        print(ex)
        return 0
    finally:
        driver.close()
        driver.quit()


def second_event():
    email = "khaimovedan1901@gmail.com"
    password = "iiRhzxyhenEd"
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.satirikon.ru/lichnyj-kabinet/avtorizaciya/")
        driver.maximize_window()
        sleep(0.5)
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/div[2]/div/main/div/div/div/div/div[1]/div/form/div[1]/input").send_keys(
            email)
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/div[2]/div/main/div/div/div/div/div[1]/div/form/div[2]/input").send_keys(
            password)
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/div/div[2]/div/main/div/div/div/div/div[1]/div/form/button/span[1]").click()
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/header/div/a[1]/span[1]").click()
        sleep(0.25)
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div/div[2]/div/main/div/section/div/div[2]/div[2]/div/button/span[1]').click()
        sleep(5)
        driver.save_screenshot("second.png")
    except Exception as ex:
        print(ex)
        return 0
    finally:
        driver.close()
        driver.quit()
