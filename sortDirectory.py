import os
import re

VIDEO_TYPES = ('.wmv', '.mov', '.avi', '.divx', '.mpeg', '.mpg', '.m4p', '.3gp', '.amv', '.qt', '.rm', '.swf', '.mp4', '.mkv')
TRASH = ('.nfo' '.txt.')
def sortDirectory(dir):

    path = input('Full path to folder: ')
    search = input('Name of show: ')
    episode_folder = input('Name of folder: ')
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
                found = find_file(search, file)
                # found gefur true ef tatturinn passar vid leitar streng
                #ta buum vid til moppu og faerum tattinn yfir
                #notandi velur nafn a moppunni 
                if found:
                    newPath = showFolder + '/' + episode_folder
                    if not os.path.exists(newPath):
                        os.mkdir(newPath)
                    if not os.path.exists(newPath +  '/' + file):
                        os.rename(file_path, newPath +  '/' + file)
                        print(file + " MOVED TO " + newPath)


def find_file(input_query, file_name):
    file_name = file_name.replace('_', '')
    input_query = re.sub(r'\W+', '', input_query) #taka ut non alpha symbolds
    file_name = re.sub(r'\W+', '', file_name)
    if input_query.lower() in file_name.lower():
        return True

    return False
