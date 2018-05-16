# Network Scanner

import subprocess
import requests
import re

ping_error = "Request timeout for icmp_seq"

ipaddr_basic = "192.168.1.{}" # Replace 192.168.1 with your IP address prefix

def decodebytes(bytes_obj):
	return bytes_obj.decode(encoding="utf-8", errors="strict")

def ping(ip_address):
	global ping_error

	out = decodebytes(subprocess.Popen(["ping", "-t", "2", ip_address], stdout=subprocess.PIPE).communicate()[0])

	if ping_error in out[1]:
		return "1"
	else:
		return "0"

def get_mac(ip_address):
	arp_scan = decodebytes(subprocess.Popen(["arp", "-n", ip_address], stdout=subprocess.PIPE).communicate()[0])

	try:
		mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", arp_scan).groups()[0]
	except AttributeError:
		mac = "No Entry"
	
	return mac

for x in range(1, 256):
	ip_addr = ipaddr_basic.format(str(x))

	retx = ping(ip_addr)

	if retx == "0":
		mac_addr = get_mac(ip_addr)
		if mac_addr != "No Entry":
			mac_addr = mac_addr + " - " + requests.get("https://api.macvendors.com/{}".format(mac_addr)).text

		print("Client {}: {}".format(ip_addr, mac_addr))
	else:
		print("Unable to get MAC Address for client {}".format(ip_addr))
