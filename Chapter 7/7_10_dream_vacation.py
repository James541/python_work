vacations = {}
name = input('Hello! What is your name? ')
vacation = input('If you could go anywhere in the world for a week, where would it be? ')

vacations[name] = vacation

print(f'\n{name} would like to go to {vacation}.')
print(vacations)