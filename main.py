import socket
import json
import pandas as pd

UDP_IP = "192.168.162.125"
UDP_PORT = 5015
index = 0
index1 = 0

class beacon:
    url: str
    rssi: int
    mac: str
    def __init__(self, data : dict):
        self.url = data['URL']
        self.rssi = data['RSSI']
        self.mac = data['Mac']
    def __repr__(self):
        return(f' URL={self.url}            rssi= {self.rssi} mac={self.mac}')

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    #print("Type:", type(data))
    #print("received message: %s" % data)
    try :
        datadict = json.loads(data.decode())
        beac = beacon(datadict)
        print(beac)
    except :
        print(data.decode())
    #print("Type:", type(datadict))
    #print(datadict['Mac'])

    #pd.DataFrame(datadict)
    #print(pd.tail(3))
    #data = json.load(json_file)

    # Print the type of data variable






sock.close()
