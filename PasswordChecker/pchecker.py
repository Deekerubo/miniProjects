import re

def PasswordValidity():
     passwords = input("Enter passwords separated by a comma: ").split(",")
     regex = "^(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[$#@])[a-zA-Z0-9$#@]{6,12}$"
     PasswordValidity = []
     for password in passwords:
         if re.match(regex, password):
             PasswordValidity.append(password)
         return ','.join(PasswordValidity)