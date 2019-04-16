from selenium import webdriver

class Provider(object):
	
	def __init__(self, browser):
		self.browser = browser
	
	def quit(self):
		self.browser.quit()
	
	def scrollToDown(self):
		self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")