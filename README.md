# Rosetta - Turn your Osu! song library into a Beat Saber one.
![Example use](/screenshots/rosetta.jpg?raw=true "Optional Title")

## Requirements:
- Python 3.x (haven't tested on versions lower than 3.8 but *should* be fine)
- `requests`
- `urllib3`

## How it works:
Rosetta takes your entire Osu! library and tries to find already existing Beat Saber counterparts using Beatsaver. You can choose which song on Beatsaver, if any, you'd like to download. Rosetta doesn't convert anything. Just searches so you won't have to.

## Usage:
### CLI:
<sup>Disclaimer: Only tested on Windows and Poweshell, but GNU/Linux *should* be fine.</sup>  
Type in `python .\main.py <Osu! Songs path> <Beat Saber CustomLevels path>`

If you have games installed in a default location you can use these instead:
- `d` for default Osu! Songs path
- `o` or `s` for the deafult Beat Saber CustomLevels path in either Oculus or Steam version respectively  

You can also mix both like this:
`python .\main.py "F:\Games\rythm games\Osu!\Songs" s`

### Script:
If the script finds any song that might be similar to the one from the Osu! library you'll be presented with up to 10 options to choose from. From there you either select the number of the map you'd like to download, skip with `Enter` or exit and finish.  
Listings aren't sorted by relevancy, just the order Beatsaver API returns (I might change it later), so you might want to show more than 2 options.  
Each song is presented with it's title, artist's name, downloads and votes. This may help you choose the map if there are many options for the same song.  
Of course it's not perfect. Many mappers tend to place their nicknames in the place of the song author field, which may be reflected on the results (usually `likely match` becomes `kinda match` in these cases).

## Features:
- Deafult install locations
- Uses standard Beat Saber folder naming scheme
- You can choose up to 10 Beatsaver listings per provided Osu! song
- Automatically goes to another song after installation or not finding any candidates
- Shows song similarity (`kinda match`, `likely match` and `same name`)

## Upcoming:
- GUI?
- Create Beast Saber playlist made up of downloaded songs
- Sort results by relevancy
- YOLO mode (install everything without asking user)
- More than 10 entries to choose from (from experience that might be overkill though)
- Download progress bar
- Support for egde cases (like absent fields in song's metadata)
- Ignore songs already present in both Osu! Songs and Beat Saber CustomLevels
