import os


def find():
    path = '.'
    writefile = open('files.txt', 'a')
    for (dirpath, dirnames, filenames) in os.walk(path):
        for file in filenames:
            writefile.write(os.path.join(dirpath, file + '\n'))
    writefile.close()
    return True


check = find()
