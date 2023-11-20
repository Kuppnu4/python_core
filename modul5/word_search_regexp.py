import re

def find_word(text, word):
    find_result = {}
    find_text = text.lower()
    find_word = word.lower()
    m = re.search(rf'\b{re.escape(find_word)}\b', find_text)

    if m:
        find_result['result'] = True
        find_result['first_index'] = m.span()[0]
        find_result['last_index'] = m.span()[1]
        find_result['search_string'] = word
        find_result['string'] = text
    else:
        find_result['result'] = False
        find_result['first_index'] = m
        find_result['last_index'] = m
        find_result['search_string'] = word
        find_result['string'] = text
        
    for i in find_result:
        print(i, find_result[i])



text = "Guido van Rossum began working on Python in the late 1980s,"\
        " as a successor to the ABC programming language,"\
        " and first released it in 1991 as Python 0.9.0."
word = 'pyton'

find_word(text, word)
    
