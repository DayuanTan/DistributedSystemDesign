import paramiko
import os

transport = paramiko.Transport(('172.16.193.129',22))
transport.connect(username="dayuan",password="1111")


srcfilepath="/home/dayuan/forGithubRepo/proj2_DS_Design/byzantineFT/transactionLog.txt"
srcfilepath.strip()
desfilepath="/home/dayuan/forGithubRepo/proj2_DS_Design/byzantineFT/transactionLog.txt"
desfilepath.strip()

sftp = paramiko.SFTPClient.from_transport(transport)
sftp.get(srcfilepath,desfilepath)
print("Update success!")

transport.close()
