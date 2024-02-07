ingredients = ['corn tortillas', 'limes', 'shredded chicken', 'cilantro', 'adobo chipotles', 'chopped jalapenos', 'chopped white onion', 'mole sauce', 'red salsa', 'cayenne pepper sauce']

print(f'The ingredients list starts with {len(ingredients)} items on it.\n')

print(f' The ingredients list in alphabetical order:\n{sorted(ingredients)}\n')

ingredients.append('green salsa')

print(f'We added a new item "green salsa" to the end of the list. \n {ingredients} \n')

ingredients.insert(3,'shredded pork')

print(f'We added a new item "shredded pork" to the middle of the list at index 3. \n {ingredients} \n')

removedItem = ingredients.pop(6)

print(f'We removed an item that was located at index 6.\n\nThe removed item was {removedItem}.')
print(ingredients)

ingredients.reverse()

print('\nJust for fun we reversed the order of the list.\n')
print(ingredients)

ingredients.sort()
print('\nAnd now, we have permenantly sorted the lsit into alphabetical order.\n')
print(ingredients)

print(f'\nThe ingredients list ended with {len(ingredients)} items on it.')
