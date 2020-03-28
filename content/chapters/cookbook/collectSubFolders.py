from os.path import join, isdir
from os import listdir

def collectSubFolders(folder):
    return [join(folder, sub)
            for sub in listdir(folder)
            if isdir(join(folder, sub))]


if __name__ == '__main__':
    subFolders = collectSubFolders('someFolder')
