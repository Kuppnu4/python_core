import os
import re
import shutil
from pathlib import Path

path = '/Users/aleksandr.voitushenko/desktop/trash/mygame'
ds_store_path = '.DS_Store'

for file in Path(path).iterdir():
    print(file)

images_dir = os.path.join(path, 'images')
videos_dir = os.path.join(path, 'videos')
docs_dir = os.path.join(path, 'documents')
music_dir = os.path.join(path, 'music')
archives_dir = os.path.join(path, 'archives')
unknown_files_dir = os.path.join(path, 'my_own_files')

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
    
for root, dirs, files in os.walk(path, topdown = False):
    
    for d in dirs:
        print(d)
        print('FILES')
        print(files)
        if file == ds_store_path:
            print(file)
            os.remove(Path(file).absolute())
        print(files)
        folder_path = os.path.join(root, d)
        print(os.listdir(folder_path))
        if not any(os.listdir(folder_path)):
            os.rmdir(folder_path)
