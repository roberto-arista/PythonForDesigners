from shutil import rmtree
from os import mkdir
from os.path import exists

def clean(folder):
    if exists(folder):
        rmtree(folder)
    mkdir(folder)


if __name__ == '__main__':
    clean('someFolder')
