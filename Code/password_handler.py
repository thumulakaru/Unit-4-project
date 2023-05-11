from passlib.hash import pbkdf2_sha512


def hash_password(password):
    '''This hashes a given password'''
    return pbkdf2_sha512.hash(password)


def check_password(password, hashed):
    '''This checks a given password against a given hashed'''
    return pbkdf2_sha512.verify(password, hashed)
