import os
import json
from environment import Environment

class EnvManager():


	def __init__(self):
		self.curEnv = None

	def loadEnv(self, name):
		self.curEnv = Environment().load('./saved-envs/%s.json' % name)

	def createEnv(self, name):
		newEnv = Environment(name)
		newEnv.save()

		print('New environment %s created successfully!' % name)

	def addApp(self, env, appAddr):
		loadEnv(env)
		self.curEnv.addApp(appAddr)

		print('New application successfully added to %s!' % env)
