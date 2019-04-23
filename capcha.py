import pyautogui as pag
import time

x,y = pag.position()
pag.PAUSE = 0.5

print(x,y)
print("解像度{0}".format(pag.size()))
time.sleep(1)

icon_region = pag.locateOnScreen('youtube_bar.png')
# icon_region = pag.locateCenterOnScreen('youtube_bar.png')
# icon_region = pag.locateCenterOnScreen('youtube_bar.png', grayscale=True, region=(x, y, w, h))

print(icon_region)
if icon_region is not None:
	x,y = pag.center(icon_region)
	pag.click(x = x, y = y)
	pag.typewrite('Bon jovi my life')
	pag.press('enter')
	pag.press('enter')

	print(x,y)
else:
	print('Not found')

"""
icon_region_gene = pag.locateAllOnScreen('youtube_bar.png')
for icon_region in icon_region_gene:
	print(icon_region) # (int, int, int, int)

img_sc = pag.screenshot()
rgb = img_sc.getpixel((200, 150)) # rgb tuple

rgb = pag.pixel(200, 150) # rgb tuple

match_flg = pag.pixelMatchesColor(200, 150, rgb, tolerance = 10)
"""


