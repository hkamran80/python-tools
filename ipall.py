# Get public/local IP (internet protocol) addresses + hostname

from requests import get
import socket
from sys import platform as _platform

localIP = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
hostname = socket.getfqdn()
pip = get('https://api.ipify.org').text
os = 'Your computer\'s os is: '

print('Your internal IP address is: ' + localIP)
print('Your public IP address is: {}'.format(pip))
print('Your computer\'s name is: ' + hostname)

if _platform == "linux" or _platform == "linux2":
   print(os + 'Linux.')
elif _platform == "darwin":
   print(os + 'macOS.')
elif _platform == "win32":
   print(os + 'Windows.')
