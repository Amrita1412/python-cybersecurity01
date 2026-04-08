import secrets
import string

chars = string.ascii_letters + string.digits + "@#$%&*"
password = ''.join(secrets.choice(chars) for _ in range(16))

print("Secure password:", password)