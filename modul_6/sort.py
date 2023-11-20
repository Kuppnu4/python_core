import sys
import re
from pathlib import Path
import os
import shutil

path = sys.argv[1]

regexp_images = re.compile(r'\.(jpg|png|jpeg|svg)$')
images_dir = os.path.join(path, 'images')

regexp_videos = re.compile(r'\.(avi|mp4|mpv|mkv)$')
videos_dir = os.path.join(path, 'videos')

regexp_docs = re.compile(r'\.(doc|docx|txt|pdf|xlsx|pptx)$')
docs_dir = os.path.join(path, 'documents')

regexp_music = re.compile(r'\.(mp3|ogg|wav|amr)$')
music_dir = os.path.join(path, 'music')

regexp_archives = re.compile(r'\.(zip|gz|tar)$')
archives_dir = os.path.join(path, 'archives')

known_extensions = set()
unknown_extensions = set()

def sort(path):
    dir_path = Path(path).absolute()
    files_names = []
    files_list = read_files_names(dir_path, files_names)
    
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


    for file in files_list:
        norm_file_name = normalize(file)
        
        
        if regexp_images.search(norm_file_name):
            write_move(file, images_dir, norm_file_name)
            

        elif regexp_videos.search(file.name):
            write_move(file, videos_dir, norm_file_name)
            
        elif regexp_docs.search(file.name):
            write_move(file, docs_dir, norm_file_name)
            
        elif regexp_music.search(file.name):
            write_move(file, music_dir, norm_file_name)
            
        elif regexp_archives.search(file.name):
            write_move(file, archives_dir, norm_file_name)
            
        else:
            if len(file.suffix) > 0:
                unknown_extensions.add(file.suffix)
            
    with open(os.path.join(path, 'known_extensions.txt'), 'w') as file:
        for e in known_extensions:
            file.write(f'{e}\n')

    with open(os.path.join(path, 'unknown_extensions.txt'), 'w') as file:
        for e in unknown_extensions:
            file.write(f'{e}\n')
    
def write_move(file, directory, norm_name):

    new_path = os.path.join(directory, norm_name)
    shutil.move(file.absolute(), new_path)
    known_extensions.add(file.suffix)


def normalize(file):
    return re.sub(r'[а-яА-я]','_',file.name)
    

def read_files_names(path,files_names):
   
    for file in path.iterdir():
        
        if file.is_file():
            files_names.append(file)
        else:
            read_files_names(file, files_names)
                   
    return files_names



if __name__ == '__main__':
    sort(path)
