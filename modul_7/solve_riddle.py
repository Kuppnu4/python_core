def solve_riddle(riddle, word_length, start_letter, reverse=False):
    
    search_word = ''
    
    for letter in riddle:
        if letter == start_letter:

            if reverse:
                search_word = riddle[riddle.index(letter):riddle.index(letter) - word_length:-1]
            else:
                search_word = riddle[riddle.index(letter):riddle.index(letter) + word_length]
            
            return search_word
    return search_word




print(solve_riddle('mi1powperet', 3, 'r', True))


'''
riddle - строка с зашифрованным словом.
word_length - длина зашифрованного слова.
start_letter - буква, с которой начинается слово
(подразумевается, что до начала слова буква не встречается в строке).
'''
