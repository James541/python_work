favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil':'python',
    }

participants = ['jen', 'james', 'sarah', 'amy', 'edward', 'cillian', 'phil']

for name in participants:
    if name in favorite_languages.keys():
        print(f'Thank you for taking our poll {name.title()}!')
    else:
        print(f'{name.title()}, please take our poll!')