import os
import urllib.request, json, urllib.parse, requests
import song


def rann(map_path):
    # Pick first .osu file
    file = [x for x in os.listdir(map_path) if x.endswith(".osu")][0]
    osu_path = os.path.join(map_path, file)
    # print(osu_path)

    f = open(osu_path, "r", encoding="UTF-8")
    lines = f.readlines()
    for line in lines:
        if "Title:" in line:
            if "Unicode" not in line:
                title = (line.replace("Title:", "")).replace("\n", "")
        if "Artist:" in line:
            if "Unicode" not in line:
                artist = (line.replace("Artist:", "")).replace("\n", "")

    return song.Song(title, artist)


def beatsaver(song, count):
    url = "https://beatsaver.com/api/search/text/0/?q=" + urllib.parse.quote(song.title)
    # very fucking dirty hack
    hed = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/39.0.2171.95 Safari/537.36"}

    response = requests.get(url, headers=hed).json()
    for x in range(count):
        try:
            got_title = response['docs'][x]["name"]
            got_artist = response['docs'][x]['metadata']['songAuthorName']
            dl = str(response['docs'][x]['stats']['downloads'])
            up = str(response['docs'][x]['stats']['upVotes'])

            if any(s in song.title.casefold().split(" ") for s in got_title.casefold().split(" ")):
                if any(s in song.artist.casefold().split(" ") for s in got_artist.casefold().split(" ")):
                    print('>[' + str(x) + '][LIKELY MATCH]---------')
                else:
                    print('>[' + str(x) + '][KINDA MATCH]----------')
            elif song.title.casefold() in got_title.casefold():
                print('>[' + str(x) + '][SAME NAME]------------')
            else:
                print('>[' + str(x) + ']-----------------------')

            print('    Name: ' + got_title)

            if got_artist:
                print('    Artist: ' + got_artist)

            print('    DL: ' + dl)
            print('    UP: ' + up)
        except IndexError:
            print('>[NOT FOUND]--------------')
            break
    # print('>[END]--------------------\n')
    print("\n")


if __name__ == "__main__":
    song_list = []
    for_counter = 0
    # Path to Osu! songs
    songs_dir = os.path.join("V:", "Games", "Osu!", "Songs")

    # How many listings per song? (Weird way just for the convenience here)
    count = 2

    for track in os.listdir(songs_dir):
        song_list.append(rann(os.path.join(songs_dir, track)))

    print("Disclaimer: Many BeatSaber and Osu! mappers instead of original song artist's name type in their own. It's "
          "not that my code is THAT dumb. Just those mappers are. Also an \"Author\" field may seem confusing if you "
          "ask me.\n")

    for song in song_list:
        inp_string = input("Press Enter for the next listing or Q and Enter to exit.\n")
        if inp_string == "Q" or inp_string == "q":
            break
        print('Searching: ' + song.title + ' by ' + song.artist)
        beatsaver(song, count)
        for_counter +=1
    print("DONE for " + str(for_counter) + " songs!")
