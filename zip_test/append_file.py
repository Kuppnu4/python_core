def add_employee_to_file(record, path):
    fh = open(path, 'a')
    fh.write('\n' + record)
    fh.close()



record = 'Alex, 35'
path = 'employees'
add_employee_to_file(record, path)
