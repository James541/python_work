rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'the united states',
}

for river, nation in rivers.items():
    print(f'The {river.title()} River runs through {nation.title()} ')

for river in rivers.keys():
    print(river.title())

for river in rivers.values():
    print(river.title())