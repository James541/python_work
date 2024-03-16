class Restaurant:
    """A model for restaurants."""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def restaurant(self):
        print(f'{self.name} serves {self.cuisine} cuisine!')

    def open_restaurant(self):
        print(f'{self.name} is now open!')

restaurant = Restaurant('Bruno\'s', 'Italian')

restaurant.restaurant()
restaurant.open_restaurant()