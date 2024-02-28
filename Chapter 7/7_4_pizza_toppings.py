prompt = '\nWhat would you like on your pizza pie?'
prompt += '\n(When you are finished entering toppings, type \'quit\')\n'

topping = ''

while topping != 'quit':
    topping = input(prompt)
    print(f'{topping} has been added to your pizza pie!')

