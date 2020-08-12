import os
import requests
import urllib.parse
import urllib.request
from time import sleep
from song import Song

def rann(map_path):
    # Pick first .osu file
    file = [x for x in os.listdir(map_path) if x.endswith('.osu')][0]
    osu_path = os.path.join(map_path, file)
    # print(osu_path)

    f = open(osu_path, 'r', encoding='UTF-8')
    lines = f.readlines()
    for line in lines:
        if 'Title:' in line:
            if 'Unicode' not in line:
                title = (line.replace('Title:', '')).replace('\n', '')
        if 'Artist:' in line:
            if 'Unicode' not in line:
                artist = (line.replace('Artist:', '')).replace('\n', '')

    return Song(title, artist)


def beatsaver(song, count):
    song_exists = True
    song_list = []

    url = 'https://beatsaver.com/api/search/text/0/?q=' + urllib.parse.quote(song.title)

    # very fucking dirty hack
    hed = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'}

    response = requests.get(url, headers=hed).json()
    listings = response["totalDocs"]
    if listings == 0:
        song_exists = False
    loop_range = range(count) if not listings < count else range(listings)

    if song_exists:
        for x in loop_range:
            try:
                got_title = response['docs'][x]['name']
                got_artist = response['docs'][x]['metadata']['songAuthorName']
                dl = str(response['docs'][x]['stats']['downloads'])
                up = str(response['docs'][x]['stats']['upVotes'])
                key = response['docs'][x]['key']

                song_list.append(Song(got_title, got_artist, key))

                if any(s in song.title.casefold().split(' ') for s in got_title.casefold().split(' ')):
                    if any(s in song.artist.casefold().split(' ') for s in got_artist.casefold().split(' ')):
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
                break
        print('\n')
    else:
        print('>[NOT FOUND]--------------\n')

    return song_list


def download(chosen_song):
    print('Downloading ' + chosen_song.title + ' by ' + chosen_song.artist)
    print('Key: ' + chosen_song.beatsaver_id)
    sleep(2)
    print('DONE!')
    sleep(1)


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


if __name__ == '__main__':
    clear()

    song_list = []
    for_counter = 0

    # Path to Osu! songs
    songs_dir = os.path.join('V:', 'Games', 'Osu!', 'Songs')

    # How many listings per song? (Weird way just for the convenience here)
    count = 3

    for track in os.listdir(songs_dir):
        song_list.append(rann(os.path.join(songs_dir, track)))

    print("Disclaimer: Many BeatSaber and Osu! mappers instead of original song artist's name type in their own. It's "
          "not that my code is THAT dumb. Just those mappers are. Also an 'Author' field may seem confusing if you "
          "ask me.")
    print("Also, any unrecognized input counts as skip, so there's that.\n")

    try:
        count = int(input('How many listings per song? ([Enter] for default = 3, max 10) '))
        if count > 10:
            print('Using max. (10)')
            count = 10
        elif count == 0:
            print('Using min. (1)')
            count = 1
        print(str(count) + ' listings.')
    except ValueError:
        print('Using default. (3)')

    for song in song_list:
        # inp_string = input('Press [Enter] for the next listing or [Q] and [Enter] to exit.\n')
        clear()

        print('Searching: ' + song.title + ' by ' + song.artist)
        returned_songs = beatsaver(song, count)
        if returned_songs:
            song_id = input('Choose song to install (id), skip [Enter] or exit [Q] and [Enter]: ')
            if song_id == 'Q' or song_id == 'q':
                break
            elif song_id.isdigit():
                if len(returned_songs) > int(song_id) >= 0:
                    download(returned_songs[int(song_id)])
                else:
                    print('Id out of range. Skipping...')
                    sleep(2)
            print('\n')
        else:
            print("No candidates found. Skipping...")
            sleep(2)

        for_counter += 1
    print('DONE for ' + str(for_counter) + ' songs!')
