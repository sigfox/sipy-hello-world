from network import Sigfox
import socket
import binascii

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

print(binascii.hexlify(sigfox.id()) )
 # make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

# send some bytes
s.send(bytes([0x48, 0x65, 0x6C,  0x6C, 0x6F, 0x20, 0x50, 0x79, 0x63, 0x6F, 0x6D, 0x21]))
