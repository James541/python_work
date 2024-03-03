sandwich_orders = ['club', 'grilled cheese', 'pastrami', 'bacon basil tomato', 'pastrami', 'jon lee style steak sandwich', 'club', 'pastrami', 'hero', 'italian', 'pesto panini']

finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print('No Pastrami available today!\n')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'Working {sandwich.title()}...')
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f'\nYour {sandwich.title()} order is ready!')