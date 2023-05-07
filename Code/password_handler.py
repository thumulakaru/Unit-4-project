from passlib.hash import pbkdf2_sha512


def hash_password(password):
    return pbkdf2_sha512.hash(password)


def check_password(password, hashed):
    return pbkdf2_sha512.verify(password, hashed)
