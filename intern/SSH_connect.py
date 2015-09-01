__author__ = 'Liang Li'
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("", port=22, username='', password='')
channel = ssh.invoke_shell()

