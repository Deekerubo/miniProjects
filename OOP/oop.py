# import hash library
import hashlib 

# class to handle stackoverflow users
class User(object):

    users = []


# user class constructor
    def __init__(self, email, username, password, role='user'):
        self.email = email
        self.password = hash(password)
        self.username = username
        self.role = role
        self.id = len(User.users) + 1

# create a user method
    def _save(self):
        new_user = {'used_id': self.id,
                    'email': self.email,
                    'username': self.username,
                    'password': self.password,
                    'role': self.role}
        return User.users.append(new_user)

# list all users method
    def get_all_users(self):
        return User.users

# returns username method
    def get_username(self):
        username = self.username
        return username


# updates user's username method
    def _update(user):
        pass

# deletes a user
    def _delete(self):
        index = self.id - 1
        return User.users.pop(index)

'''inherit class attributes'''
class Admin(User):
    def __init__(self, email, username, password, role='user'):
        User.__init__(
            self, email, username, password, role='Admin')

'''encapsulation'''
kelvin = User('kelvin@gmail.com', 'kelvin', 'pass')
kelvin._save()
kelvin._delete()
diana = User('dianakerubo24@gmail.com', 'DianaKerubo', '1234taka')
diana._save()

jonathan = Admin('jonathanmusila@gmail.com', 'Jona', 'pass')
jonathan._save()
kelvin._delete()

print(User.users)