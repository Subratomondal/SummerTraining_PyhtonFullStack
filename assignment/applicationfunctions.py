"""
Date: 22-6-2025
Author: Subrato
Desc: for in -> Data Management Application for a music library. Here we write al the methods or we can say that the functions of application
"""

# library -> dictionary-> stores all albums
# album_info -> A tuple ->details : artist, title, year, songs(list)

def add_album(library,album_info):
    artist, title, year,songs = album_info
    library[title] =(artist,year,songs)
    return library

#song_selection -> List of tuples (album_title ,song_title)
# Creates a playlist from selected songs.
def create_playlist(library, song_selection):
    playlist =[]
    for album_title ,song_title in song_selection:
        if album_title in library:
            artist,year,songs = library[album_title]
            if song_title in songs:
                playlist.append(song_title)

    return playlist

#  Adds a new song to an existing album.
def add_song_to_album(library, album_title ,new_song):
    if album_title in library:
        artist, year,songs = library[album_title]
        if new_song not in songs:
            songs.append(new_song)
        library[album_title] = (artist,year,songs)

    else:
        print("Album not found.")

    return library


#Removes a song from the playlist
def remove_song_from_playlist(playlist,song):
    if song in playlist:
        playlist.remove(song)
    else:
        print('Song not found in playlist')

    return playlist


#Prints all albums with details from the library.
def display_library(library):
    if not library:
        print('Library is empty.')
    else:
        for title, (artist ,year,songs) in library.items():
            print(f'{title}| Artist : {artist}| Year: {year} | Songs: {songs}')

#Displays current playlist songs.
def display_playlist(playlist):
    if not playlist:
        print("Playlist is empty.")
    else:
        print(f'Playlist : {playlist}')



