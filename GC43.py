print("calculator for voltage ( V = IR ) ")
input1 = input("which one do you want to solve for? current, resistance or voltage")
resistance = 0
voltage = 0
current = 0
if input1 == "current":
    resistance = int(input("whats your resistance?"))
    current = int(input("whats your current?"))
    voltage = resistance * current
    print(f"the voltage is {voltage} volts")
elif input1 == "resistance":
    voltage = int(input("whats your voltage?"))
    current = int(input("whats your current?"))
    resistance = voltage / current
    print(f"the resistance is {resistance} ohms")
elif input1 == "current":
    resistance = int(input("whats your resistance?"))
    voltage = int(input("whats your voltage?"))
    current = voltage / resistance
    print(f"the current is {current} amps")
else:
    print("invalid input")
