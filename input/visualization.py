import matplotlib.pyplot as plt
import pandas as pd
import os

# fileName = os.listdir('MTA_Tracking')

fileName = ['NYCT_4207.csv',
            'NYCT_4713.csv',
            'NYCT_4783.csv',
            'NYCT_4840.csv',
            'NYCT_4862.csv',
            'NYCT_5038.csv',
            'NYCT_5039.csv',
            'NYCT_5222.csv',
            'NYCT_5242.csv',
            'NYCT_5312.csv',
            'NYCT_5351.csv',
            'NYCT_5627.csv',
            'NYCT_6029.csv',
            'NYCT_6518.csv',
            'NYCT_6565.csv',
            ]

for i in fileName:
    print(i)
    data = pd.read_csv('MTA_Tracking/' + i)
    plt.plot(data['VehicleLocation.Longitude'],
             data['VehicleLocation.Latitude'], '-')
# data = pd.read_csv("norm/NYCT_4207.csv")
plt.savefig('test.png')
