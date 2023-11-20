from re import sub

text = '''
t is used for:

web development (server-side),
software development,
mathematics,
system scripting.
What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.

'''

#sym_to_exclude = ('.',',', '!', ':', '?')

reg_exp = r'[^a-zA-Z0-9 ]'
normalized_text = text.lower()
normalized_text = sub(reg_exp, '', normalized_text)

words_list = normalized_text.split()
unique_words_list = set(words_list)

n_words = len(words_list)
n_unic_words = len(set(words_list))

words_quantity = {}

for word in unique_words_list:
    words_quantity[word] = normalized_text.count(word)

words_quantity_list = list(words_quantity.items())

def sort_by_quantity(elements):
    return elements[1]

words_quantity_list.sort(key = sort_by_quantity, reverse = True)

