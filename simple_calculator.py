num1 = float(input("first number: "))
operator = (input("your operator: "))
num2 = float(input("second number: "))

if operator == "+" :
    print(num1 + num2)
elif operator == "-" :
    print(num1 - num2)
elif operator == "*" :
    print(num1*num2)
elif operator == "/" :
    if num2 == 0:
        print("cannot divide by zero")
    else :
        print(num1/num2) 
elif operator == "per" : # (per) here is symbol of percentage because "%" this is symbol of modulo
    print((num1/num2)*100)
else :
    print("the program is invalid")  
    
    