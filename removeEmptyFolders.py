"""
This script removes all empty folders in the directory it's placed in and all subdirectories below it.

A folder is considered empty if it has no files and no directories.
"""

# Imports
import os

# Get current folder
currentFolder = os.getcwd()

# Each pass may create new empty folders. Run until none are found.
clean = False
while not clean:
	clean = True

	# Depth-first search. Remove all empty folders.
	for dirpath, dirnames, filenames in os.walk(currentFolder):
		# A folder is empty if the list of directories and the list of filenames are both empty.
		if dirnames == [] and filenames == []:
			os.rmdir(dirpath)
			clean = False