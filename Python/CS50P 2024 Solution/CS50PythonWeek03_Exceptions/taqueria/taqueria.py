#form a table in dic form
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#can use _ here????????????????? just kdding
TotalCost = 0
#use loop attempt 1
while True:
    try:
        item = input("Item: ").lower().title()
        if item not in menu:
           raise Exception

    except EOFError:
        break
    except:
        continue
    else:
        TotalCost += menu[item]
        print(f"Total : ${TotalCost:.2f}")
