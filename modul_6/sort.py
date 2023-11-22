import sys
import re
from pathlib import Path
import os
import shutil

path = sys.argv[1]

ds_store_path = '.DS_Store'

images = []
videos = []
documents = []
music = []
archives = []
known_extensions = set()
unknown_extensions = set()

'''
def remove_DS_Store(path):
    os.remove(path)'''
 

images_dir = os.path.join(path, 'images')
videos_dir = os.path.join(path, 'videos')
docs_dir = os.path.join(path, 'documents')
music_dir = os.path.join(path, 'music')
archives_dir = os.path.join(path, 'archives')
unknown_files_dir = os.path.join(path, 'unknown_files')


def create_new_directories(path):
    
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    if not os.path.exists(videos_dir):
        os.makedirs(videos_dir)
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)
    if not os.path.exists(music_dir):
        os.makedirs(music_dir)
    if not os.path.exists(archives_dir):
        os.makedirs(archives_dir)
    if not os.path.exists(unknown_files_dir):
        os.makedirs(unknown_files_dir)
        

def sort(path):
    
    dir_path = Path(path).absolute()
    files_list = []
    files_list = collect_all_files(dir_path, files_list)
    
    create_new_directories(dir_path)

    regexp_images = re.compile(r'\.(jpg|png|jpeg|svg)$')
    regexp_videos = re.compile(r'\.(avi|mp4|mpv|mkv)$')
    regexp_docs = re.compile(r'\.(doc|docx|txt|pdf|xlsx|pptx)$')
    regexp_music = re.compile(r'\.(mp3|ogg|wav|amr)$')
    regexp_archives = re.compile(r'\.(zip|gz|tar)$')
    
    for file in files_list:
        norm_file = normalize(file)
        
        if regexp_images.search(norm_file.name):
            move_file(file, images_dir, norm_file)
            images.append(norm_file)
            
        elif regexp_videos.search(norm_file.name):
            move_file(file, videos_dir, norm_file)
            videos.append(norm_file)
            
        elif regexp_docs.search(norm_file.name):
            move_file(file, docs_dir, norm_file)
            documents.append(norm_file)
            
        elif regexp_music.search(norm_file.name):
            move_file(file, music_dir, norm_file)
            music.append(norm_file)
            
        elif regexp_archives.search(norm_file.name):
            move_file(file, archives_dir, norm_file)
            archives.append(norm_file)
            
        else:
            if len(norm_file.suffix) > 0:
                move_file(file, unknown_files_dir, norm_file)
                unknown_extensions.add(norm_file.suffix)

    for a in Path(archives_dir).iterdir():
        if regexp_archives.search(a.name):
            shutil.unpack_archive(a,archives_dir)
            
    with open(os.path.join(path, 'known_extensions.txt'), 'w') as file:
        for e in known_extensions:
            file.write(f'{e}\n')

    with open(os.path.join(path, 'unknown_extensions.txt'), 'w') as file:
        for e in unknown_extensions:
            file.write(f'{e}\n')

    remove_DS_files(path)
    remove_empty_folders(path)

    
def move_file(orig_file, directory, norm_file):

    new_path = os.path.join(directory, norm_file.name)
    shutil.move(orig_file.absolute(), new_path)
    known_extensions.add(norm_file.suffix)


def normalize(file):
    kirillic_translate = str.maketrans({
        'а':'a', 'б':'b','в':'v', 'г':'g','д':'d', 'е':'ie','ё':'io',
        'ж':'j','з':'z','и':'i','й':'y', 'к':'k', 'л':'l', 'м':'m',
        'н':'n', 'о':'o','п':'p', 'р':'r','с':'s', 'т':'t','у':'u',
        'ф':'f','х':'h','ц':'c','ч':'ch', 'ш':'sh','щ':'sh', 'ъ':'',
        'ы':'y', 'ь':'','э':'e', 'ю':'iu','я':'ia',
        'А':'A', 'Б':'B','В':'V', 'Г':'G','Д':'D', 'Е':'Ie','Ë':'Io',
        'Ж':'J','З':'Z','И':'I','Й':'Y', 'К':'K', 'Л':'L', 'М':'M',
        'Н':'N', 'О':'O','П':'P', 'Р':'R','С':'S', 'Т':'T','У':'U',
        'Ф':'F','Х':'H','Ц':'C','Ч':'Ch', 'Ш':'Sh','Щ':'Sh', 'Ъ':'',
        'Ы':'Y', 'Ь':'','Э':'E', 'Ю':'Iu','Я':'Ia'
        })
    
    name, extension  = os.path.splitext(os.path.basename(file))
    
    file_name = name.translate(kirillic_translate)
    file_name = re.compile(r'[^a-zA-Z0-9]').sub('_', file_name)
    
    return Path(file_name + extension)
    

def collect_all_files(path,files_list):
   
   
    for file in path.iterdir():
        
        if file.is_file():
            files_list.append(file)
        else:
            collect_all_files(file, files_list)
                   
    return files_list



def remove_empty_folders(directory):
    print('\n\ndirectory >>>>>>>',directory, '\n\n')
    regexp_ds = re.compile(r'\.(DS_Store)$')

    for folder in Path(directory).iterdir():
        folder_path = os.path.join(directory, folder)
        
        print(folder_path, '>>>>>>', Path(folder_path).absolute().is_dir())
        
        if regexp_ds.search(folder_path):
            print('\n\n\n<<<<<GOT DS>>>>>>\n\n\n')
            os.remove(Path(folder_path))
            continue

        elif os.path.isfile(folder_path):
            continue
        
        elif len(os.listdir(folder_path)) == 0:
            print('\n LEN folder_path = 0 \n')
            os.remove(folder_path)

        else:
            print('\n LEN folder_path > 0 \n')
            remove_empty_folders(folder_path)

        
        
        


            
       

        

        
            
            

    
    '''
    for root, dirs, files in os.walk(directory, topdown = False):
        
        print(root, '>>>>>', dirs, '>>>>>', files)
        
        for d in dirs:
            
            #print(d)
            folder_path = os.path.join(root, d)
            print('FOLDER PATH >>>>>>', folder_path)

            content = os.listdir(folder_path)
            #print(content)
            for c in content:
                print('PATH C >>>>>>>', Path(c).absolute())
                if c == ds_store_path:
                    os.remove(Path(c))
            
            if not any(os.listdir(folder_path)):
                print("empty")
                os.rmdir(folder_path)'''

    


if __name__ == '__main__':
    sort(path)
