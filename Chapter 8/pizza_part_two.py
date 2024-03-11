def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print(f'-{topping}')

make_pizza('pepperoni')
make_pizza('pepperoni', 'black olives', 'green olives', 'jalapeno peppers')
make_pizza('pepperoni', 'extra cheese')