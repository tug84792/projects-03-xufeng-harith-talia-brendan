import os.path

def checkExtension(images):
    for i in images:
        if i.endswith('jpg'):
            if os.path.isfile(i):
                print('File works')
                #upload file
            else:
                print('File error')
        else:
            print('File not .jpg')
