import re
def token_parser(s):
    tokens = []
    digit_str = ''
    i = 0
    
    for t in s:
        i += 1
        
        if t == ' ':
            if digit_str:
                tokens.append(digit_str)
                digit_str = ''
            continue

        elif re.compile(r'\d').match(t):
            
            digit_str += t
            if i == len(s):
                tokens.append(t)
                
            
        elif t == '+' or t == '-' or t == '*' or t == '/' or t == '(' or t == ')':
            
            if digit_str:                
                tokens.append(digit_str)
                digit_str = ''
            tokens.append(t)

    return tokens



print(token_parser('2+ 34 + 234 -5 * 3'))
