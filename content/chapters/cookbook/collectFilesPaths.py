from os.path import join, isfile
from os import listdir

def collectFilesPaths(folder, extension=''):
    """hidden files (starting with a dot) are filtered out"""
    paths = []
    for eachFileName in [nn for nn in listdir(folder) if nn.startswith('.') is False]:
        eachPath = join(folder, eachFileName)
        if isfile(eachPath) and eachPath.endswith(extension):
            paths.append(eachPath)
    return paths


if __name__ == '__main__':
    filePaths = collectFilesPaths('someFolder')