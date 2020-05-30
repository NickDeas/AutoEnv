#!/usr/bin/env python

"""
	Command Line Interface for AutoEnv.
"""

import sys
import os
from envManager import EnvManager



#Constants and global variables--------------------------------

manager = EnvManager()

START_INSTR = '-------  Welcome to AutoEnv!  -------\n \
Start by using the command "autoenv newEnv  \
[name] to create a new work environment.\nThen \
use "autoenv addApp/addUrl [env name] [app address/url] \
to add an app or url to the environment for opening.'

#Command dictionary - CLI -> Method-----------------------------
commands = {
	'newEnv': 	manager.createEnv,
	'remEnv':	manager.remEnv,
	'rename':	manager.rename,
	# 'list':		manager.list,
	# 'display': 	manager.display,
	'addApp': 	manager.addApp,
	'addUrl': 	manager.addUrl,
	'remApp': 	manager.remApp,
	'remUrl': 	manager.remUrl,
	'open':	  	manager.openEnv,
}


#Success and error messages-------------------------------------
success = {
	'newEnv': 	'New environment created successfully!',
	'remEnv':	'Environment removed successfully!',
	'rename':	'Environment renamed successfully!',
	'addApp': 	'Application added to environment successfully!',
	'addUrl': 	'Url added to environment successfully!',
	'remApp': 	'Application removed from environment successfully!',
	'remUrl': 	'Url removed from environment successfully!',
	'open':	  	'Opening environment...',
}

errors = {
	'BAD_COMMAND': 		'Command not found.',
	'BAD PARAMETERS': 	'Invalid command parameters.',
}


#CLI Commands
def display(env):
		manager.loadEnv(env)
		name = manager.curEnv.name
		apps = manager.curEnv.apps
		urls = manager.curEnv.urls

		print('Environment Name: %s' % name)
		
		print('Apps: ')
		if len(apps) == 0:
			print("\tNone")
		else:
			for i, app in enumerate(apps):
				print('\t[%d]: %s' % (i, app))
		
		print('Urls: ')
		if len(urls) == 0:
			print("None")
		else:
			for i, url in enumerate(urls):
				print('\t[%d]: %s' % (i, url))

def list():
		envs = [env[:-5] for env in os.listdir('./saved-envs/')]
		for i, env in enumerate(envs):
			print('[%d]: %s' % (i, env))


#Command parser
def handleCommand(command, args):
	"""
		Take the parsed command and arguments to execute the proper
			corresponding method.
	"""

	if command == 'display':
		display(*args)
	elif command == 'list':
		list(*args)
	elif command in commands.keys():
		f = commands[command]
		if(f(*args) == 0): #Call the command based on system arguments
			if(command in success.keys()):
				print(success[command])
	else:
		print(errors['BAD_COMMAND'])


def main():
	if len(sys.argv) == 1:
		print(START_INSTR)
	else:
		command = sys.argv[1]
		args = sys.argv[2:] if len(sys.argv) > 2 else []
		handleCommand(command, args)


if __name__ == "__main__":
	main()