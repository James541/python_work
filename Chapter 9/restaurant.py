class Restaurant:
    """A model for restaurants."""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def restaurant(self):
        print(f'{self.name} serves {self.cuisine}!')

    def open_restaurant(self):
        print(f'{self.name} is now open!')