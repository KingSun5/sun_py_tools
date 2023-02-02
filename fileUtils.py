import os


# @func:获取目录下所有文件（递归）
# @sPath:路径
def getAllFiles(sPath):
    filePathList = []
    for root, dirs, files in os.walk(sPath):
        for aa in files:
            filePathList.append(os.path.join(root, aa))
    return filePathList


# @func:获取当前目录下所有文件
# @sPath:路径
def getCurFiles(sPath):
    return os.listdir(sPath)


# @func:获取文件内容
# @sPath:路径
def getFileTxt(sPath):
    file = open(sPath, 'r', encoding="UTF-8")
    content = file.read()
    file.close()
    return content


# @func:获取文件所有行的内容
# @sPath:路径
def getAllFileLines(sPath):
    file = open(sPath, 'r', encoding="UTF-8")
    allLines = file.readlines()
    file.close()
    return allLines


# @func:获取文件某一行的内容
# @sPath:路径
def getFileLine(sPath, index):
    allLines = getAllFileLines(sPath)
    return allLines[index - 1]


# @func:写文件
# @sPath:路径
# @txt:写入内容
def writeFileTxt(sPath, txt):
    file = open(sPath, 'w', encoding="UTF-8")
    file.write(txt)
    file.close()


# @func:写文件通过数组
# @sPath:路径
# @lines:写入内容
def writeFileLines(sPath, lines):
    file = open(sPath, 'w', encoding="UTF-8")
    file.writelines(lines)
    file.close()


# @func:写如文件某一行
# @sPath:路径
# @txt:写入内容
# @index:写入行
def writeFileTxtByIndex(sPath, txt, index):
    lines = getAllFileLines(sPath)
    lines.insert(index-1, txt+"\n")
    txt = ''.join(lines)
    writeFileTxt(sPath, txt)


# @func:删除文件某一行
# @sPath:路径
# @indexList:删除行数组
def removeFileTxtByIndex(sPath, indexList):
    lines = getAllFileLines(sPath)
    if isinstance(indexList, list):
        indexList.sort()
        for x in range(len(indexList)-1, -1, -1):
            indexList.pop(indexList[x])
    else:
        lines.pop(indexList - 1)
    txt = ''.join(lines)
    writeFileTxt(sPath, txt)


# @func:替换文件某一行
# @sPath:路径
# @txt:替换内容
# @index:替换行
def replaceFileTxtByIndex(sPath, txt, index):
    lines = getAllFileLines(sPath)
    lines[index-1] = txt+"\n"
    txt = ''.join(lines)
    writeFileTxt(sPath, txt)


# @func:判断文件存在
# @sPath:路径
def isExist(sPath):
    return os.path.exists(sPath)