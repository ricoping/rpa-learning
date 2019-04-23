import pyautogui as pag

pag.PAUSE = 2.5

for i in range(10):
	img_sc = pag.screenshot(
		'images/img_sc_%s.jpg' % str(i), 
		region = (300, 300, 500, 400) # x,y,w,h
		)
	img_sc.save(
		'images/img_sc_%s.jpg' % str(i),
		quality = 10)

#img_sc_crop = img_sc.crop(300, 300, 800, 700)
#img__sc.save('fdaf.jpg', quality=100)