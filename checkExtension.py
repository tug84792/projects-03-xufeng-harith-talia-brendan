import os.path

def checkExtension(images):
    for i in images:
        if i.endswith('jpg'):
            if os.path.isfile(i):
                print('Downloading: ', i)
                download(i)
            else:
                print('File error: ', i)
        else:
            print('File not .jpg:', i)
