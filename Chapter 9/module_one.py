class Users:
    """A model for users."""

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def describe_user(self):
        print(f'\nFull name: {self.name} {self.last_name}')
        
    def greet_user(self):
        print(f'Welcome {self.name}! We hope that you enjoy your visit.')


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user'] 

    def show_privileges(self):
        print(f'Available admin privileges:')
        for privilege in self.privileges:
            print(f'{privilege}')

class Admin(Users):

    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.privileges = Privileges()

