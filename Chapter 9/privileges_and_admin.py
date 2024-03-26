from users import Users

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