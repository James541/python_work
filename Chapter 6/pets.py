pets = [
    {
    'name':'finn',
    'owner':'amy',
    'animalType':'cat',
    },
    {
    'name':'sloth',
    'owner':'cillian',
    'animalType':'sloth',
    },
    {
    'name':'buck-buck',
    'owner':'james',
    'animalType':'chicken',
    },
]

for pet in pets:
    print(f'{pet['owner'].title()} has a {pet['animalType']} named {pet['name'].title()}. {pet['name'].title()} is a good {pet["animalType"]}!')