# Sample quiz app data for guidance only.
# Use this as a reference for your own seed/test data.

sample_artists = [
    {"id": 1, "name": "The Beatles"},
    {"id": 2, "name": "Miles Davis"},
]

sample_albums = [
    {"id": 1, "title": "Abbey Road", "artist_id": 1},
    {"id": 2, "title": "Kind of Blue", "artist_id": 2},
]

sample_songs = [
    {"id": 1, "title": "Come Together", "album_id": 1, "length_seconds": 259},
    {"id": 2, "title": "Something", "album_id": 1, "length_seconds": 182},
    {"id": 3, "title": "So What", "album_id": 2, "length_seconds": 545},
]

# Example usage (not for production):
# for artist in sample_artists:
#     print(artist["name"])
