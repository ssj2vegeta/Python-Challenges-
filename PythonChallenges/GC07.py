import random

balance = random.randint(1000,10000)
print(f"your bank balance is {balance}")
while True:
    withdrawal = int(input("how much money do you want to withdraw?"))
    if withdrawal % 5 == 0 and withdrawal < balance:
        balance  = balance - withdrawal - 0.5
        break
    else:
        print("the withdrawal amount is not a multiple of 5 or you are withdrawing more than your balance ")

print(f"your withdrawal amount is {withdrawal} and your remaining bank balance after a transaction fee of 0.5$ is {balance}")
