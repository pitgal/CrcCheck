#Piotr Gałuszka 28.04.2021

import sys,os, utils

CRC_FILE_EXT = ".crc"
SUCCESS = 0
FAIL_READ_CBPROJ = 1
FAIL_READ_CRC = 2
BAD_CRC = 3
NO_PARAM = 4


def prtExitMsg(returnCode, message = ""):
    print(message)
    sys.exit(returnCode)

def main():
    if len(sys.argv) < 2:
        prtExitMsg(NO_PARAM, "Usage {} <ProjectPath>".format(sys.argv[0]))

    cbprojPath = sys.argv[1]
    result, crc = utils.getFileSha256(cbprojPath)
    if not result:
        prtExitMsg(FAIL_READ_CBPROJ, "Load {} failed!".format(cbprojPath))

    crcFilePath = os.path.splitext(cbprojPath)[0] + CRC_FILE_EXT
    result, lines = utils.loadLines(crcFilePath)
    if not result:
        prtExitMsg(FAIL_READ_CRC, "Load {} failed!".format(crcFilePath))
    if not lines or crc != lines[0]:
        prtExitMsg(BAD_CRC, "Crc nonidentical!")
    else:
        prtExitMsg(SUCCESS, "OK Crc match")

if __name__ == "__main__":
    main()
