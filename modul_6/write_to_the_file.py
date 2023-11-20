def write_employees_to_file(employee_list, path):
    new_list = []
    
    for e in employee_list:
        if isinstance(e, list):
            unpack_list(e, new_list)
            
        else:
            new_list.append(e)
        print(new_list)

    fh = open(path, 'w')
    for employee in new_list:
        print(employee)
            
        fh.write(employee)
        fh.write('\n')
    fh.close()
            
    
def unpack_list(row_list, new_list):
    
    for e in row_list:
        if isinstance(e, list):
            unpack_list(e, new_list)
            
        else:
            new_list.append(e)



employee_list = [['Robert Stivenson,28', 'Alex Denver,30', ['Robert Stivenson2,28', 'Alex Denver2,30']], 'Drake Mikelsson,19']
write_employees_to_file(employee_list, 'employees')
