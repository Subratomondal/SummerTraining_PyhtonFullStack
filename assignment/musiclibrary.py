"""
Date: 22-6-2025
Author: Subrato
Desc: for in -> Data Management Application for a music library. Main code are written here .
"""
#retriving methods form applicationfunctions file

from assignment.applicationfunctions import add_album, create_playlist, add_song_to_album, remove_song_from_playlist, \
    display_library, display_playlist

library = {}
playlist = []

while True:
    print("\n--- Music Library Menu ---")
    print("1. Add a New Album")
    print("2. Create a Playlist")
    print("3. Add Song to Album")
    print("4. Remove Song from Playlist")
    print("5. View Library")
    print("6. View Playlist")
    print("7. Exit")

    choice  = int(input('Enter your choice (1-7): '))

    if choice == 1:
        artist = input("Enter artist name: ")
        title = input("Enter album title: ")
        year = int(input("Enter release year: "))
        songs_input = input("Enter song titles (comma-separated): ")
        songs = [s.strip() for s in songs_input.split(",")]
        album_info = (artist, title, year, songs)
        library = add_album(library, album_info)
        print("Album added successfully.")

    elif choice == 2:
        n = int(input("How many songs do you want to add to the playlist? "))
        song_selections = []
        for _ in range(n):
            album_title = input("Enter album title: ")
            song_title = input("Enter song title: ")
            song_selections.append((album_title, song_title))
        playlist = create_playlist(library, song_selections)
        print("Playlist created successfully.")

    elif choice == 3:
        album_title = input("Enter album title: ")
        new_song = input("Enter new song title to add: ")
        library = add_song_to_album(library, album_title, new_song)
        print("Song added to album successfully.")

    elif choice == 4:
        song = input("Enter song name to remove from playlist: ")
        playlist = remove_song_from_playlist(playlist, song)
        print("Song removed from playlist (if it existed).")

    elif choice == 5:
        print("\n--- Music Library ---")
        display_library(library)

    elif choice == 6:
        print("\n--- Playlist ---")
        display_playlist(playlist)

    elif choice == 7:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")