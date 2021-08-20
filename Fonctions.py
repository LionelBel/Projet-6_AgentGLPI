# Définition des Fonctions utilisées par install.py

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

#5. Définition fonction config_agent
def config_agent():
	file = open("/etc/fusioninventory/agent.cfg" , "r")
	lignes = file.readlines()
	lignes[13]= "server = http://10.0.1.188/glpi/plugins/fusioninventory/\n"
	file.close()
	file = open("/etc/fusioninventory/agent.cfg", "w")
	file.writelines(lignes)
	file.close()

#6 Définition fonction send_Info
def send_info():
	os.system("pkill -USR1 -f -P 1 fusioninventory-agent")
