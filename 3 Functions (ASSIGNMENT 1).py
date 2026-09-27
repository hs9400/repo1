def attention(status):
    '''
    Description:
    The function evaluates whether a device requires attention based on its
    status.
    Parameters:
    status (str): 'Normal, 'High', or 'Critical'
    Returns:
    bool: True if attention is required, otherwise False
    '''
    if status =="Reading is High" or status== "Reading is Critical" or status=="Reading is Low/Invalid":
        return True
    else:
        return False

def energy_cost(energy_consumption, electricity_rate):
    '''
    Description:
    The function calculates the estimated electricity cost (AED) based on 
    energy consumption and electricity rate
    Parameters:
    energy_consumption(float): Energy consumed in kWh
    electricity_rate(float): rate of electricity (cost) in AED per kWh
    Returns:
    cost(float): Estimated cost of energy consumption in AED
    '''
    if energy_consumption <0 or electricity_rate<0:
        print("Invalid entry!")

    cost= energy_consumption*electricity_rate
    return cost


def feedback(device, status):
    '''
    Description:
    The function analyzes and provides feedback on Homesystem devices based on type of device and status.
    Parameters:
    device(str): Type of Device
    status(str): status of device (High/Normal/Critical)
    Returns:
    feedback as string
    '''    
    if status=="Reading is Normal":
        return "Device is operating efficiently. No action needed."
    elif status=="Reading is High":
        if device=="Refrigerator":
            return print("Check for damage and temperature controls.")
        if device=="Air Conditioner":
            return print("Check for damage and operating duration.")
        if device == "Washing Machine":
            return print("Check controls and operating efficiency.")
    elif status=="Reading is Critical":
        return ("URGENT ATTENTION NEEDED! Extreme power spike detected. Disconnect Immediately!")
    else:
        return ("Invalid entry.")
    

def main():
    device=str(input('enter device name: '))
    x=check_range(device)

    energy_consumption=float(input("Enter energy consumption in kWh: "))
    electricity_rate=float(input("Enter electricity rate in AED/kWh: "))

    y=energy_status(x,energy_consumption)
    needs_attention = attention(y)
    cost = energy_cost(energy_consumption, electricity_rate)
    fb = feedback(device, y)

    print(y)
    print("Attention required:", needs_attention)
    print("Cost:", cost)
    print("Feedback:", fb)


main()