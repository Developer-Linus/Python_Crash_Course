def make_album(artist, album_title, number_of_tracks=""):
    album = {"album artist": artist, "album title": album_title}
    if number_of_tracks:
        album["tracks number"] = number_of_tracks
    return album


album1 = make_album("HHHhhhh", "titoenejen")
album2 = make_album("Hnvjeoijen", "djeofijdioekld")
album3 = make_album("jddj", "Jofiejeio eojeoijf", 23)

print([album1, album2, album3])
