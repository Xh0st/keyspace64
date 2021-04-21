# Keyspace Puzzle 64 Random
# Made by Andrei Melek
# https://github.com/xh0st/keyspace64

try:
    from bitcoin import *
    import random

# If required imports are unavailable, we will attempt to install them!

except ImportError: 
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'bitcoin'])

while True:  
    low  = 0x8000000000000000 
    high = 0xffffffffffffffff
    val = str ( hex ( random.randrange( low, high ) ) )[2:]
    priv = val.rjust(48 + len(val), '0')
    pub = privtopub(priv)
    pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
    addr = pubtoaddr(pubkey1)
    n = addr
    if n.startswith('16jY7qLJnxb7C'):
        print ("found!!",addr,result)
        k1 = priv
        k2 = pub
        k3 = addr

        file = open('boom.txt', 'a')
        file.write("Private key: " + k1 + '\n' + "Public key: " + k2 + '\n' + "Address: " + k2 + '\n\n')    
        file.close()
    else:
        print ("searching...",addr,result)
