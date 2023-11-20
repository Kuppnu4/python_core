import sys
from pathlib import Path

path = sys.argv[1]



def sort(path):
    dir_path = Path(path).absolute()
    print(dir_path)
    


sort(path)
