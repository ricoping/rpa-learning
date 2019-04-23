import pyautogui as pag

pag.PAUSE = 2.5

pag.moveTo((300, 400))

pag.click()

pag.hotkey('ctrl', 'c')
pag.hotkey('ctrl', 'v')

"""
pag.keyDown('ctrl')
pag.press('c')
pag.keyUp('ctrl')

pag.keyDown('ctrl')
pag.press('v')
pag.keyUp('ctrl')
"""





