from pathlib import Path

Path()
#PosixPath('.')

my_path = Path('Users//aleksandr.voitushenko//Desktop//GoIT//')
print(my_path)
#PosixPath('Desktop/GoIT')

parent = my_path.parent
print(parent)
#PosixPath('Desktop')

name = my_path.name
print(name)
#'GoIT'

my_path = Path('//Users//aleksandr.voitushenko//Desktop//GoIT//PythonCore//modul4//practice.py')
print(my_path.suffix)
#.py

b = my_path.exists()
print(b)

d = my_path.is_dir()
print(d)

f = my_path.is_file()
print(f)

my_path = Path('//Users//aleksandr.voitushenko//Desktop//GoIT//PythonCore//modul4//')
for i in my_path.iterdir():
    print(i)
