import sys
import os
import hashlib


def DirTreeWalk(params):

    if len(params) == 2:
        if params[1] == "-h" or params[1] == "--help":
            helpfunc()
        else:
            startdir = params[1]
            if os.path.exists(startdir) and os.path.isdir(startdir):
                treewalk(startdir)
            else:
                print("Error: Path not found: " + startdir + "!")
                exit(1)
    else:
        helpfunc()

def hashit(directory):
        with open(directory) as new_file:
            file_content = new_file.read()
            return hashlib.md5(str(file_content).encode('utf-8')).hexdigest()


def treewalk(startdir):
    try:
        for i in os.listdir(startdir):
            directory = startdir + "\\" + i
            if os.path.isdir(directory):
                print("{:30}".format(i) + "{:40}".format("<dir>") + os.path.abspath(directory))
                treewalk(directory)
            else:
                md5_sum = hashit(directory)
                print("{:30}".format(i) + "{:40}".format(str(md5_sum)) + os.path.abspath(directory))
    except:
        print("Error:", sys.exc_info()[0])

def helpfunc():
    print("usage: DirTreeWalk.py [-h] path")
    exit(1)


DirTreeWalk(list(sys.argv))

