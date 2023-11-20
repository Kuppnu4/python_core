result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        result = int(input())
        wait_for_number = False
        break
    except ValueError:
        print (f"\'{result}\' is not a number, try again ")

while True:

    inpt = input()
    
    if wait_for_number: 
        try:
            operand = int(inpt)
            if operator == "+":
                result += operand    
            elif operator == "-":   
                result -= operand    
            elif operator == "*":   
                result *= operand  
            elif operator == "/":  
                result /= operand
            wait_for_number = False
            continue
        except ValueError:
            print(f"{inpt} is not a number")


    else:
        try:

            operator = inpt
            if operator == "=":
                print(f"Result is: {result}")
                break
            elif operator != "+" and operator != "-" and  operator != "*" and  operator != "/":
                raise ValueError()
            else:
                wait_for_number = True
                continue
    
        except ValueError:
            print(f"\'{operator}\' is not '+' or '-' or '/' or '*'. Try again")


        

        
