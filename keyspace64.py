# Keyspace Puzzle 64 Random
# Made by Andrei Melek
# https://github.com/xh0st/keyspace64

try:
    import random
    from bitcoin import *

# If required imports are unavailable, we will attempt to install them!

except ImportError: 
    import subprocess
    subprocess.check_call(["python3", '-m', 'pip', 'install', 'bitcoin'])

while True:  
    low  = 0x8000000000000000 
    high = 0xffffffffffffffff
    val = str ( hex ( random.randrange( low, high ) ) )[2:]
    result = val.rjust(48 + len(val), '0')
    priv = result
    pub = privtopub(priv)
    pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
    addr = pubtoaddr(pubkey1)
    n = addr
    if n.startswith('16jY7qLJnxb7C'):
        print ("found!!",addr,result)
        s1 = result
        s2 = addr
        s3 = pub

        file = open('boom.txt', 'a')
        file.write("Private key: " + s1 + '\n' + "Public key: " + s3 + '\n' + "Address: " + s2 + '\n\n')    
        file.close()
    else:
        print ("searching...",addr,result)

