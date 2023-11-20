import re

def save_applicant_data(source, output):
    
    with open(output, 'w') as abitur_base:
        for abiturient in source:
            abitur_info = ''
            for k, v in abiturient.items():
                abitur_info += str(v) + ','
                
            abitur_info = abitur_info.removesuffix(',')

            abitur_base.write(abitur_info + '\n')


abiturients = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]


save_applicant_data(abiturients, 'output')
