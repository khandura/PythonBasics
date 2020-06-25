import shutil
import os

basedir = "E:\\workspaces\\dir1\\"
copydir = "E:\\workspaces\\dir2\\"

print(basedir)
print(copydir)

os.curdir = basedir

print("current directory is : "+os.curdir)

shutil.copy2("file1.txt", copydir)