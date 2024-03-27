from random import choice

drawing_pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']


def draw_winner():
    winning_combo = ""

    while len(winning_combo) < 4:
        pick = str(choice(drawing_pool))
        winning_combo += pick
    
    print(winning_combo)



draw_winner()