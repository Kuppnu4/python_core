def write_employees_to_file(employee_list, path):
    fh = open(path, 'r')
    while True:
        line = fh.readline()
        if not line:
            break
        else:



employee_list = [
        'Asdfff, ssd',
        'Svgfhfk, 37',
        'Wjfjfjfjjf, 33'
        ]
write_employees_to_file(employee_list, path)
