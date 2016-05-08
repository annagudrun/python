import os
import re

VIDEO_TYPES = ('.wmv', '.mov', '.avi', '.divx', '.mpeg', '.mpg', '.m4p', '.3gp', '.amv', '.qt', '.rm', '.swf', '.mp4', '.mkv')
TRASH = ('.nfo' '.txt.')
def sortDirectory(dir):

    path = input('Full path to folder: ')
    search = input('Name of show: ')
    folderShowName = input('Name of folder: ')
   #gera edge case her ef tetta skyldi ekki vera rett
   #if not os.path.isdir(path):

    os.chdir(path)

    showFolder = ''

#bua til shows moppuna sem vid svo rodum i
    if not os.path.exists(os.path.join(path, 'Shows')):
       os.mkdir(os.path.join(path,'Shows'))
       showFolder = os.path.join(path,'Shows')
    else:
       showFolder = os.path.join(path,'Shows')
    print(showFolder)
    #labba svo i gegnum allt og tekka hvort tad se med tatta endingu

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(VIDEO_TYPES):
                file_path = os.path.join(root, file)
                hit = find_file(search, file) #gefur okkur true eda false eftir tvi hvort eitthvad finnist
                if hit:
                    beforeMove(file, file_path, folderShowName, showFolder)


def find_file(query, file_name):
    file_name = file_name.replace('_', '')
    query = re.sub(r'\W+', '', query) #taka ut non alpha symbolds
    file_name = re.sub(r'\W+', '', file_name)
    if query.lower() in file_name.lower():
        return True

    return False

def beforeMove(file, file_path, folderShowName, showFolder):
    seasons = re.search('[Ss]\s*[0-9]+\s*[Ee]\s*[0-9]+',file)
    seasons1 = re.search('\[[0-9]+x[0-9]+\]|[0-9]+x[0-9]+',file)

    new_file_path = showFolder + '/' + folderShowName
    print('newfilepath ' + new_file_path)
 #   os.mkdir(new_file_path)
 
