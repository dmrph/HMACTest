import hmac
import hashlib
import json

# Shared secret key
SECRET_KEY = b'mysecret'

# Read the file saved by appSend.py
with open("message.json", "r") as file:
    received_data = json.load(file)

# Extract the payload and signature
payload = received_data.get("payload")
received_signature = received_data.get("signature")

# Recreate the JSON string of the payload
payload_str = json.dumps(payload, sort_keys=True)
payload_bytes = payload_str.encode()

# Compute the HMAC signature over the received payload
computed_signature = hmac.new(SECRET_KEY, payload_bytes, hashlib.sha256).hexdigest()

# Verify that the received signature matches the computed signature
if hmac.compare_digest(received_signature, computed_signature):
    print("Signature verified!")
    print("Payload:", payload)
else:
    print("Signature verification failed!")
