from selenium import webdriver
from PIL import Image
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# setup google maps
driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/@50.8620482,20.6071062,3a,75y,354.2h,87.38t/data=!3m6!1e1!3m4!1sozNZo85s2nfXWZUdi-PKCw!2e0!7i13312!8i6656?hl=pl")
driver.find_element_by_xpath(
    "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div").click()
time.sleep(2)
driver.execute_script(
    "document.getElementsByClassName('widget-titlecard')[0].style.display = 'none';")
driver.execute_script(
    "document.getElementsByClassName('app-horizontal-widget-holder')[0].style.display = 'none';")
driver.execute_script(
    "document.getElementById('minimap').style.display = 'none';")
driver.execute_script(
    "document.getElementsByClassName('scene-footer-container')[0].style.display = 'none';")
driver.execute_script(
    "document.getElementById('image-header').style.display = 'none';")
driver.execute_script(
    "document.getElementsByClassName('Q5q7Ge-compass-suEOdc-V67aGc-sM5MNb')[0].style.display = 'none';")
driver.execute_script(
    "document.getElementById('snackbar').style.display = 'none';")

# obrót ludka i screenshot


def walk(iterator):
    for x in range(iterator):
        driver.save_screenshot("ss1x=%x.png" % (x))
        screenshot = Image.open("ss1x=%x.png" % (x))
        # screenshot.show()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div[9]/div[22]/div[1]/div[2]/div[3]/div/button[2]").click()  # obrót w prawo
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[3]/div[9]/div[22]/div[1]/div[2]/div[3]/div/button[2]").click()  # obrót o 180 stopni
        time.sleep(1)
        driver.save_screenshot("ss2x=%x.png" % (x))
        screenshot = Image.open("ss2x=%x.png" % (x))
        # screenshot.show()
        driver.find_element_by_xpath(
            "/html/body/div[3]/div[9]/div[22]/div[1]/div[2]/div[3]/div/button[1]").click()  # obrót w lewo
        time.sleep(1)

        # ruch do przodu
        el = driver.find_element_by_xpath(
            "/html/body").click()
        actions = ActionChains(driver)
        actions.context_click(el)
        print(driver.current_url)
        actions.send_keys(Keys.ARROW_UP)
        actions.perform()
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[3]/div[9]/div[22]/div[1]/div[2]/div[3]/div/button[1]").click()  # obrót w lewo
        time.sleep(1)


walk(100)
