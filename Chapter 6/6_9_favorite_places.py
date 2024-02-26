places = {

    'james': ['the beach', 'in the forest', 'at home'],
    'amy': ['the beach', 'a lake', 'her imagination'],
    'finn': ['in bed', 'on the couch', 'in a lap'],
}

for name, places in places.items():
    print(f'\n{name.title()}\'s favorite places are:')
    for place in places:
        print(f'\t{place.title()}')