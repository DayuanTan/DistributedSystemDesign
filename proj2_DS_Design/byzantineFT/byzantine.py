import os
import paramiko
import time
import filecmp

ip1="172.16.193.129"
ip2="172.16.193.130"
ip3="172.16.193.131"
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

def checkandupdate(ip,thatipfilepath):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=ip,port=22,username=usrname,password=pw)
	stdid,stdout,stderr = ssh.exec_command('stat -c %Y ' + srcfilepath)
	mtimeOfSrcFile = int(stdout.read().strip())
	r = os.popen("stat -c %Y "+thatipfilepath)
	mtimeOfLocalFile = r.read()
	if int(mtimeOfSrcFile) > int(mtimeOfLocalFile):
		transport = paramiko.Transport((ip1,22))
		transport.connect(username=usrname,password=pw)
		sftp = paramiko.SFTPClient.from_transport(transport)
		sftp.get(srcfilepath,thatipfilepath)
		transport.close()
	ssh.close()

while(1==1):
	time.sleep(2)

	checkandupdate(ip1,ip1filepath)
	checkandupdate(ip2,ip2filepath)
	checkandupdate(ip3,ip3filepath)
	

	if ( filecmp.cmp(localfilepath,ip1filepath) and filecmp.cmp(localfilepath,ip2filepath) and not filecmp.cmp(localfilepath,ip3filepath) ):
		filecmp.clear_cache()		
		print("The file in "+ ip3 + " is not correct!!")
	if ( filecmp.cmp(localfilepath,ip1filepath) and not filecmp.cmp(localfilepath,ip2filepath) and filecmp.cmp(localfilepath,ip3filepath) ):
		filecmp.clear_cache()
		print("The file in "+ ip2 + " is not correct!!")
	if ( not filecmp.cmp(localfilepath,ip1filepath) and filecmp.cmp(localfilepath,ip2filepath) and filecmp.cmp(localfilepath,ip3filepath) ):
		filecmp.clear_cache()
		print("The file in "+ ip1 + " is not correct!!")
	
	
	if ( filecmp.cmp(localfilepath,ip1filepath) and filecmp.cmp(localfilepath,ip2filepath) and filecmp.cmp(localfilepath,ip3filepath) ):
		filecmp.clear_cache()		
		print("Everyone is same!")


