def sequence_buttons(string):
    
    SYMBOLS = ('.', ',', '?', '!', ':', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z', ' ')

    NUMBERS = ('1', '11', '111', '1111', '11111', '2', '22', '222', '3', '33', '333',
               '4', '44', '444', '5', '55', '555', '6', '66', '666',
               '7', '77', '777', '7777', '8', '88', '888', '9', '99', '999', '9999', '0'
               )
    

    TRANSLATE_DICT = {}

    for s, n in zip(SYMBOLS, NUMBERS):
        TRANSLATE_DICT[ord(s)] = n
        TRANSLATE_DICT[ord(s.lower())] = n

    return string.translate(TRANSLATE_DICT)

print(sequence_buttons("Hello, World!"))
