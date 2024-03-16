class Restaurant:
    """A model for restaurants."""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def restaurant(self):
        print(f'\n{self.name} serves {self.cuisine} cuisine!')

    def open_restaurant(self):
        print(f'{self.name} is now open!')

restaurant = Restaurant('Bruno\'s', 'Italian')
restaurant_two = Restaurant('High Street Grill', 'American')
restaurant_three = Restaurant('Lemongrass', 'Thai')


restaurant.restaurant()
restaurant.open_restaurant()

restaurant_two.restaurant()
restaurant_two.open_restaurant()

restaurant_three.restaurant()
restaurant_three.open_restaurant()