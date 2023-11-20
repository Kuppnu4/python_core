import re


def replace_spam_words(text, spam_words):

    

    for word in spam_words:
        
        text = re.sub(rf'\b{re.escape(word)}\b', '*'*len(word), text, flags = re.IGNORECASE)

    return text

spam_words = [
    'buy', 'sell', 'sale', 'chance', 'you'
    ]

text = 'you Have a Sale.'
print(replace_spam_words(text, spam_words))
