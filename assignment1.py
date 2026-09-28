def device():
    choice = 0
    choice = input("Enter your choice: ")
    if choice == 'LED Light':
        print("Minimum normal energy consumption is 0.01 kWh")
        print("Maximum normal energy consumption is 0.10 kWh")

    elif choice == 'Television':
        print("Minimum normal energy consumption is 0.05 kWh")
        print("Maximum normal energy consumption is 0.50 kWh")\

    elif choice == 'Refrigerator':
        print("Minimum normal energy consumption is 0.10 kWh")
        print("Maximum normal energy consumption is 1.50 kWh")

    elif choice == 'Washing Machine':
        print("Minimum normal energy consumption is 0.30 kWh")
        print("Maximum normal energy consumption is 2.50 kWh")

    elif choice == 'Air Condition':
        print("Minimum normal energy consumption is 0.50 kWh")
        print("Maximum normal energy consumption is 5.00 kWh")

#device()

def analysis():
    energy = float(input("Enter your energy consumption in kWh : "))
    if 0.10 >= energy >= 0.01:
        print("The device is a LED Light") 

    elif 0.50 >= energy >= 0.05:
        print("The device is a Television")

    elif 1.50 >= energy >= 0.10:
        print("The device is a Refrigerator")

    elif 2.50 >= energy >= 0.30:
        print("The device is a Washing Machine") 

    elif 5.00 >= energy >= 0.50:
        print("This device is an Air Conditioner")
    
#analysis()

def status(device, energy_consumption):
    if















