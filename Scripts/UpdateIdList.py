# python 3.9.2
# Author: huabi
# Date: 2021-03-25
# Encoding: UTF-8
# Description: UpdateIdList

import os

g_pictureDirPath = "../FemalTotalitarianismPicture"
g_quotesDirPath = "../FemalTotalitarianismQuotes"

def GetIdFromFile(fileName):
    if len(fileName) < 0:
        return None
    pos = fileName.find(':') + 1
    return fileName[pos:]

def UpdateIdList():
    idList = []
    for (root, dirs, files) in os.walk(g_pictureDirPath):
        for file in files:
            temp = GetIdFromFile(file)
            if temp is None or len(temp) < 0:
                continue
            idList.append(temp)

    for (root, dirs, files) in os.walk(g_quotesDirPath):
        for file in files:
            temp = GetIdFromFile(file)
            if temp is None or len(temp) < 0:
                continue
            idList.append(temp)

    with open("../Document/IdList.txt", 'a', encoding = "UTF-8") as idListFile:
        for id in idList:
            idListFile.write("%s\n" %(id))


if __name__ == "__main__":
    UpdateIdList()

