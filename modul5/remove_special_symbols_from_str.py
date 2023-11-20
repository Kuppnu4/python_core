import re
def real_len(text):
  
    clean_text = re.sub(r'[\n\f\r\t\v]', '', text)
    print(len(re.sub(r'[\n\f\r\t\v]', '', text)))

real_len('jsjsjsjj\njdj\fkdkd\rkdkdk\tkkdkd\v')
