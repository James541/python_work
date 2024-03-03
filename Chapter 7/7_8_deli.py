sandwich_orders = ['club', 'grilled cheese', 'bacon basil tomato', 'jon lee style steak sandwich', 'club', 'hero', 'italian', 'pesto panini']

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'Working {sandwich.title()}...')
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f'\nYour {sandwich.title()} order is ready!')