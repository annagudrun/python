import os
import re
import shutil

VIDEO_TYPES = ('.wmv', '.mov', '.avi', '.divx', '.mpeg', '.mpg', '.m4p', '.3gp', '.amv', '.qt', '.rm', '.swf', '.mp4', '.mkv')
TRASH = ('.nfo' '.txt.')

def sortDirectory(dir):

    path = input('Full path to folder: ')
    if not os.path.isdir(path):
        print('Invalid path, try again!')
        path = input('Full path to folder: ')
    search = input('Name of show: ')
    episode_folder = input('Name of folder: ')
   
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
                found = find_episode(search, file)
                # found gefur true ef tatturinn passar vid leitar streng
                #ta buum vid til moppu og faerum tattinn yfir
                #notandi velur nafn a moppunni 
                if found:
                    newPath = showFolder + '/' + episode_folder
                    if not os.path.exists(newPath):
                        os.mkdir(newPath)
                    if not os.path.exists(newPath +  '/' + file):
  #                      shutil.move(file, newPath)
                        os.rename(file_path, newPath +  '/' + file)
                        print(file + " MOVED")
    #flokkar eftir serium
    move_to_season_folders(newPath)

def find_episode(input_query, file_name):
    file_name = file_name.replace('_', '')
    input_query = re.sub(r'\W+', '', input_query) #taka ut non alpha symbolds
    file_name = re.sub(r'\W+', '', file_name)
    if input_query.lower() in file_name.lower():
        return True
    return False

def move_to_season_folders(episode_folder):

    os.chdir(episode_folder)
    print('episode folder: ' + episode_folder)
    for root,dirs,files in os.walk(episode_folder):
        for file in files:
            seas_type1 = re.search(r'[sS]\d+',file)
            seas_type2 = re.search(r'\[[0-9]+x\]\d+|[0-9]+x\d+',file)
            seas_type3 = re.search(r'[0-9]{3}', file)
            file_path = os.path.join(episode_folder, file)
            if seas_type1:
                seas = seas_type1.group()
                if len(seas) == 2:
                    seas = seas[0] + '0' + seas[1]
                seas = seas.lower()
                if not os.path.exists(os.path.join(episode_folder,seas)):
                    new_folder = os.mkdir(os.path.join(episode_folder,seas))
                else:
                    new_folder = os.path.join(episode_folder,seas)
                    shutil.move(file_path, new_folder)
            elif seas_type2:
                seas = seas_type2.group()
                new_seas = seas.split('x')
                if len(new_seas[0]) == 1:
                    seas_to_use = 's' + '0' + new_seas[0]
                else:
                    seas_to_use = 's'+ new_seas[0]
                if not os.path.exists(os.path.join(episode_folder, seas_to_use)):
                    new_folder = os.mkdir(os.path.join(episode_folder, seas_to_use))
                else:
                    new_folder = os.path.join(episode_folder, seas_to_use)
                    shutil.move(file_path, new_folder)
            elif seas_type3:
                seas = seas_type3.group()
                seas = 's' + '0' + seas[0]
                if not os.path.exists(os.path.join(episode_folder, seas)):
                    new_folder = os.mkdir(os.path.join(episode_folder, seas))
                else:
                    new_folder = os.path.join(episode_folder, seas)
                    shutil.move(file_path, new_folder)
                
                
