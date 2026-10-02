
# TASK 1

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
        return "Unknown Device!"
    
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
    elif energy_consumption>range[-1] and energy_consumption<=critical:
        return 'Reading is High'
    elif energy_consumption>=range[0] and energy_consumption<=range[1]:
        return 'Reading is Normal'
    else:
        return 'Reading is Low/Invalid'

def attention(status):
    '''
    Description:
        The function evaluates whether a device requires attention based on its
        status.
    Parameters:
        status (str) - 'Normal, 'High', or 'Critical'
    Returns:
        bool - True if attention is required, otherwise False
    '''
    if status =="Reading is High" or status== "Reading is Critical" or status=="Reading is Low/Invalid":
        return True
    else:
        return False
    
#TASK 2

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

#TASK 3

def feedback(device, status):
    '''
    Description:
        The function analyzes and provides feedback on Homesystem devices based on type of device and status.
    Parameters:
        device(str) - Type of Device
        status(str) - status of device (High/Normal/Critical)
    Returns:
        feedback as string
    '''    
    if status=="Reading is Normal":
        return "Device is operating efficiently. No action needed."
    elif status=="Reading is High":
        if device=="Refrigerator":
            return "Check for damage and temperature controls."
        elif device=="Air Conditioner":
            return "Check for damage and operating duration."
        elif device == "Washing Machine":
            return "Check controls and operating efficiency."
        else:
            return 'Energy consumption is high check device.'
    elif status=="Reading is Critical":
        return "URGENT ATTENTION NEEDED! Extreme power spike detected. Disconnect Immediately!"
    else:
        return "Invalid entry."

#TASK 4 
   
def report():
    readings=[['LED Light',0.06],['LED Light',0.18],['Television',0.32],['Television',1.20],
          ['Refrigerator',0.80],['Refrigerator',2.20],['Washing Machine',1.40],['Washing Machine',4.50],
          ['Air Conditioner',2.80],["Fan",0.20],['Air Conditioner',7.50],["Television",0.05],
          ["LED Light",0.10],["Air Conditioner",5.05],["Refrigerator",2.00],["LED Light",0.00],
          ["Washing Machine",-0.30]]

    num=0
    total_energy_consumption=0
    normal=0
    high=0
    critical=0

    for reading in readings:
        
        num+=1
        total_energy_consumption+=reading[1]
        print('DEVICE: ',reading[0])
        print('ENERGY CONSUMPTION: ',reading[1],'kWh')

        energy_range=check_range(reading[0])
        
        if energy_range == "Unknown Device!":
            print()
            continue

        status=energy_status(energy_range,reading[1])

        if status =="Reading is Normal":
            normal+=1
        elif status=="Reading is High":
            high+=1
        elif status== "Reading is Critical":
            critical+=1

        needs_attention = attention(status)
        if needs_attention:
            print('ATTENTION REQUIRED!')
        else:
            print('Device is functioning normally. Attention not required.')
        
        print('DEVICE STATUS: ', status)
        if status == "Reading is Low/Invalid":
            print()
            continue

        energy_rate=0.3
        print('ENERGY COST: ',energy_cost(reading[1],energy_rate),'AED/kWh')
        print('FEEDBACK: ',feedback(reading[0],status))

        print()

#TASK 5 & 6
    print('~~~REPORT~~~')
    print('Number of Readings: ',num)
    print('Normal: ',normal)
    print('High: ',high)
    print('Critical: ',critical)

    print()
    print('Readings requiring attention: ',high+critical)

    energy_rate=0.3
    print('Total Energy: ', total_energy_consumption)
    print('Estimated Cost: ',total_energy_consumption*energy_rate)
    print()

    highest_consumption=0.00
    highest_consumption_device=''
    for reading in readings:
        if reading[1]>highest_consumption:
            highest_consumption_device=reading[0]
            highest_consumption=reading[1]
    print('Highest consumption: ')
    print(highest_consumption_device,'-',highest_consumption )

def main():
    report()
main()





    

    
    
   




