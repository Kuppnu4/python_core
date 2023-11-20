import shutil
from pathlib import Path

'''
for shortcut, description in shutil.get_archive_formats():#to see all the formats of archives
    print('{:<10}|{:<10}'.format(shortcut, description))
'''

def create_backup(path, file_name, employee_residence):
    with open(f'{path}/{file_name}', 'wb') as file:
        for name, country in employee_residence.items():
            file.write(f'{name} {country}\n'.encode('utf-8'))

    archive_path = shutil.make_archive('backup_folder', 'zip', path)
    
    return archive_path
    

def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)




path = Path.cwd()
path_to_unpack = Path('/Users/aleksandr.voitushenko/Desktop/GoIT/PythonCore/zip_test')
file_name = 'employee_residence_backup_file'
employee_residence = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}

archive_path = create_backup(path, file_name, employee_residence)
print(archive_path)

unpack(archive_path, path_to_unpack)


