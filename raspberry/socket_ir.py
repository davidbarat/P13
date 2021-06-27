import socket
import requests
import json
import time
import os
from datetime import datetime
from gpiozero import LED
from signal import pause

SOCKPATH = "/var/run/lirc/lircd"
sock = None
led = LED(4)
group_name = "Barat"
now = datetime.now()
dt_formated = now.strftime("%Y-%m-%dT%H:%M:%S")
status = "open"
token = os.getenv("TOKEN")
url = 'http://167.71.57.121/event/list/'
data = {
    "date_event": dt_formated,
    "group_name": group_name,
    "status": status}
headers = {
    'Content-type': 'application/json',
    'Authorization': 'Token d0c55c311586b688894de0d39e0a011f47cedee3'}

# Establish a socket connection to the lirc daemon
def init_irw():
    global sock
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(SOCKPATH)
    print ('Socket connection established!')
    print ('Ready...')

# parse the output from the daemon socket
def getKey():
    while True:
        data = sock.recv(128)
        data = data.strip()
        if (len(data) > 0):
            break

    words = data.split()
    return words[2], words[1]

if __name__ == '__main__':
    try:
        init_irw()
        while True:
            key, dir = getKey()
            key = key.decode() # This variable contains the name of the key
            dir = dir.decode() # This variable contains the direction (pressed/released)
            # print(dir)
            # print(key)
       	    # Only print the name when the key is pressed (and not released)
       	    if (dir == '00' and key == 'BUTTON_1'):
       	        print ("BUTTON 1 PRESSED!")
                r = requests.post(url, headers=headers, data=json.dumps(data)) 
                # led.blink()
                led.on()
                time.sleep(1)
                led.off()
                time.sleep(1)
                led.on()
                time.sleep(1)
                led.off()
                time.sleep(1)
                led.on()
                time.sleep(1)
                led.off()

    except KeyboardInterrupt:
    	print ("\nShutting down...")
    	# Close the socket (if it exists)
    	if (sock != None):
       	    sock.close()
    	print ("Done!")
