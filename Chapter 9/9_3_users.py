class Users:
    """A model for users."""

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


    def describe_user(self):
        print(f'\nFull name: {self.name} {self.last_name}')
        
    def greet_user(self):
        print(f'Welcome {self.name}! We hope that you enjoy your visit.')

user1 = Users('James', 'Wagner')
user2 = Users('Monty', 'Burns')
user3 = Users('Joe', 'Burrow')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

