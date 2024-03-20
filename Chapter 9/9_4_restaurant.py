class Restaurant:
    """A model for restaurants."""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 5

    def restaurant(self):
        print(f'{self.name} serves {self.cuisine} cuisine!')

    def open_restaurant(self):
        print(f'{self.name} is now open!')

    def customer_count(self):
        print(f'{self.number_served} customers served so far.')

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, number):
        self.number_served += number



restaurant = Restaurant('Bruno\'s', 'Italian')

restaurant.restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(10)
restaurant.increment_number_served(35)
restaurant.increment_number_served(25)
restaurant.customer_count()
