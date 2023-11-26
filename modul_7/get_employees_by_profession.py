def get_employees_by_profession(path, profession):

    employees_list = []
    new_list = []
    with open(path, 'r') as file:

        while True:
            line = file.readline()
            if not line:
                break
            elif line.find(profession) != -1:
                employees_list.append(line)
            else:
                continue

        for e in employees_list:
            
            new_list.append(e.replace('\n', '').replace(' ', ''))
            
        new_str = ' '.join(new_list)

        new_str = new_str.replace(profession, '')
        print(new_str)

        

    return new_str



path = '/users/aleksandr.voitushenko/desktop/goit/pythoncore/modul_7/test.txt'
profession = 'courier'
get_employees_by_profession(path, profession)
