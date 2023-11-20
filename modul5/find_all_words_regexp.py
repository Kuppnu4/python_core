import re

def find_all_words(text, word):

    
    return re.findall(rf'\b{re.escape(word)}\b', text, re.IGNORECASE)

text = "Guido van Rossum began working on Python in the late 1980s,"\
        " as a successor to the ABC programming language,"\
        " and first released it in 1991 as Python 0.9.0."
word = 'python'

print(find_all_words(text, word))
