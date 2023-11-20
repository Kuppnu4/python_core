def format_string(string, length):
    if len(string) >= length:
        return(f"string=\'{string}\'")
    else:
        for i in range((length - len(string) - 1)//2):
                string = ' ' + string
                
        return(f"string=\'{string}\'")

a = format_string("aaaaaaaaaaaaaaaaac", 12)
b = format_string(length = 15, string = 'abaa')
print(a)
print(b)


def cost_delivery(quantity, *_, discount=0):
    
"""Функція повертає суму за доставлення замовлення.

     Перший параметр &mdash; кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0.
"""

    
    
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result
