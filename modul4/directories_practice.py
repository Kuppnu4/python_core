
from pathlib import Path
def parse_folder(path):
    
    
    files = []
    folders = []

    for i in path.iterdir():
        if i.is_file():
            files.append(i.name)
        if i.is_dir():
            folders.append(i.name)
        
            
    print(files, folders)
            
    return files, folders

parse_folder(Path("/Users/aleksandr.voitushenko/Desktop/GoIT/"))
