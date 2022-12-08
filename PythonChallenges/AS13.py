revenue = int(input(" what is total revenue?"))
cogs = int(input("what is the cost of goods sold?"))
expenses = int(input("what is the total expenses?"))

print(f" the gross profit is {(revenue - cogs)} and the net profit is {revenue - cogs - expenses}")
print(f"the gross profit margin is {((revenue - cogs)/revenue) * 100}% and the net profit margin is {(((revenue - cogs)/revenue)-expenses/revenue) * 100}%")

if ((revenue - cogs)/revenue) * 100 > 50:
    print("this business has a good gross profit margin")
elif ((revenue - cogs)/revenue) * 100 < 50:
    print("this business has a bad gross profit margin")

if (((revenue - cogs)/revenue)-expenses/revenue) * 100 > 20:
    print("this business has a good net profit margin")
elif (((revenue - cogs)/revenue)-expenses/revenue) * 100 < 20:
    print("this business has a bad net profit margin")
