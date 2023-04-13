import rsa

public_key, private_key = rsa.newkeys(1024)

with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))   

# from Crypto.PublicKey import RSA

# keyPair = RSA.generate(bits=1024)
# print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
# print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")