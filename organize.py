import os

foldersToMake = {}

def identifyExt(dest):
    extensions = []
    for file in dest:
        if os.path.isfile(file) == False:
            continue
        ext = os.path.splitext(file)
        if ext[1] in extensions:
            continue
        extensions.append(ext)
    return extensions

def populateDictWithExt(ext):
    for ext1 in range(len(ext)):
        foldersToMake[ext1] = ext1[1:] # .mp3 = mps

def main():
    dest = input('Address: ')
    allFiles = os.listdir(dest)


main()