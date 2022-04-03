import os
from PIL import Image

directory = r'./images'
file_format = '.jpg'

def createList(directory_path,file_format):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(file_format):
              with open('search.txt','a') as f:
                    f.write(f'{file}\n')
                    f.close()

def generateJpg(file_n):
    file_name,file_ext = os.path.splitext(file_n)
    file_source = Image.open(r'./images/{}'.format(file_n))
    return file_source.save(r'./new_files/{}.jpg'.format(file_name))

def readList():
    with open('search.txt', 'r') as readlist:
        return readlist.readlines()
        

createList(directory,file_format)
list_names = readList()
for index in range(len(list_names)): 
    generateJpg(list_names[index].replace('\n',''))