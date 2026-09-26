# create range

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
    

def main():
    device=str(input('enter device name: '))
    x=check_range(device)

    EC=float(input('enter energy comsumption of device: '))
    y=energy_status(x,EC)