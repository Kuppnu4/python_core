import re


def find_all_emails(text):
    result = re.findall(r"[a-zA-Z]{1}[\w._]{1,}@[\w]+[.]{1}[\w]{2,}", text)
    return result


text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org '\
        'first.middle.last@iana.or a@test.com abc111@test.com.net'

print(text)
print(find_all_emails(text))
