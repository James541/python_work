usernames = ['admin', 'james', 'amy', 'cillian', 'finn']

for username in usernames:
    if username == 'admin':
        print('Hello Admin! Would you like to run a status report?')
    else:
        print(f'Hello {username.capitalize()}! Thank you for logging in today.')
