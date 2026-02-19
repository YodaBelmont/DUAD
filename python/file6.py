def read_songs_list(path):
    with open(path) as file:
        songs = file.readlines()
        songs.sort()
    write_songs(songs,"songs_sorted.txt")

def write_songs(songs, path):
    with open(path, "w") as file:
        for song in songs:
            file.write(song)

read_songs_list("songs.txt")