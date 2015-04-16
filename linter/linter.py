##linter.py

import argparse
import json
import logging
import os
import subprocess
import sys

def lint(file):
	cmd = "jsonlint " + file + " -q"
	logging.debug(cmd)
	stdoutdata = subprocess.getoutput(cmd)
	if stdoutdata:
		msg = "File : " + file
		print(msg)
		logging.debug(msg)
		print(stdoutdata)
		logging.debug(stdoutdata)
		print()


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='linter.log',level=logging.INFO)

parser = argparse.ArgumentParser()

parser.add_argument("-jsoninput", "--jsoninput", help="Recursively descend into directory and lint every file in all subdirectories.", type=str, required=True)

args = parser.parse_args()

j = json.loads(str(args.jsoninput))
walk_dir = j['path']

logging.debug(walk_dir)

if os.path.isdir(walk_dir) == False:
	msg = walk_dir + " is not directory"
	logging.error(msg)
	print(msg)
	exit()
if os.path.exists(walk_dir) == False:
	msg = walk_dir = " does not exist"
	logging.error(msg)
	print(msg)
	exit()

for root, dirs, files in os.walk(walk_dir):
    for file in files:
        lint(os.path.join(root, file))

