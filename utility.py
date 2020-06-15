import numpy as np
from pandas import read_csv

def load_dataset(file):
    dataset = read_csv(file,header=None)
    dataset = dataset.values.astype(str)
    x = dataset[:,2:].astype(float)
    y = dataset[:,1] == 'M'
    return x,y