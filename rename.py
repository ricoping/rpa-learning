import pyautogui as pag

pag.PAUSE = 0.5
pag.rightClick(x=300, y=400)

pag.typewrite('m')
pag.typewrite('新しいファイル')

pag.press('enter')
