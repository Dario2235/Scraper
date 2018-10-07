#! /usr/bin/env python
#
#
#
# Author: Dario Weeink
#

from paramiko import SSHClient
from scp import SCPClient
import paramiko

server = "85.214.242.152"
port = "22"

# De user moet hier zelf nog ingevuld worden hardcoded is het makkelijkste
user = ""

# Hier moet zelf het password nog ingevuld worden
password = ""

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client


def run(filename):
    ssh = createSSHClient(server, port, user, password)
    scp = SCPClient(ssh.get_transport())
    scp.put(filename, 'files')
    return