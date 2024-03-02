age = ""

while age != 'quit':
    age = input('Please input your age or \'quit\' if your are done: ')
    if age == 'quit':
        break
        
    if int(age) < 3:
        cost = 'Free'
    elif int(age) >= 3 and int(age) <= 12:
        cost = '$10.00'
    else:
        cost = '$15.00'
    print(f'{cost}')
   