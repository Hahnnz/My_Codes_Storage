import numpy as np

def MinMaxScaler(data):
    minval=np.min(data,0)
    maxval=np.max(data,0)
    numerator = data - minval
    denominator = maxval - minval
    return numerator/ (denominator + 1e-8), minval, maxval
    
def UnMinMaxScaler(data, minval, maxval):
    return data * (maxval-minval+1e-8)+minval
