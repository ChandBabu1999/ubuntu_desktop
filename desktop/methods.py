import os

parent_dir = "media"

def create_folder(directory):
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)