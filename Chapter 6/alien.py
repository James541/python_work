alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x-position'] = 0
alien_0['y-position'] = 25

print(alien_0)

alien_0['color'] = 'yellow'

print(alien_0)
print(f'The alien is now {alien_0['color']}')