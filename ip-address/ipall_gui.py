# Get public/local IP (internet protocol) addresses + hostname

from guizero import *
from requests import get
import socket
from sys import platform as _platform

def ip_get():
    localIP = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    hostname = socket.getfqdn()
    pip = get('https://api.ipify.org').text
    os = "Computer Operating System: "
    
    local.set("Internal IP: " + localIP)
    public.set("Public IP: {}".format(pip))
    hostnameTXT.set("Computer Name: " + hostname)
    
    if _platform == "linux" or _platform == "linux2":
       osTXT.set(os + 'Linux')
    elif _platform == "darwin":
       osTXT.set(os + 'macOS')
    elif _platform == "win32":
       osTXT.set(os + "Windows")
       
    blank0.set("")
    

# Window code
app = App(title="IP Address")

# Widget code
titling = Text(app, text="IP Address", size=25)

blank0 = Text(app, text="Click the 'Refresh' button to get your computer info.")

# Local, Public IPs, Hostname, OS (display)
local = Text(app, text="Local IP")
public = Text(app, text="Public IP")
hostnameTXT = Text(app, text="Hostname")
osTXT = Text(app, text="Operating System")

blank1 = Text(app, text="")

refresh = PushButton(app, command=ip_get, text="Refresh")

app.display()
