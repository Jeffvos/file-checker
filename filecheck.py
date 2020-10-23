import os

try:
    files = open('result.txt', 'r')
except FileNotFoundError as err:
    print('File not found')
    print(err)


class FileChecker:
    def __init__(self):
        self.countbyte = 0

    def filesize(self, filepath):
        os.path.getsize(filepath)
        return os.path.getsize(filepath)

    def checkfilelist(self, filelist):
        print("... Starting to count ...")
        for file in filelist:
            self.countbyte += self.filesize(file.rstrip("\n"))
        return self.btogb()

    def btogb(self):
        gbsize = self.countbyte / 1073741824
        return gbsize


check = FileChecker()
print(str(check.checkfilelist(files)) + "GB")
