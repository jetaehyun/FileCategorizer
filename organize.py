import os
from os import path
from os import rename

foldersToMake = []
filesAndExt = {}

def identifyExt(dest, whatFiles):
    extensions = []
    for file in whatFiles:
        checkFile = os.path.join(dest, file)
        if os.path.isfile(checkFile) == False:
            continue
        ext = os.path.splitext(file)
        if ext[1] in extensions:
            continue
        # print(ext[1])
        extensions.append(ext[1])
    return extensions

def populate_foldersToMake(ext):
    for ext1 in ext:
        foldersToMake.append(ext1[1:])                     # Ex. mp3
    return None

def populate_filesAndExt(files):
    for file in files:
        ext = os.path.splitext(file)
        filesAndExt[file] = ext[1][1:]                          # Ex. value = mp3, key = someMusicFile.mp3
    return None

def generateFolderDirectories(dest, ext):
    for extension in range(len(ext)):
        newFolder = str(ext[extension]) + '_files'
        path = os.path.join(dest, newFolder)
        if os.path.exists(path) == True:
            continue
        os.mkdir(path)
    return None

def OrganizeFiles(addr, files):
    for file in files:
        orgFileAddr = os.path.join(addr, file)                  # Ex. /home/user/documents/someMusic.mp3
        whichFolder = filesAndExt[file]                         # Get extension of file
        path = os.path.join(addr, whichFolder + '_files', file) # Ex. /home/user/documents/mp3_files/someMusic.mp3
        os.rename(orgFileAddr, path)
    return None

def getOnlyFiles(dest):
    listFiles = os.listdir(dest)
    for file in listFiles:
        path = os.path.join(dest, file)
        if os.path.isfile(path) == False:
            listFiles.remove(file)
    return listFiles
        
def main():
    dest = input('Address: ')                                   # Get address
    if os.path.isdir(dest) == False:
        print('Invalid Address...')
        exit()
    allFiles = getOnlyFiles(dest)                                 # Get list of files
    populate_filesAndExt(allFiles)                              # Populate Dictionary
    ext = identifyExt(dest, allFiles)
    populate_foldersToMake(ext)                             # Populate list with unique ext
    generateFolderDirectories(dest, foldersToMake)              # Make new directories
    OrganizeFiles(dest, allFiles)

if __name__ == '__main__':
    main()