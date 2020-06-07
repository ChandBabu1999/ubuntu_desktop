import os

parent_dir = "media"

def create_folder(directory):
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)


def create_document(filename):
    path = os.path.join(parent_dir, filename)
    with open(path, 'w') as fp: pass

def moveTotrash(filename):
    os.remove(os.path.join(parent_dir, filename), os.path.join(parent_dir, "trash"))