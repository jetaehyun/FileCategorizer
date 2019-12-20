import os

foldersToMake = []
filesAndExt = {}

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

def populate_foldersToMake(ext):
    for ext1 in range(len(ext)):
        foldersToMake.append(ext1[1:]) # ex. mp3

def populate_filesAndExt(files):
    for file in files:
        ext = os.path.splitext(file)
        filesAndExt[file] = ext[1][1:]                          # Ex. value = mp3, key = someMusicFile.mp3

def generateFolderDirectories(dest, ext):
    addr = os.path.split(dest)
    for extension in range(len(ext)):
        newFolder = str(ext[extension]) + '_files'
        path = os.path.join(addr[0], newFolder)
        os.mkdir(path)

def OrganizeFiles(addr, files):
    for file in files:
        orgFileAddr = os.path.join(addr, file)                  # Ex. /home/user/documents/someMusic.mp3
        whichFolder = filesAndExt[file]                         # Get extension of file
        path = os.path.join(addr, whichFolder + '_files', file) # Ex. /home/user/documents/mp3_files/someMusic.mp3
        if os.path.isdir(path) == False: # only for testing
            continue 
        os.rename(orgFileAddr, path)


def main():
    dest = input('Address: ')                                   # Get address
    if os.path.isdir(dest) == False:
        print('Invalid Address...')
        exit()
    allFiles = os.listdir(dest)                                 # Get list of files
    populate_filesAndExt(allFiles)                              # Populate Dictionary
    populate_foldersToMake(identifyExt(allFiles))               # Populate list with unique ext
    generateFolderDirectories(dest, foldersToMake)              # Make new directories



if __name__ == '__main__':
    main()