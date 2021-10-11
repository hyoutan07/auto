import time                  # import            
from selenium import webdriver       
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import cv2
import pyocr
import pyocr.builders
from PIL import Image
import sys
import os
path_tesseract = "C:\\Program Files\\Tesseract-OCR"
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract
import chromedriver_binary

driver = webdriver.Chrome()            
driver.get('https://www.google.com/') 

window = (800, 420+123)
driver.set_window_size(*window)

target_url = 'http://typingx0.net/sushida/play.html'
driver.get(target_url)

target_xpath = '//*[@id="game"]/div'
webgl_element = driver.find_element_by_xpath(target_xpath)
actions = ActionChains(driver)
actions.move_to_element(webgl_element).perform()

time.sleep(10)

pyautogui.moveTo(150,456)
time.sleep(1)
pyautogui.scroll(-150)
time.sleep(5)
pyautogui.moveTo(630,590)
time.sleep(1)
pyautogui.click()

pyautogui.moveTo(330,340)
time.sleep(1)
pyautogui.click()
time.sleep(1)

pyautogui.moveTo(630,590)
time.sleep(1)
pyautogui.click()

pyautogui.press("enter")

start = time.time()
while time.time() - start < 120.0:
    im = pyautogui.screenshot(region=(425, 550, 350, 43))
    im.save("hoge.png")
    img = cv2.imread('hoge.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invgray = cv2.bitwise_not(gray)
    cv2.imwrite("hoge.png", invgray)

    img_before = Image.open('hoge.png')
    img_after = img_before.resize((1200,150))
    img_after.save('hoge.png')

    tools = pyocr.get_available_tools()
    tool = tools[0]
        
    img_org = Image.open("hoge.png")
    builder = pyocr.builders.TextBuilder(tesseract_layout=4)
    result = tool.image_to_string(img_org, lang="eng", builder=builder)
        
    pyautogui.write(result,interval = 0.02)

input('何か入力してください')
    
driver.close()
driver.quit()

a = 1