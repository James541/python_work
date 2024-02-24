# Store information about a pizza being ordered.

pizza = {
    'crust': 'deep dish',
    'toppings': ['pepperoni', 'green olives']
}

print(f'Order received for {pizza['crust'].title()} pizza with:')

for topping in pizza['toppings']:
    print(f'\t{topping.title()}')