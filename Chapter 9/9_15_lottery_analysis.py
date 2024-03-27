from random import choice

drawing_pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']
my_ticket = '0C54'
winner = 'no'
attempts = 0


def draw_winner():
    winning_combo = ""

    while len(winning_combo) < 4:
        pick = str(choice(drawing_pool))
        winning_combo += pick
        
    return winning_combo
    
while winner != 'yes':
    winning_combo = draw_winner()
    attempts += 1

    if str(winning_combo) == my_ticket or attempts > 1000000:
        print(winning_combo)
        winner = 'yes'
        print(f'You won! It took {attempts} attempts.')

