def make_album(artist, title, song_count= None):
    album_information = {'artist_name': artist.title(), 'album_title': title.title()}
    if song_count:
        album_information['song_count'] = song_count
    return album_information

while True:
    artist = input('Enter the name of the artist (or \'q\' to quit): ')
    if artist == 'q':
        break

    title = input('Enter the name of the album (or \'q\' to quit): ')
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)