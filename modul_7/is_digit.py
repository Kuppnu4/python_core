import re
def is_integer(s):

    s = s.strip()
    regexp = re.compile(r'((\+|-)\d+)')

    if len(s) == 0:
        return False

    
    elif regexp.match(s):
        return True

    else:
        return False

print(is_integer('  -34  '))
