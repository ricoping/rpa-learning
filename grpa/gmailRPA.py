import pyautogui as pag
import time

class GmailRPA():
	def __init__(self):
		pag.PAUSE = 1.0
		time.sleep(1)
		self.W,self.H = pag.size()
		print("解像度{0}".format(pag.size()))

	def open_inboxes(self):
		star_regions = pag.locateAllOnScreen('star_not_read.png')

		for region in star_regions:
			print(region)
			x,y = pag.center(region)
			pag.moveTo((x + 100, y))
			pag.click()

			time.sleep(2)

			self.copy_body()

			self.switch_left()

			self.paste_excel()

			self.switch_right()

			self.browser_back()

	def copy_body(self):
		trash = pag.locateOnScreen('trash.png')

		if trash is not None:
			x,y = pag.center(trash)
			pag.click(x = x, y = y + 60, clicks=3)
			pag.hotkey('ctrl', 'c')
			print(x,y)
		else:
			print('Not found')


	def switch_left(self):
		x = self.W / 4
		pag.click((x, 15))

	def switch_right(self):
		x = self.W / 4
		pag.click((self.W / 2 + x, 15))

	def paste_excel(self):
		pag.hotkey('shift', 'ctrl', 'v')
		pag.press('down')

	def browser_back(self):
		pag.hotkey('alt', 'left')


if __name__ == '__main__':
	grpa = GmailRPA()
	grpa.open_inboxes()
