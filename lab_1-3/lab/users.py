users = dict()
class User():
    def __init__(self, login, password, chmod):
        self.login = login
        self.password = password
        self.chmod = chmod
        users[self.login] = {
            'login': self.login,
            'password': self.password,
            'chmod': self.chmod
        }
        
admin = User('admin', 'admin', 0o777)
user = User('user', '1234', 0o666)
guest = User('guest', '', 0o000)