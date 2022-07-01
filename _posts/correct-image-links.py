
from os import listdir
import sys
import re

#run with command line arg of filename (including extention) ex python3 edit_photo_link.py filename.md

def handleCommandLineArgs():
    if(len(sys.argv)<=1):
        print("no command line arguments were found!")
        return False
    else:
        filename = sys.argv[1]
        print('Got filename from command line argument: ', filename)
        return filename

def isMd(file:str)->bool:
    try:
        result = file.index(".md") or file.index(".markdown")
        print(f"{file} is a markdown file, processing...")
        return True
    except ValueError:
        print(f"{file} is not markdown file!")
        return False

def removeFileNameExtension(filename:str)->str:
    pattern = '\.(md|markdown)'
    result = re.search(pattern, filename)
    return filename[0:result.start()]


def indexImageName(link:str):
    # find image name in url
    imageNameIndex = link.rfind('/')
    return link[imageNameIndex::]

def isImageLink(line:str):
    # regex detects ![any text]
    pattern = '!\[(.*?)\]'
    result = re.search(pattern, line)
    return result

def correctLink(filename, imageName):
    filename = removeFileNameExtension(filename)
    correctImageLink = f"![](/assets/{filename}{imageName})"
    return correctImageLink

def processFile(filename:str):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print('process file')
    for lineNumber,line in enumerate(lines):
        if(isImageLink(line)):
            print("old: " + line)
            newLink = correctLink(filename, indexImageName(line))
            print("new: " + newLink)
            lines[lineNumber] = newLink
    
    with open(filename, 'w') as outputFile:
        outputFile.writelines(lines)

filename = handleCommandLineArgs()
if(filename != False and isMd(filename)):
    print("processing...")
    processFile(filename)


# tests
##########
# test indexImageName: must extract image name from url
# print(indexImageName("![Untitled](Html-CSS%209360a589e4364ee18512ee052ecc52b3/Untitl_ed.png)"))

# test isImageLink: must return true if input is image link
# if(isImageLink("![Untitled](Html-CSS%209360a589e4364ee18512ee052ecc52b3/Untitled.png)")):
#     print("it works")

# test correctLink: must create correct image url
# print(correctLink("2022-blog-post.md", indexImageName("![Untitled](Html-CSS%209360a589e4364ee18512ee052ecc52b3/Untitl_ed.png)")))

# #test removeFileNameExtension(filename): must remove extension
# print(removeFileNameExtension("2022-02-post.md"))