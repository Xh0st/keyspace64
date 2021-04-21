# Keyspace Puzzle 64 Random
# Made by Andrei Melek
# https://github.com/xh0st/keyspace64

try:
    import random
    from bitcoin import *
    import random
    import hashlib
    import binascii
    import ecdsa

# If required imports are unavailable, we will attempt to install them!

except ImportError: 
    import subprocess
    subprocess.check_call(["python3", '-m', 'pip', 'install', 'bitcoin'])
    subprocess.check_call(["python3", '-m', 'pip', 'install', 'ecdsa'])

while True:  
    low  = 0x8000000000000000 
    high = 0xffffffffffffffff
    val = str ( hex ( random.randrange( low, high ) ) )[2:]
    private_key = val.rjust(48 + len(val), '0')
    sign = ecdsa.SigningKey.from_string(binascii.unhexlify(private_key), curve = ecdsa.SECP256k1)
    key_bytes = binascii.hexlify(sign.verifying_key.to_string()).decode('utf-8')
    key = ('0x' + binascii.hexlify(sign.verifying_key.to_string()).decode('utf-8'))
    # Get X from the key (first half)
    half_len = len(key_bytes) // 2
    key_half = key_bytes[:half_len]
    # Add bitcoin byte: 0x02 if the last digit is even, 0x03 if the last digit is odd
    last_byte = int(key[-1], 16)
    bitcoin_byte = '02' if last_byte % 2 == 0 else '03'
    public_key = bitcoin_byte + key_half
    addr = pubtoaddr(public_key)
    n = addr
    if n.startswith('16jY7qLJnx'):
        print ("found!!",addr,private_key)
        k1 = private_key
        k2 = public_key
        k3 = addr

        file = open('boom.txt', 'a')
        file.write("Private key: " + k1 + '\n' + "Public key: " + k2 + '\n' + "Address: " + k3 + '\n\n')    
        file.close()
    else:
        print ("searching...",addr,private_key)
