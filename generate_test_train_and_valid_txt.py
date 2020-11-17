import os

with open('data/train.txt', 'w')as out:
    for images in [f for f in os.listdir('train') if f.endswith('jpg')]:
        out.write('train/' + img + '\n')

import os

with open('data/test.txt', 'w')as out:
    for images in [f for f in os.listdir('test') if f.endswith('jpg')]:
        out.write('test/' + img + '\n')

import os

with open('data/valid.txt', 'w')as out:
    for images in [f for f in os.listdir('valid') if f.endswith('jpg')]:
        out.write('valid/' + img + '\n')