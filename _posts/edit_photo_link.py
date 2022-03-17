from os import listdir
# get list of all files in dir -> filter for .md files
# read file -> find line starting with ![] -> replace path with /assets/

def isImageLink(line:str)-> bool:
    return line[:3] == "![]"

def correctLink(line:str)->str:
    try:
        indexOfImageName = line.index("img/") + 4
    except ValueError as ve:
        print("could not find 'img/', returning same link")
        return line
    correctImageLink = f"![](/assets/{line[indexOfImageName::]}"
    return correctImageLink

def processFile(filename:str):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    for lineNumber,line in enumerate(lines):
        if(isImageLink(line)):
            print("old: " + line)
            print("new: " + correctLink(line))
            lines[lineNumber] = correctLink(line)
    
    with open(filename, 'w') as outputFile:
        outputFile.writelines(lines)

# processFile('2022-03-17-Feature-matching-using-BRISK-test.md')
def isMd(file:str)->bool:
    try:
        result = file.index(".md") or file.index(".markdown")
        return True
    except ValueError:
        print(f"{file} is not markdown file!")
        return False

filesInDir = listdir()
markdownFiles = []
for file in filesInDir:
    if(isMd(file)):
        markdownFiles.append(file)
for file in markdownFiles:
    processFile(file)