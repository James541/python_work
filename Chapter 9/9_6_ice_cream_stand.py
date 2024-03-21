class Restaurant:
    """A model for restaurants."""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def restaurant(self):
        print(f'{self.name} serves {self.cuisine}!')

    def open_restaurant(self):
        print(f'{self.name} is now open!')


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        """Represent aspects of a restaurant, specific to ice cream stands."""
        super().__init__(name, cuisine)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint', 'cookie dough']

    def display_flavors(self):
        print('Available Flavors: ')
        for flavor in self.flavors:
            print(f'{flavor.title()}')

restaurant = IceCreamStand('Bones for Cones', 'Ice Cream')

restaurant.restaurant()
restaurant.open_restaurant()
restaurant.display_flavors()