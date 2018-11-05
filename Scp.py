#! /usr/bin/env python
#
#
#
# Author: Dario
#

from scp import SCPClient
import paramiko


class Scp:

    """
    This class contains the Scp function
    """
    server = "85.214.242.152"
    port = 22

    # De user moet hier zelf nog ingevuld worden hardcoded is het makkelijkste
    user = ""

    # Hier moet zelf het password nog ingevuld worden
    password = ""


    def createSSHClient(self):
        """
        Create ssh connection
        :param server: IP address of the server.
        :param port: port number of the ssh connection.
        :param user: The ssh user.
        :param password: The password of the ssh user.
        :return: Ssh client.
        """
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.server, self.port, self.user, self.password)
        return client


    def run(self, filename):
        """
        Upload file to server.
        :param filename: Name of the uploaded file.
        :return: nothing
        """
        ssh = Scp.createSSHClient(self)
        scp = SCPClient(ssh.get_transport())
        print filename
        scp.put(filename, 'test')
        return
