#tasks
#num inputs
#operation input
#magic of match ?

#num inputs
Cal = input("please enter your equation :")

Num1, optr, Num2 = Cal.split()
# as demo has input as a single line

Num1 = float(Num1)
Num2 = float(Num2)

match optr:
    case "+":
        print(Num1+Num2)
    case "-":
        print(Num1-Num2)
    case "/":
        print(Num1/Num2) #ignore 0
    case "*":
        print(Num1+Num2) #ignore 0
    case _:
        print("ENTER PROPERLY MY DEAR CHILD")
