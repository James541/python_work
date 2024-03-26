class Users:
    """A model for users."""

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def describe_user(self):
        print(f'\nFull name: {self.name} {self.last_name}')
        
    def greet_user(self):
        print(f'Welcome {self.name}! We hope that you enjoy your visit.')