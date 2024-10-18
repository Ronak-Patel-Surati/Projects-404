# take cokebill amount
# fixed price of coke is 50
fp = 50
amtd = fp
while amtd > 0:
    print("Amount Due: " + str(amtd))
    coin = int(input("Amount Due: "))
    if coin in [25, 10, 5]:
        amtd -= coin
if amtd < 0:
    amtd = -amtd
print("Change Owed: " + str(amtd))
