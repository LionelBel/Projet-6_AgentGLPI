#!/usr/bin/python 
# -*- coding: utf-8 -*-

#0. Importation de la classe Ansible module 
from ansible.module_utils.basic import AnsibleModule

#1. Importation du module Python OS pour interagir avec DEBIAN
import os

#2. Définition fonction install_dependencies
def install_dependencies():
	os.system("apt install -y dmidecode hwdata ucf hdparm")
	os.system("apt -y install perl libuniversal-require-perl libwww-perl libparse-edid-perl")
	os.system("apt -y install libproc-daemon-perl libfile-which-perl libhttp-daemon-perl")
	os.system("apt -y install libxml-treepp-perl libyaml-perl libnet-cups-perl libnet-ip-perl")
	os.system("apt -y install libdigest-sha-perl libsocket-getaddrinfo-perl libtext-template-perl")
	os.system("apt -y install libxml-xpath-perl libyaml-tiny-perl")

#3. Définition fonction download_agentFI
def download_agentFI():
	os.system("wget https://github.com/fusioninventory/fusioninventory-agent/releases/download/2.5.2/fusioninventory-agent_2.5.2-1_all.deb")

#4. Définition fonction dpkg_agentFI
def dpkg_agentFI():
	os.system("dpkg -i fusioninventory-agent_2.5.2-1_all.deb")

#5. Definition fonction envoie information du systeme
def send_info():
	os.system("pkill -USR1 -f -P 1 fusioninventory-agent")





#6. Définition du Module Ansible
def main():



	install_dependencies()
	download_agentFI()
	dpkg_agentFI()
	send_info()   
	reponse = {"result" : "Agent FusionInventoy installé ;)"}                   
	module.exit_json(changed=False, meta=reponse)

if __name__ == '__main__':
	main()