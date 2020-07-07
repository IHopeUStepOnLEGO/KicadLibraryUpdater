# KicadLibraryUpdater
Simple tool to update local kicad libraries from github repositories. 

Written in python.

## DISCLAMER
Currently the program will **delete(!)** library folders with the same name as the requested one.

e.g. if you want to update "library" (kicad-symbols) from the official git, it will delete your existing "library" folder
and redownload it from git.

Make sure to have your own github libraries updated to not loose your data!

## How to use
1. place the files in the same directory your kicad symbols and footprints will be located (usually "...\KiCad\share\kicad\")
2. have a look into ".kicadUpdater\config\updaterConfig.json" to see the supported library names and git urls
3. modify the JSON through "main.py" to fit your needs (add/remove gits from the "updaterConfig.json")
4. load the libraries from the "updaterConfig.json"
5. use the "updateByKey(libName)" method to **delete(!)** and download the files from your github link into your local dir 

## Current status
python script for command line that:
- holds library names and git urls in an JSON config
- can add/remove libraries and git urls to this JSON config
- can update libraries, contained by the JSON config

## TODO
- make an GUI in QT and implement all neccessary functions
- create an executable file from the python scripts (pyinstaller ...)
- make an function to pull() from git and handle errors occuring from this approach

## future works
- look into how to add features to kicad itself
- implement this function - gui into kicad
