import os
import json
from environment import Environment

class EnvManager():


	def __init__(self):
		self.curEnv = None

	def loadEnv(self, name):
		self.curEnv = Environment()
		self.curEnv.load('./saved-envs/%s.json' % name)

	def createEnv(self, name):
		newEnv = Environment(name)
		newEnv.save()

		print('New environment %s created successfully!' % name)

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

		print('New application successfully added to %s!' % env)

	def addUrl(self, env, url):
		self.loadEnv(env)
		self.curEnv.addUrl(url)
		self.curEnv.save()

		print('New url successfully added to %s!' % env)

	def openEnv(self, env):
		self.loadEnv(env)
		self.curEnv.open()

		print('Opening environment %s...' % env)
