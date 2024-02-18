car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

drinks = ['water', 'coffee', 'beer']

print('\nDoes the list contain tea?')

if 'tea' in drinks:
    print('Yes.')
else:
    print('No it does not.')

print('\nDoes the list contain coffee?')

if 'coffee' in drinks:
    print("Yes.")
else:
    print('No it does not.')

print('\nAre there more than five items on the list?')

if len(drinks) > 5:
    print('Yes there are more than five items on the list.')
else:
    print('No.')
