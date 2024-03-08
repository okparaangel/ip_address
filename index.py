import socket
import uuid

ip= socket.gethostbyname(socket.gethostname())

adapters = []
for adapter in socket.if_nameindex():
    adapters.append(adapter[1])

mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)])

print("IP Address:", ip)
print("Network Adapters:", adapters)
print("MAC Address:", mac_address) 

