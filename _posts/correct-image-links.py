
from os import listdir
import sys
import re


def indexImageName(link:str):
    # find image name in url
    pattern='[\w-]+\.(jpg|png|txt)'
    return re.search(pattern, link).group()

def isImageLink(line:str):
    # regex detects ![untitled]
    pattern = '!\[[A-Z*a-z*]*\]'
    result = re.search(pattern, line)
    return result

def correctLink(filename, imageName):
    correctImageLink = f"![](/assets/{filename}/{imageName}"
    return correctImageLink

def processFile(filename:str):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print('process file')
    for lineNumber,line in enumerate(lines):
        if(isImageLink(line)):
            print("old: " + line)
            print("new: " + correctLink(filename))
            lines[lineNumber] = correctLink(filename, indexImageName(line))
    
    with open(filename, 'w') as outputFile:
        outputFile.writelines(lines)


# tests
##########
# test indexImageName: must extract image name from url
# print(indexImageName("![Untitled](Html-CSS%209360a589e4364ee18512ee052ecc52b3/Untitl_ed.png)"))

# test isImageLink: must return true if input is image link
# if(isImageLink("![Untitled](Html-CSS%209360a589e4364ee18512ee052ecc52b3/Untitled.png)")):
#     print("it works")

# test correctLink: must create correct image url
# print(correctLink("2022-blog-post.md", indexImageName("![Untitled](Html-CSS%209360a589e4364ee18512ee052ecc52b3/Untitl_ed.png)")))