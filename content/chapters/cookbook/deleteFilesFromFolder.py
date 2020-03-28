from os import remove, listdir

def deleteFilesFromFolder(folder, extension):
    paths = [nn for nn in listdir(folder) if nn.endswith(extension)]
    for eachP in paths:
        remove(eachP)


if __name__ == '__main__':
    deleteFilesFromFolder('someFolder', '.jpg')
