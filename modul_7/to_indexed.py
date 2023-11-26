def to_indexed(source_file, output_file):

    lines_list = []
    i = 0
    with open(source_file, 'r') as source:
       
        
        while True:
            
            in_line = source.readline()
            if not in_line:
                break
            lines_list.append(f'{i}: ' + in_line)
            i += 1

    with open(output_file, 'a') as output:
        for l in lines_list:
                
            output.write(l)

           

source_file = '/users/aleksandr.voitushenko/desktop/goit/pythoncore/modul_7/test.txt'
output_file = '/users/aleksandr.voitushenko/desktop/goit/pythoncore/modul_7/test copy.txt'
to_indexed(source_file, output_file)
