# telephone number 0123456789

from re import search

reg_exp = r'^\+?(38)?8?[- (]*0\d{2}[- )]?\d{3}[- ]?\d{2}[- ]?\d{2}$'

phone_numbers = [
            '0631231212',
            '+380631231212',
            '380631231212',
            '063 123 12 12',
            '(063)123 12 12',
            '+38 (063)123 12 12',
            '010101001',
            '0998899009',
            '858585858888',
            '39988990000009',
            '+390631231212',
            '+30631231212',
            '80631231212'
    ]


for number in phone_numbers:
    
    result = search(reg_exp, number)
   

    if result is None:
        print(f'NOT a phone Number - {number}')
    else:
        print(f'GOOD phone Number - {result.group()}')

    
