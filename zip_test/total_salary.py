import sys
import re

def total_salary(path):

    fh = open(path, 'r')
    team = []
    while True:
        line = fh.readline()
        if not line:
            break
        team.append(line)

    fh.close()
    
    regexp = r'\d+'
    summ = 0.00
    
    for m in team:
        salary = re.search(regexp, m)
        
        summ += float(salary.group())

    print(summ)
    return summ
        


total_salary('new_file')
