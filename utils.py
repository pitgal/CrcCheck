#Piotr Gałuszka 23.02.2021

import os
import sys
import hashlib

def getFilesFromFile(file):
    try:
        result = []
        for strLine in open(file):
            if strLine.startswith('#'):
                continue
            project = strLine.strip().strip('"')
            if len(project):
                result.append(project)
        return result

    except:
        return []

def getFilesFromDir(dirPath, fileExtensions):
    result = []
    for dirname, dirnames, filenames in os.walk(dirPath):
        for filename in filenames:
            if getFileExt(filename) in fileExtensions.split(","):
                project = os.path.join(dirname, filename)
                result.append(project)
    return result

def loadLines(filePath):
    lines = []
    try:
        for line in open(filePath):
            lines.append(line)
        result = True
    except OSError:
        result = False
    return result, lines

def getHash(string):
    h = hashlib.sha256()
    h.update(string.encode())
    return h.hexdigest()

def getFileSha256(filePath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filePath,"rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
            return True, sha256_hash.hexdigest()
    except:
        return False, ""
    

def checkPythonVersion(majorVersion, minorVersion):
    if sys.version_info[0] < majorVersion or\
        (sys.version_info[0] == majorVersion and\
         sys.version_info[1] < minorVersion):
        return "Python {}.{} or later required!".format(majorVersion, minorVersion)

def findKeyword(lines, keyword):
    for line in lines:
        if keyword in line:
            return True
    return False

def getFileExt(filePath):
    return os.path.splitext(filePath)[1]

def getSortedList(colection):
    result = list(colection)
    result.sort()
    return result