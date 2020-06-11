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

	def listEnvs(self):
		envs = [env_name[:-5] for env_name in os.listdir('./saved-envs/')]
		return envs

	def loadEnv(self, name):
		self.curEnv = Environment()
		self.curEnv.load('./saved-envs/%s.json' % name)

	def createEnv(self, name):
		newEnv = Environment(name)
		newEnv.save()

		return 0

	def rename(self, env, new_name):
		self.loadEnv(env)
		self.curEnv.rename(new_name)

		return 0

	def remEnv(self, name):
		os.remove('./saved-envs/%s.json' % name)

		return 0

	def addApp(self, env, appAddr):
		self.loadEnv(env)
		self.curEnv.addApp(appAddr)
		self.curEnv.save()

		return 0

	def addUrl(self, env, url):
		self.loadEnv(env)
		self.curEnv.addUrl(url)
		self.curEnv.save()

		return 0

	def remApp(self, env, appI):
		self.loadEnv(env)
		app = self.curEnv.apps[appI]
		self.curEnv.removeApp(appI)

		return 0

	def remUrl(self, env, urlI):
		self.loadEnv(env)
		url = self.curEnv.urls[urlI]
		self.curEnv.removeUrl(urlI)

		return 0

	def openEnv(self, env):
		self.loadEnv(env)
		self.curEnv.open()

		return 0
