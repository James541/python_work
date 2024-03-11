def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make."""
    print(f'\nMaking a {size.title()} a pizza with the following toppings:')
    for topping in toppings:
        print(f'-{topping}')

make_pizza('large','pepperoni')
make_pizza('medium','pepperoni', 'black olives', 'green olives', 'jalapeno peppers')
make_pizza('extra large','pepperoni', 'extra cheese')