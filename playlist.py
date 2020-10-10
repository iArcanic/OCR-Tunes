import math
valid = False
while valid == False:
    user = input("Do you want a playlist created from a genre or a time limit\n")
    user = user.lower()
    if user == "genre" or user == "time limit":
        valid = True
        playlist = []
        time = 0
        index = 0
        if user == "genre":
            genre = input("What genre do you want the playlist to be?\n")
            while index < 5:
                if genre == song_genre[index]:
                    playlist.append(song_title[index])
                index+=1
        elif user == "time limit":
            time_limit = int(input("What is time limit do you want for your playlist in minutes\n"))
            time_limit = time_limit * 60 + 1 
            time = 0
            while time_limit > time and index < 5 :
                time = time + (math.modf(song_time[index])[1]*60) + (math.modf(song_time[index])[0]*100)
                if time < time_limit:
                    playlist.append(song_title[index])
                else:
                    time = time - (song_time[index]*60)
                index+=1 
print("We created this playlist for you:",playlist,"with",len(playlist),"songs")