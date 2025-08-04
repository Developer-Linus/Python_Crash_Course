def make_album(artist, album_title):
    album = {"album artist": artist, "album title": album_title}
    return album


active = True
while active:
    print("\nProvide the artist and title of album")
    print("(Enter 'q' to quit the program.)")
    album_artist = input("album artist: ").lower()
    if album_artist == 'q':
        break
    album_title = input("Title of album: ").lower()
    if album_title == 'q':
        break
    created_album = make_album(album_artist, album_title)
    print(created_album)
