import os.path

def checkExtension():
    filename = input('ImageName.jpg\n')
    while filename != 'q':
        if filename.endswith('.jpg'):
            if os.path.isfile(filename):
                print('File works')
                #upload file
            else:
                print('File error')
        else:
            print('File not .jpg')
        filename = input('ImageName.jpg\n')
