import re
def is_spam_words(text, spam_words, space_around=False):
    is_spam = False
    text = text.lower()
    
    if not space_around:
        for w in spam_words:
            if text.count(w) > 0:
                print(w)
                is_spam = True

    else:
        reg1 = r'\b'
        for w in spam_words:
            regexp = rf'{reg1}{w}{reg1}'
            if re.search(regexp, text):
                
                print(text)
                is_spam = True

            
    
    return is_spam
        
    



spam_words = [
    'buy', 'sell', 'sale', 'chance'
    ]

spam = is_spam_words('you have a sale.', spam_words, True)
print(spam)
