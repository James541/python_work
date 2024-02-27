prompt = input('How many people are in your party today? ')
prompt = int(prompt)

if prompt > 8:
    print('Please give us a few minutes to prepare a table for you.')
else:
    print('Perfect. We have a table avaible for you now.')