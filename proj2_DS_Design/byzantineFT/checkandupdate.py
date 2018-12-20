import os
import paramiko
import time
import filecmp

srcip="172.16.193.129"
usrname="dayuan"
pw="1111"
srcfilepath="/home/dayuan/forGithubRepo/proj2_DS_Design/byzantineFT/transactionLog.txt"
srcfilepath.strip()

localfilepath="/home/dayuan/forGithubRepo/proj2_DS_Design/byzantineFT/transactionLog.txt"
localfilepath.strip()


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

while(1==1):
	time.sleep(10)
	ssh.connect(hostname=srcip,port=22,username=usrname,password=pw)
	stdid,stdout,stderr = ssh.exec_command('stat -c %Y ' + srcfilepath)
	mtimeOfSrcFile = int(stdout.read().strip())
	
	r = os.popen("stat -c %Y "+localfilepath)
	mtimeOfLocalFile = r.read()
	print("Modify time of romte file is: ", mtimeOfSrcFile)
	print("Modify time of local file is: ", mtimeOfLocalFile)
	
	if int(mtimeOfSrcFile) > int(mtimeOfLocalFile):
		os.system("python3 sftprcp.py")
	else:
		print("No need to update!\n\n")
