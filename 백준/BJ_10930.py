import hashlib
import sys

# SHA256 인코딩

data = sys.stdin.readline().replace("\n", "")
encoded = data.encode()
sha_data = hashlib.sha256(encoded).hexdigest()
print(sha_data)