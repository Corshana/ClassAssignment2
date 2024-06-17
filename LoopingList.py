# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
tracks = 1
#Task 1 
for genre in genres:
    print(f"Track{tracks}: This is a {genre} track.")
    tracks += 1
#Task 2 
while True:
    for genre in genres:
        print(f"Track{tracks}: This is a {genre} track.")
        tracks += 1 
    if genre == "Hip Hop":
        print("Stopping the loop!")
        break