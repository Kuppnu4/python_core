import re
HEADER = "HEADER"
# comand: add/remove
# item: contains digits only
# amount: contain digits only
#
# $command $item $amount
def add(*args):
    print('add')

def remove():
    print('remove')


def regexp_check(*args):
    
    pattern = r"^(add|remove) [a-zA-Z]+ \d+$"
    user_string = " ,".join(args)

    return True if re.match(pattern, user_string)  is not None else False
       


def classic_check():
    if command != 'and' or command != 'or':
        return None

    if not item.isalpha:
        return None

    if not amount.isdigit():
        return None
    
    return True


def parse_input(sequence, check):
    tokens = sequence.split(" ")
    
    if len(tokens) != 3:
        return None
    
    command, item, amount = tokens

    result = check_callback(*tokens)

    if not result:
        return None

    print("Hello")


def main():

    while True:
       
        sequence = input(">>> ")

        if sequence == "exit":
            print('Good buy')
            continue
            
        parsing_result = parse_input(sequence, regexp_check)
        
        

        if parse_input == None:
            print("Wrong comand format")
            continue

        print(parsing_result)


if __name__ == "__main__":
    main()
