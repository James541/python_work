favorite_numbers = {
    'james': [5, 42],
    'cillian': [2, 8],
    'amy': [42, 7],
    'finn': [10],
    'joe': [9, 1]
}

for key, favorite_numbers in favorite_numbers.items():
    print(f'\n{key.title()}\'s favorite numbers are:')
    for number in favorite_numbers:
        print(f'\t{number}')

