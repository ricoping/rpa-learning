import time
import os
import pyautogui as pag
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

options = Options()

exe_path = os.path.abspath(
	os.path.join(os.path.dirname(__file__),
	"geckodriver.exe")
)

browser = webdriver.Firefox(
	executable_path = exe_path, 
	firefox_options=options
)

pag.PAUSE = 0.5
time.sleep(1)

res = pag.prompt(
		text = "キーワードを入力してください",
		title = "Google 画像検索",
		default = "チワワ"
	)
# pag.password(
# text="", title="", default="", mask="*"
# )
url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiAmOrekeThAhV3yYsBHTtAD2QQ_AUIDygC&biw=1187&bih=752" % res

browser.get(url)
source = browser.page_source