import os
import json
from environment import Environment

class EnvManager():
	"""
		Manages the creation, deletion, and modification of environments
			saved by the user.
	"""

	def __init__(self):
		self.curEnv = None

	def loadEnv(self, name):
		self.curEnv = Environment()
		self.curEnv.load('./saved-envs/%s.json' % name)

	def createEnv(self, name):
		newEnv = Environment(name)
		newEnv.save()

	def rename(self, env, new_name):
		self.loadEnv(env)
		self.curEnv.rename(new_name)

	def remEnv(self, name):
		os.remove('./saved-envs/%s.json' % name)

	def list(self):
		envs = [env[:-5] for env in os.listdir('./saved-envs/')]
		for i, env in enumerate(envs):
			print('[%d]: %s' % (i, env))

	def display(self, env):
		self.loadEnv(env)
		name = self.curEnv.name
		apps = self.curEnv.apps
		urls = self.curEnv.urls

		print('Environment Name: %s' % name)
		print('Apps: ')
		for i, app in enumerate(apps):
			print('\t[%d]: %s' % (i, app))
		print('Urls: ')
		for i, url in enumerate(urls):
			print('\t[%d]: %s' % (i, url))

	def addApp(self, env, appAddr):
		self.loadEnv(env)
		self.curEnv.addApp(appAddr)
		self.curEnv.save()

	def addUrl(self, env, url):
		self.loadEnv(env)
		self.curEnv.addUrl(url)
		self.curEnv.save()

	def remApp(self, env, appI):
		self.loadEnv(env)
		app = self.curEnv.apps[appI]
		self.curEnv.removeApp(appI)

	def remUrl(self, env, urlI):
		self.loadEnv(env)
		url = self.curEnv.urls[urlI]
		self.curEnv.removeUrl(urlI)

	def openEnv(self, env):
		self.loadEnv(env)
		self.curEnv.open()
