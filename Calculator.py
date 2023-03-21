"""           #####   CALCULATOR   #####           """

while True:
    print("                ### TWO INPUT CALCULATOR ###                ")

    x=input("\nEnter opreation as add,sub,mul,div,modulo,floor_div,power:")
    y=int(input("Enter first number:"))
    z=int(input("Enter second number:"))

    match x:
        case "add":
            print("result=",y+z)
        case "sub":
            print("result=",y-z)
        case "mul":
            print("result=",y*z)
        case "div":
            print("result=",y/z)
        case "modulo":
            print("result=",y%z)
        case "floor_div":
            print("result=",y//z)
        case "power":
            print("result=",y**z)
        case _:
            raise ValueError("You have given an invalid input\n Please restart for using")

                          
    a=int(input("To continue operations Enter \"1\", to end Enter \"0\"\n"))

    if a==1:
        continue
    elif a==0:
        break
    else:
        raise ValueError("You have given an invalid input\n Please restart for using")

print(":-)(-:")