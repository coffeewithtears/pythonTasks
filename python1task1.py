#!/usr/bin/python

import os

directory = "photos"
parent_directory = "C:\\Users\\user\\OneDrive\\"
path = os.path.join(parent_directory, directory)
os.mkdir(path)
print ("Directory '%s' created" % directory)


