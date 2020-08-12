# Rosetta - Turn your Osu! song library into a Beat Saber one.
![Example use](/screenshots/rosetta.jpg?raw=true "Optional Title")

## Requirements:
- Python 3.x (haven't tested on versions lower than 3.8 but *should* be fine)
- `requests`
- `urllib3`

## Usage:
<sup>Disclaimer: Only tested on Windows and Poweshell, but GNU/Linux *should* be fine.</sup>  
Type in `python .\main.py <Osu! Songs path> <Beat Saber CustomLevels path>`

If you have games installed in a default location you can use these instead:
- `d` for default Osu! Songs path
- `o` or `s` for the deafult Beat Saber CustomLevels path in either Oculus or Steam version respectively  

You can also mix both like this:
`python .\main.py "F:\Games\rythm games\Osu!\Songs" s`

## Features:
- Deafult install locations
- Uses standard Beat Saber folder naming scheme
- You can choose up to 10 Beatsaver listings per provided Osu! song
- Automatically goes to another song after installation or not finding any candidates
- Shows song similarity (`kinda match`, `likely match` and `same name`)

## Upcoming:
- GUI?
- Create Beast Saber playlist made of downloaded songs
- Sort results by likeness
- YOLO mode (install everything without asking user)
- More than 10 entries to choose from (from experience that might be overkill though)
- Download progress bar
