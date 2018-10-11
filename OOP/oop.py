`class StackOverflowUser(object):
    users = []


    def __init__(self, email, username, password, role='user'):
        self.email = email
        self.password = password
        self.username = username
        self.role = role
        self.id = len(StackOverflowUser.users) + 1

    def _save(self):
        new_user = {'used_id': self.id,
                    'email': self.email,
                    'username': self.username,
                    'password': self.password,
                    'role': self.role}
        return StackOverflowUser.users.append(new_user)

    def get_all_users(self):
        return StackOverflowUser.users

    def _update(user):
        pass

    def _delete(self):
        return StackOverflowUser.users.pop(1)

'''inherit class attributes'''
class Admin(StackOverflowUser):
    def __init__(self, email, username, password, role='user'):
        StackOverflowUser.__init__(
            self, email, username, password, role='Admin')

'''encapsulation'''
kelvin = StackOverflowUser('kelvin@gmail.com', 'kelvin', 'pass')
kelvin._save()
diana = StackOverflowUser('dianakerubo24@gmail.com', 'DianaKerubo', '1234taka')
diana._save()

jonathan = Admin('jonathanmusila@gmail.com', 'Jona', 'pass')
jonathan._save()


print(kelvin.get_all_users())