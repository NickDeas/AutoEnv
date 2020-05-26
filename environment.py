import os
import json

class Environment():


	def __init__(self, name = ''):

		self.name = name

		self.apps = []
		self.urls = []


	def load(self, saveDataLoc: str):
		with open(saveDataLoc) as sdJson:
			data = json.load(sdJson)

		self.apps = data['apps']
		self.urls = data['urls']

	def save(self):
		saveData = {'name': self.name, 'apps': self.apps, 
			'urls': self.urls}

		with open('./saved-envs/%s' % (self.name + '.json')):
			json.dumps(saveData)



	#Editing methods

	def addApp(self, appAddr:str):
		self.apps.append(appAddr)

	def addUrl(self, url:str):
		self.urls.append(url)

	def removeApp(self, index:int):
		self.apps.pop(index)

	def removeUrl(self, index:int):
		self.urls.pop(index)


	#Open environment

	def open(self):
		self.openApps()
		self.openUrls()

	def openApps(self):
		for app in self.apps:
			try:
				os.startfile(app)
			except Exception as e:
				print(type(e))
				print(e.args)
				print(e)

	def openUrls(self):
		if len(self.urls) > 0:
			webbrowser.register( 'chrome',
				None,
				webbrowser.BackgroundBrowser('C://Program Files (x86)//Google//Chrome//Application//chrome.exe')
			)

			for url in self.urls:
				webbrowser.get('chrome').open(url)