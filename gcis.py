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
    elif device == 'Refrigerator':
        print('normal range is 0.10 - 1.50 kWh')
    elif device == 'Washing Machine':
        print('normal range is 0.30 - 2.50 kWh')
    elif device == 'Air Conditioner':
        print('normal range is 0.50 - 5.00 kWh')
    else:
        print('Unknown Device!')
    normal_range=False
    high_range=False
    critical_range=False

c=(check_range('LED Light'))
print(type(c))