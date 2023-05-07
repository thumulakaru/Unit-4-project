import re

regex = '^[a-z0-9.]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def validate_email(email):
    if re.search(regex, email):
        print("Email valid")
        return True
    else:
        print("Email not valid")
        return False



def validate_password(password):
    if len(password)<8 or len(password)>32:
        return False
    else:
        return True