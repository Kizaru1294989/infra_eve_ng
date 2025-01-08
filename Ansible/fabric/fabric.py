from paramiko import SSHClient
from scp import SCPClient
import logging
import os
import subprocess
import paramiko

def ssh_scp_files(ssh_host, ssh_user, ssh_password, source_volume, destination_volume, hostname):
    """
    Copy files to the server using SCP and print the hostname being processed.
    """
    print(f"Copying files to {hostname} at {ssh_host}")
    logging.info(f"In ssh_scp_files() method, copying files to the server: {hostname}")
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ssh_host, username=ssh_user, password=ssh_password, look_for_keys=False)

    with SCPClient(ssh.get_transport()) as scp:
        scp.put(source_volume, recursive=True, remote_path=destination_volume)
        

def border_leaf(password, user):
    ssh_scp_files("10.43.192.156", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/leaf/Border/1/conf.txt", "/home/cvpadmin/", "LEAF-BORDER-1")
    ssh_scp_files("10.43.192.157", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/leaf/Border/2/conf.txt", "/home/cvpadmin/", "LEAF-BORDER-2")         

def leaf(password, user):
    ssh_scp_files("10.43.192.156", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/leaf/1/conf.txt", "/home/cvpadmin/", "LEAF-BORDER-1")
    ssh_scp_files("10.43.192.157", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/leaf/2/conf.txt", "/home/cvpadmin/", "LEAF-BORDER-2") 
    ssh_scp_files("10.43.192.160", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/leaf/3/conf.txt", "/home/cvpadmin/", "LEAF-3")
    ssh_scp_files("10.43.192.161", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/leaf/4/conf.txt", "/home/cvpadmin/", "LEAF-4")
    ssh_scp_files("10.43.192.162", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/leaf/5/conf.txt", "/home/cvpadmin/", "LEAF-5")
    ssh_scp_files("10.43.192.163", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/leaf/6/conf.txt", "/home/cvpadmin/", "LEAF-6") 
    ssh_scp_files("10.43.192.164", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/leaf/7/conf.txt", "/home/cvpadmin/", "LEAF-7")
    ssh_scp_files("10.43.192.165", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/leaf/8/conf.txt", "/home/cvpadmin/", "LEAF-8")  

def spine(password, user):
    ssh_scp_files("10.43.192.158", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/spine/1/conf.txt", "/home/cvpadmin/", "SPINE-1")
    ssh_scp_files("10.43.192.159", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/spine/2/conf.txt", "/home/cvpadmin/", "SPINE-2") 

def access(password, user):
    ssh_scp_files("10.43.192.166", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/Access/1/conf.txt", "/home/cvpadmin/", "ACCESS-1") 
    ssh_scp_files("10.43.192.167", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/Access/2/conf.txt", "/home/cvpadmin/", "ACCESS-2")
    ssh_scp_files("10.43.192.168", user, password, "/home/rais/Arista_Nexus_Backbone/Conf-File/Fabric-EVPN/Access/3/conf.txt", "/home/cvpadmin/", "ACCESS-3")  

def execute_scp_command(password, user):
    # border_leaf(password, user)
    spine(password, user)
    leaf(password, user)
    # access(password, user)

def run_ansible_playbook(playbook_path):
    os.chdir(os.path.dirname(playbook_path))
    try:
        subprocess.run(["ansible-playbook", os.path.basename(playbook_path)], check=True)
    except subprocess.CalledProcessError as e:
        return False
    else:
        return True

def main():
    execute_scp_command("Exaprobe1234", "cvpadmin")
    playbook = run_ansible_playbook("/home/rais/Arista_Nexus_Backbone/Ansible/fabric/replace.yml")
    return playbook

if __name__ == '__main__':
    main()
