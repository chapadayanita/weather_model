import csv
import numpy as np

def read_temperature_data(filename):
    time = []
    temp = []
    
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            time.append(float(row['Time']))
            temp.append(float(row['Temperature']))
    
    return np.array(time), np.array(temp)

