import hashlib

def hash_password(password):
    hashed_pass = hashlib.sha1(bytes(password, 'UTF-8')).hexdigest()
    return hashed_pass