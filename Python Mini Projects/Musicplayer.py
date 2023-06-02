import random, os
music_dir = 'F:\\VIDEOS\RESIZED'
songs = os.listdir(music_dir)
song = random.randint(0,len(songs))

# Prints The Song Name
print(songs[song])  
os.startfile(os.path.join(music_dir, songs[song]))
print(os.getpid())