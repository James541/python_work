pets = ['dog', 'cat', 'fish', 'cat', 'monkey', 'dog', 'cat', 'dog', 'fish', 'snake']

while 'cat' in pets:
    pets.remove('cat')

while 'dog' in pets:
    pets.remove('dog')

print(pets)