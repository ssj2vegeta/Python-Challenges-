vendingmachine = {"chips":50,"cola":25,"chocolate":100,"ice cream": 65}
print(vendingmachine)
input2 = input("what would you like?")
money = 0
f = vendingmachine[input2]
print(f"the price is {f}")
change = 0
while money < f:
    input1 = int(input("how much money would you like to add??"))
    money = money + input1
    change = money - f
print(f"the product is {input2} and the change is {change} ")
