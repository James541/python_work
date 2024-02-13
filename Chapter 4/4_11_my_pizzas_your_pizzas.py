pizzas = ['pepperoni', 'pepperoni and jalapenos','pepperoni and black olives' ]

friends_pizzas = pizzas[:]

pizzas.append('pepperoni, jalapeno, and banana peppers')
friends_pizzas.append('sausage')

print(f'My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print(f'\nMy friends favorite pizzas are:')
for friends_pizza in friends_pizzas:
    print(friends_pizza)
