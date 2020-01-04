import os
import gui
import tkinter as tk
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
        extensions.append(ext[1])
    return extensions

def populate_foldersToMake(ext):
    for ext1 in ext:
        foldersToMake.append(ext1[1:])                          # Ex. mp3
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

def changePaths(addr, files):
    for file in files:
        orgFileAddr = os.path.join(addr, file)                  # Ex. /home/user/documents/someMusic.mp3
        whichFolder = filesAndExt[file]                         # Get extension of file
        path = os.path.join(addr, whichFolder + '_files', file) # Ex. /home/user/documents/mp3_files/someMusic.mp3
        os.rename(orgFileAddr, path)
    return None

def getOnlyFiles(dest):
    listFiles = os.listdir(dest)
    listFilesTrue = []
    for file in listFiles:
        path = os.path.join(dest, file)
        if os.path.isfile(path):
            listFilesTrue.append(file)
    return listFilesTrue

def organizeFiles(addrGUI):
    dest = addrGUI.get()
    addrGUI.delete(0, tk.END)
    if os.path.isdir(dest) == False:
        gui.message(False)
        return None
    allFiles = getOnlyFiles(dest)                               # Get list of files
    populate_filesAndExt(allFiles)                              # Populate Dictionary
    ext = identifyExt(dest, allFiles)
    populate_foldersToMake(ext)                                 # Populate list with unique ext
    generateFolderDirectories(dest, foldersToMake)              # Make new directories
    changePaths(dest, allFiles)   
    gui.message(True)

def main():
    # Window
    field = tk.Tk(className='File Categorizer')
    field.geometry("500x200")
    field.resizable(0, 0)

    # User Entry
    tk.Label(master=field, text='Address').grid(row=0, column=0)
    user = tk.Entry(field)
    user.grid(row=0, column=1)

    # Button Command
    tk.Button(master=field, text='Quit', command=field.quit).grid(row=0, column=5)
    tk.Button(master=field, text='Enter', command=lambda:organizeFiles(user)).grid(row=0, column=2)

    tk.mainloop()

if __name__ == '__main__':
    main()
