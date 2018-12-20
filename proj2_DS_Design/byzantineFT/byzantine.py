import os
import paramiko
import time
import filecmp

ip1="172.16.193.129"
ip2="172.16.193.129"
ip3="172.16.193.129"
usrname="dayuan"
pw="1111"

srcfilepath="/home/dayuan/forGithubRepo/proj2_DS_Design/byzantineFT/transactionLog.txt"
srcfilepath.strip()

localfilepath="/home/dayuan/forGithubRepo/proj2_DS_Design/byzantineFT/transactionLog.txt"
localfilepath.strip()

ip1filepath="/home/dayuan/forGithubRepo/proj2_DS_Design/byzantineFT/transactionLogip1.txt"
ip1filepath.strip()
ip2filepath="/home/dayuan/forGithubRepo/proj2_DS_Design/byzantineFT/transactionLogip2.txt"
ip2filepath.strip()
ip3filepath="/home/dayuan/forGithubRepo/proj2_DS_Design/byzantineFT/transactionLogip3.txt"
ip3filepath.strip()


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

while(1==1):
	time.sleep(2)

	ssh.connect(hostname=ip1,port=22,username=usrname,password=pw)
	stdid,stdout,stderr = ssh.exec_command('stat -c %Y ' + srcfilepath)
	mtimeOfSrcFile = int(stdout.read().strip())
	r = os.popen("stat -c %Y "+ip1filepath)
	mtimeOfLocalFile = r.read()
	if int(mtimeOfSrcFile) > int(mtimeOfLocalFile):
		transport = paramiko.Transport((ip1,22))
		transport.connect(username=usrname,password=pw)
		sftp = paramiko.SFTPClient.from_transport(transport)
		sftp.get(srcfilepath,ip1filepath)
		transport.close()


	ssh.connect(hostname=ip2,port=22,username=usrname,password=pw)
	stdid,stdout,stderr = ssh.exec_command('stat -c %Y ' + srcfilepath)
	mtimeOfSrcFile = int(stdout.read().strip())
	r = os.popen("stat -c %Y "+ip2filepath)
	mtimeOfLocalFile = r.read()
	if int(mtimeOfSrcFile) > int(mtimeOfLocalFile):
		transport = paramiko.Transport((ip2,22))
		transport.connect(username=usrname,password=pw)
		sftp = paramiko.SFTPClient.from_transport(transport)
		sftp.get(srcfilepath,ip2filepath)
		transport.close()


	ssh.connect(hostname=ip3,port=22,username=usrname,password=pw)
	stdid,stdout,stderr = ssh.exec_command('stat -c %Y ' + srcfilepath)
	mtimeOfSrcFile = int(stdout.read().strip())
	r = os.popen("stat -c %Y "+ip3filepath)
	mtimeOfLocalFile = r.read()
	if int(mtimeOfSrcFile) > int(mtimeOfLocalFile):
		transport = paramiko.Transport((ip3,22))
		transport.connect(username=usrname,password=pw)
		sftp = paramiko.SFTPClient.from_transport(transport)
		sftp.get(srcfilepath,ip3filepath)
		transport.close()



	if ( filecmp.cmp(localfilepath,ip1filepath) and filecmp.cmp(localfilepath,ip2filepath) and ~filecmp.cmp(localfilepath,ip3filepath) ):
		print("The file in "+ ip3 + "1 is not correct!!")
	if ( filecmp.cmp(localfilepath,ip1filepath) and ~filecmp.cmp(localfilepath,ip2filepath) and filecmp.cmp(localfilepath,ip3filepath) ):
		print("The file in "+ ip2 + "2 is not correct!!")
	if ( ~filecmp.cmp(localfilepath,ip1filepath) and filecmp.cmp(localfilepath,ip2filepath) and filecmp.cmp(localfilepath,ip3filepath) ):
		print("The file in "+ ip1 + "3 is not correct!!")
	
	
	print("--")


