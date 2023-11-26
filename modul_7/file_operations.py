def file_operations(path, additional_info, start_pos, count_chars):

    with open(path, 'a') as file:
        file.write(additional_info)

    with open(path, 'r') as file:
        file.seek(start_pos)
        return file.read(count_chars)


path = '/users/aleksandr.voitushenko/desktop/goit/pythoncore/modul_7/test.txt'
additional_info = 'Hello World!\n'
start_pos = 3
count_chars = 5
print(file_operations(path, additional_info, start_pos, count_chars))
      
