class Users:
    """A model for users."""

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.login_attempts = 1


    def describe_user(self):
        print(f'\nFull name: {self.name} {self.last_name}')
        
    def greet_user(self):
        print(f'Welcome {self.name}! We hope that you enjoy your visit.')

    def increment_login_attempts(self):
        self.login_attempts += 1cd des  

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = Users('James', 'Wagner')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
