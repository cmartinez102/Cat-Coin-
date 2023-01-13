# works here in replit
# in shell run python RSA_private_public_keys.py
# generates private.pem and public.pem
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64

# Generates RSA Encryption + Decryption keys / Public + Private keys
key = RSA.generate(2048)

# creates private key
# pem is privacy enhanced mail
# Privacy Enhanced Mail (PEM) is an email security standard to provide secure electronic mail communication over the internet.
private_key = key.export_key()
with open('private.pem', 'wb') as f:
    f.write(private_key)

# creates public key
public_key = key.publickey().export_key()
with open('public.pem', 'wb') as f:
    f.write(public_key)
