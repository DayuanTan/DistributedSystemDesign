from paramiko import SSHClient
from scp import SCPClient

ssh = SCPClient()
ssh.load_system_host_keys()
ssh.connect(hostname="172.16.193.129",port=22,username="dayuan",password="1111")

srcfilepath = os.path.join("home","dayuan","forGithubRepo","Proj2_DS_Design","byzantinFT","transactionLog.txt")

with SCPClient(ssh.get_transport()) as scp:
	scp.put(srcfilepath, "test.txt")
