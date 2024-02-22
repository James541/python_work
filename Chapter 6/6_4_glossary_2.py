glossary = {
    'loop': 'A loop allows you to take the same action (or set of actions) with every item in a list.',
    'if': 'An "if statement" allows you to examine the current state of the program and respond appropriately to that state.',
    'variable': 'A variable allows you to assign a value to a named storage location to be used later in the program.',
    'list': 'A collection of items in a particular order.', 
    'dictionary': 'A dictionary is a data structure that stores a collection of key-value pairs.',
    'set': 'A set is a collection in which each ite, mst be unique',
    'keys() method': 'The keys() method tells Python to pull all the keys from a dictionary (w used w a loop)',
    'values() method': 'The values() method tells Python to pull all the values from a dictionary (w used w a loop)' 
    }

for word, definition in glossary.items():
    print(f'{word.capitalize()}: {definition}')