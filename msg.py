import pyautogui as pag
import time

pag.PAUSE = 0.5
time.sleep(1)

# icon_region = pag.locateOnScreen('youtube_bar.png')
icon_region = "dummy"
if icon_region is not None:
	# x,y = pag.center(icon_region)
	pag.moveTo(400, 400)
	pag.click()
	pag.typewrite('Bon jovi my life')
	pag.press('enter')
	res = pag.confirm(
		text="本当に検索してもよいですか？",
		title="確認",
		buttons=["OK", "No", "Cancell"]
		)
	if res == "OK":
		pag.press('enter')
	else:
		res = pag.alert(
		text="キャンセルされました",
		title="確認",
		button="OK"
		)
	"""
	res = pag.alert(
		text="本当に検索してもよいですか？\nDo you really want to search it?",
		title="確認",
		button="OK")
	print(res)
	"""
	print(x,y)
else:
	print('Not found')
