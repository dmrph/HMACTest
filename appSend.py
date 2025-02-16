import hmac
import hashlib
import json

# Shared secret key
SECRET_KEY = b'mysecret'

# Define payload 
payload = {
    "message": "Sending a (hopefully) secure message",
    "sender": "mrph",
    "timestamp": "2025-02-16T12:00:00"
}

# Convert payload to a JSON string
payload_str = json.dumps(payload, sort_keys=True)
payload_bytes = payload_str.encode()

# Compute the HMAC signature using SHA256
signature = hmac.new(SECRET_KEY, payload_bytes, hashlib.sha256).hexdigest()

# Bundle payload and signature together
data_to_send = {
    "payload": payload,
    "signature": signature
}

# Save the bundled data to a JSON file
with open("message.json", "w") as file:
    json.dump(data_to_send, file, indent=4)

print("Payload and HMAC signature saved")
