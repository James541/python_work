class Dog:
    """A simple attepmt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age


    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f'{self.name} is now sitting.')


    def roll_over(self):
        """Simulate rollong over in response to a command."""
        print(f'{self.name} rolled over!')


my_dog = Dog('Loki', 5)
your_dog = Dog('Bub', 3)

print(f'My dog\'s name is {my_dog.name}.')
print(f'My dog is {my_dog.age} years old.')
my_dog.sit()
my_dog.roll_over()

print(f'Your dog\'s name is {your_dog.name}.')
print(f'Your dog is {your_dog.age} years old.')
your_dog.sit()
your_dog.roll_over()



