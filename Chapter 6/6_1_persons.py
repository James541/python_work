people = [
    {
    'first_name': 'James',
    'last_name': 'Wagner',
    'age': 43,
    'current_city': 'Medford',
    },
    {
    'first_name': 'Joey',
    'last_name': 'Joe-Joe',
    'age': 31,
    'current_city': 'Seattle',
    },
    {
    'first_name': 'Monty',
    'last_name': 'Burns',
    'age': 110,
    'current_city': 'Springfield',
    },
    ]

for person in people:
    print(f'{person['first_name']} {person['last_name']} is {person['age']} years old and lives in {person['current_city']}.')