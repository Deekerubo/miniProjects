import re

def PasswordValidity():
    passwords = input("Enter passwords separated by a comma: ").split(",")
    print(passwords)
    regex = "^(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[$#@])[a-zA-Z0-9$#@]{6,12}$"
    PasswordValidity = ['dftg']
    for password in passwords:
        print("inside for loop")
        if re.match(regex, password):
             PasswordValidity.append(password)
    print (','.join(PasswordValidity))
    return ','.join(PasswordValidity)

print(PasswordValidity())
