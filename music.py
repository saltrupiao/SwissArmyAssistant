import os

# These functions are a straight ripped from file.py and modified for music player functionality
# Connor / Sal will know how these work in more detail

# Essentially, This allows the select tag to pull the contents of /static/media/Music

def dir_listing_music(path):
    # Show directory contents
    files = os.listdir(path)
    return files

def setFilePathMusic(folder):
    # Get the root of this python file
    root = os.path.dirname(os.path.abspath(__file__))
    if folder is None:
        # If the user just loaded the page there won't be a directory, so documents is default
        folder = "Music"
    # Add the /static/media path to the full path
    path = root + "/static/media/" + folder

    return path