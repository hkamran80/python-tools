# Check Internet Connection

import socket
import time
import sys

def check(host="8.8.8.8", port=53, timeout=3):
    # 8.8.8.8 is the primary Google DNS server
    # 4.4.4.4 is the secondary server
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print("Connected")
        sys.exit()
    except Exception as ex:
        print(ex.message)
        print("Not Connected")
        os.system("sudo reboot")
        sys.exit()

check()
