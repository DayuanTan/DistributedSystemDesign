import os
import shutil
import time


srcfilepath = os.path.join("172.16.193.129","home","dayuan","forGithubRepo","Proj2_DS_Design","byzantinFT","transactionLog.txt")
oldMtime = time.ctime(os.stat(srcfilepath).st_mtime)

desfielpath = os.path.join("172.16.193.128","home","dayuan","forGithubRepo","Proj2_DS_Design","byzantinFT","transactionLog.txt")


def fileCopy():
    if (os.path.exists(srcfilepath) )  :
        print("Begin")
        shutil.copyfile(srcfilepath, desfielpath)
        if os.path.exists(desfielpath):
            print("Copy operation success!")
        mtime1 = time.ctime(os.stat(srcfilepath).st_mtime)
        mtime2 = time.ctime(os.stat(desfielpath).st_mtime)
        print("Last modify time of {0} is: ".format(mtime1))
        print("Last modify time of {0} is: ".format(mtime2))
        if mtime1 < mtime2:
            print("Good job!")

if __name__ == "__main__":
    if (os.path.exists(srcfilepath) )  :
        mtime = time.ctime(os.stat(srcfilepath).st_mtime)
        if mtime > oldMtime:
            fileCopy()
    
