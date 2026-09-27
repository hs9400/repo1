def check_range(device):
    """
        Description:
            This function accecpts a device as a parameter and
            returns the normal range of power consumption.
        Parameters:
            device (string) - User input device name
        Returns:
            Normal operating range of provided device.
    """
    if device == 'LED Light':
        print('normal range is 0.01 - 0.10 kWh')
        return [0.01,0.10]
    elif device == 'Television':
        print('normal range is 0.05 - 0.50 kWh')
        return [0.05,0.50]
    elif device == 'Refrigerator':
        print('normal range is 0.10 - 1.50 kWh')
        return [0.10,1.50]
    elif device == 'Washing Machine':
        print('normal range is 0.30 - 2.50 kWh')
        return [0.30,2.50]
    elif device == 'Air Conditioner':
        print('normal range is 0.50 - 5.00 kWh')
        return [0.50,5.00]
    else:
        print('Unknown Device!')

def energy_status(range,energy_consumption):
    """
        Description:
            The function takes a device and its energy 
            consumption and returns if it is normal,high or critical.
            where high is upto 20% higher and critical is 50% higher  
        Parameters:
            range (list) - it is the list of the devices normal energy range. 
            energy_comsumption (float) - given energy consumed by the device
        Returns:
            string, if the energy consumption of the device is within normal, high or critical range.  
    """

    critical=range[-1]+((range[-1]*50)/100)
    high=range[-1]+((range[-1]*20)/100)
    if energy_consumption>=critical:
        return 'Reading is Critical'
    elif energy_consumption>=high:
        return 'Reading is High'
    elif energy_consumption>=range[0] and energy_consumption<=range[1]:
        return 'Reading is Normal'
    else:
        return 'Reading is Low/Invalid'

    
print(energy_status([0.05,0.50],0))


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
    if status =="Reading is High" or status== " Reading is Critical" or status=="Reading is Low/Invalid":
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
        return print("URGENT ATTENTION NEEDED! Extreme power spike detected. Disconnect Immediately!")
    else:
        return print("Invalid entry.")
    

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