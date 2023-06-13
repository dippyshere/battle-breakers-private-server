"""
Battle Breakers Private Server / Master Control Program ""Emulator"" Copyright 2023 by Alex Hanson (Dippyshere).
Please do not skid my hard work.
https://github.com/dippyshere/battle-breakers-private-server
This code is licensed under the [TBD] license.

Utility script to generate a public key from a private key for the Battle Breakers Private Server.
"""

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Load the private key from file
with open("bb_private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=b'pw',  # Replace with your password if applicable
        backend=default_backend()
    )

# Get the public key from the private key
public_key = private_key.public_key()

# Serialize the public key to a PEM-encoded string
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Save the public key to a file
with open("bb_public_key.pem", "wb") as key_file:
    key_file.write(public_pem)
