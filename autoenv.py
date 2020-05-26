#!/usr/bin/env python
import sys
from envManager import EnvManager

START_INSTR = '-------  Welcome to AutoEnv!  -------\n \
Start by using the command "autoenv newEnv  \
[name] to create a new work environment.\nThen \
use "autoenv addApp/addUrl [env name] [app address/url] \
to add an app or url to the environment for opening.'


manager = EnvManager()

# commands = {
# 	'newEnv': manager.createEnv,
# 	'addApp': manager.addApp,
# 	'addUrl': manager.addUrl,
# 	'remApp': manager.removeApp,
# 	'remUrl': manager.removeUrl,
# }

def handleCommand(command, args):
	return

if __name__ == "__main__":

	# Argument validation
	if len(sys.argv) == 1:
		print(START_INSTR)
	else:
		command = sys.argv
		args = sys.argv[2:] if len(sys.argv) > 2 else []
		handleCommand(command, args)


