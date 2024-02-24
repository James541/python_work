favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'c'],
    'phil':['python', 'javascript', 'rust',]
    }

for name, languages in favorite_languages.items(): 
    print(f'\n{name.title()}\'s favorite programming languages are:')
    for language in languages:
        print(f'\t {language.title()}')

    
    
    

