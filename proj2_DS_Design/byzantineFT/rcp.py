import os
import shutil
import time


# path = os.path.join(part1,part2)

filename = "transactionLog.txt"
oldMtime = time.ctime(os.stat(filename).st_mtime)

def fileCopy():
    if (os.path.exists("transactionLog.txt") )  :
        print("Begin")
        shutil.copyfile("transactionLog.txt", "transactionLog1.txt")
        if os.path.exists("transactionLog1.txt"):
            print("Copy operation success!")
        mtime1 = time.ctime(os.stat("transactionLog.txt").st_mtime)
        mtime2 = time.ctime(os.stat("transactionLog1.txt").st_mtime)
        print("Last modify time of transactionLog.txt is: ", mtime1)
        print("Last modify time of transactionLog1.txt is: ", mtime2)
        if mtime1 < mtime2:
            print("Good job!")

if __name__ == "__main__":
    if (os.path.exists("transactionLog.txt") )  :
        mtime = time.ctime(os.stat("transactionLog.txt").st_mtime)
        if mtime > oldMtime:
            fileCopy()
    
