Linter
=========

JsonLint challenge. 
1. Create a program/script that given a directory containing JSON files will recursively descend into the directory and lint every file in all subdirectories
2. The program should print the name of the file that failed linting and also print the lines that failed the test.
3. The program should accept a single argument named "jsoninput". the argument should accept a single string of the form '{\"path\":\"/home/harish/jsons\"}'
4. The program should extract the supplied path from the above string and use that as the input.

## Dependencies

Python must be installed and on the PATH.  Install [Python](https://www.python.org/)

Node.js must be installed and on the PATH. Install [Node.js](https://nodejs.org/)

[JSON Lint](http://zaach.github.com/jsonlint/) must be installed.  Install jsonlint with npm to use the command line interface:

    npm install jsonlint -g

## Command line interface
	
	python linter --jsoninput '{\"path\":\"../test\"}"





