import re

def sanitize_file(source, output):
    regexp = r'\d+'
    san_text = ''
    
    with open(source, 'r') as initial_file:
        init_text = initial_file.read()
        san_text = re.sub(regexp, '', init_text)
        print(san_text)

    with open(output, 'w') as san_file:
        san_file.write(san_text)






sanitize_file('source', 'output')
