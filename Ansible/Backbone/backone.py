from paramiko import SSHClient 
from scp import SCPClient
import logging
import os
import subprocess
import paramiko






def ssh_scp_files(ssh_host, ssh_user, ssh_password, source_volume, destination_volume):
    logging.info("In ssh_scp_files() method, copying files to the server")
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, username=ssh_user, password=ssh_password, look_for_keys=False)

    with SCPClient(ssh.get_transport()) as scp:
        scp.put(source_volume, recursive=True, remote_path=destination_volume)
        

def execute_scp_command(password, user):
    print("DC1")
    ssh_scp_files("10.43.192.112", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/arista/1/conf.txt", "/home/cvpadmin/")
    print("DC2")
    ssh_scp_files("10.43.192.113", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/arista/2/conf.txt", "/home/cvpadmin/")
    print("DC3")
    ssh_scp_files("10.43.192.114", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/arista/3/conf.txt", "/home/cvpadmin/")
    print("DC4")
    ssh_scp_files("10.43.192.115", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/arista/4/conf.txt", "/home/cvpadmin/")
    print("DC5")
    ssh_scp_files("10.43.192.116", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/arista/5/conf.txt", "/home/cvpadmin/")
    print("DC6")
    ssh_scp_files("10.43.192.117", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/arista/6/conf.txt", "/home/cvpadmin/")


def run_ansible_playbook(playbook_path):
    os.chdir(os.path.dirname(playbook_path))
    try:
        subprocess.run(["ansible-playbook", os.path.basename(playbook_path)], check=True)
    except subprocess.CalledProcessError as e:
        return False
    else:
        return True


def main():
    execute_scp_command("Exaprobe1234" , "cvpadmin")
    playbook = run_ansible_playbook("/home/rais/Arista_Nexus_Backbone/Ansible/replace.yml")
    return playbook
    

if __name__ == '__main__':
    main()
