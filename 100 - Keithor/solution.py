from hashlib import *
from base64 import *
import sys
import signal




#hint: flag only contains capital letters and numbers and no special characters
character = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
flag_size = 6
possible_flag = [0] * flag_size

base64 = b'NGY3OTgwN2E3YzQ3ZjY5N2JkNWYwNmJlZWY5NTVjZmRmNGZkYWVmOGFkZThlZGY3MDc4NThmZTQyOTRkNzgwZDY5ZDRkNmE4OTdkODU5OGNlMzE0MmQyMDc2NDBjYTUxZDgyMTVkMGQ2YzY5Mzg3M2ZkMzJjMWY2ZTQ2ODc1MDAyN2I1ZGIzNGI3ZDljZTBhNzk3NTNlY2M3M2RhNjY0YTk5NTg4OWUwZDM2ZGI0YmZjNjhkZjlmYzhkYTNkMzY5YjI2NmU2MTdhNjE1OGQxNmNjYWQ0MTg5ZjBhM2RjYWU2MmQ5YjEwM2I1MGIwZDQzMzdjOTYxNjM0NzFiNDIzZmMyOGYzY2RhMjk0MTdiNzI4MGViOTMyMTQ5MjA3NWM1ODkwZGMwMzM0NzFjZjkxNzgxYTA3MDAxY2VhNjY5NmIzMmNkZjU2YjIxMjliYzc2YTgzMjE4YmVlNTJjODMwYThiZmMwOWVjNTVhZTM3MjExMGMwY2M4OTUwZWY1NzdkMzJlZDIxMWQ0MDMwN2MzZmQ2Njg0MTEzMzQxZTYwM2M='
m = b64decode(base64)

flag_hash = {
    "md5": m[0:32],
    "sha1": m[32:32 + 40],
    "sha224": m[32 + 40:32 + 40 + 56],
    "sha256": m[32 + 40 + 56:32 + 40 + 56 + 64],
    "sha384": m[32 + 40 + 56 + 64:32 + 40 + 56 + 64 + 96],
    "sha512": m[32 + 40 + 56 + 64 + 96:32 + 40 + 56 + 64 + 96 + 128]
             }


print(b'md5: ' + flag_hash["md5"])
print(b'sha1: ' + flag_hash["sha1"])
print(b'sha224: ' + flag_hash["sha224"])
print(b'sha256: ' + flag_hash["sha256"])
print(b'sha384: ' + flag_hash["sha384"])
print(b'sha512: ' + flag_hash["sha512"])



def permute_(size):
    if size == -1:
        a = ''.join(possible_flag)
        print(a)
        if md5(a.encode()).hexdigest().encode() == flag_hash["md5"]:
            print(b"flag: " + b64encode(a.encode()))
            exit(0)
    else:
        for x in range(0, len(character), 1):
            possible_flag[size] = character[x]
            permute_(size - 1)

def permute():
    permute_(flag_size - 1)

permute()
