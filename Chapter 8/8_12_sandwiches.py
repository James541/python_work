def make_sandwich(*toppings):
    print('\nMaking a sandwich with the following toppings:')
    for topping in toppings:
        print(f'-{topping}')

make_sandwich('turkey', 'bacon', 'mayo', 'lettuce', 'black pepper')
make_sandwich('salami', 'ham', 'pepperoni', 'mayo', 'italian dressing', 'onion', 'lettuce', 'pickle')
make_sandwich('ham','cheese')