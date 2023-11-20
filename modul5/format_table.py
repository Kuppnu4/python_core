grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    students_list = []
    n = 1
    for k, v in students.items():
        
        line = '{:>4}|{:<10}|{:^5}|{:^5}'.format(n, k, v, grades[v])
        students_list.append(line)
        n += 1

    return students_list



students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
#print(formatted_grades(students))
for el in formatted_grades(students):
    print(el)
