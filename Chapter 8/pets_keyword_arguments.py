def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f'\nI have a {animal_type}.')
    print(f'My {animal_type}\'s name is {pet_name.title()}.')

describe_pet(animal_type='cat', pet_name='finn')
describe_pet(animal_type='snake', pet_name='loki')
