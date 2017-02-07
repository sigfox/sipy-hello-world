from network import Sigfox
import socket
import binascii

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

print('I am device ',  binascii.hexlify(sigfox.id()) )
 # make the socket blocking
s.setblocking(True)

#Uplink + Downlink : Send then receive a reply from the network
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, True)

# send some bytes
#Send 0x0F  as an uplink message
output = s.send(bytes([0x0F]))
input = s.recv(8)
print(output)
print("... Downlink response ... ")
print(binascii.hexlify(input))
