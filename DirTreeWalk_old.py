# -*- coding: utf-8 -*-

import sys
import os
import hashlib


def dirTreeWalk(params):

    if len(params) == 2:
        if params[1] == "-h" or params[1] == "--help":
            helpfunc()
        else:
            startdir = params[1]
            if os.path.exists(startdir) and os.path.isdir(startdir):
                treeWalk(startdir)
            else:
                print("Error: Path not found: " + startdir + "!")
                exit()
    else:
        helpfunc()


def hashIt(directory):
        with open(directory, "rb") as new_file:
            file_content = bytearray(new_file.read())
            return hashlib.md5(str(file_content).encode('utf-8')).hexdigest()


def treeWalk(startdir):
    try:
        for i in os.listdir(startdir):
            directory = startdir + "\\" + i
            if os.path.isdir(directory):
                print("{:85}".format(i) + "{:35}".format("<dir>"))
                treeWalk(directory)
            else:
                md5_sum = hashIt(directory)
                print("{:50}".format(i) + "{:35}".format(str(md5_sum)) + os.path.abspath(directory))
    except:
        print("Error: ", sys.exc_info()[0])


def helpfunc():
    print("usage: DirTreeWalk.py [-h] path")
    exit()


dirTreeWalk(list(sys.argv))

