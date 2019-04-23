import pyautogui as pag

x,y = pag.position()

print(x,y)
print("解像度{0}".format(pag.size()))

pag.PAUSE = 2.5
pag.FAILSAFE = True

x,y = (300, 400)

pag.moveTo(x, y)

# pag.moveTo(500, 500, 1, pag.easeInQuad)
# pag.moveTo(700, 700, 1, pag.easeOutQuad) #easeInOutQuad
# pag.moveTo(900, 900, 1, pag.easeInQuad)
# pag.moveTo(1300, None, 5, pag.easeInBounce) #easeInElastic

print("最小時間 : %s" % str(pag.MINIMUM_DURATION))

"""
for i in range(10):
	if i % 2:
		pag.moveRel(50, 50, 1)
	else:
		pag.moveRel(50, -50, 1)
"""

#pag.dragTo(300, 450, 2)

# pag.click(clicks=2)
# pag.doubleClick()
# pag.click(x=300, y=300, clicks=3, interval=0.7)
# pag.tripleClick(x=300, y=300, interval=0.7, button="right")
# pag.rightClick(x=300, y=300)
# pag.click()


# pag.mouseDown()
# pag.moveRel(200, 200, 3)
# pag.mouseUp()
# pag.mouseDown(x=400, y=300)
# pag.mouseUp(x=400, y=300)

# pag.scroll(1000)





