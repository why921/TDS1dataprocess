import glob
import netCDF4 as nc
from netCDF4 import Dataset
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import os


b = np.load("E:\GNSSR_DATA\TDS-1\DDM_numpy\\201804\\30\H00\\000000.npy")
print(b.shape)

file = open("E:\GNSSR_DATA\TDS-1\DDM_numpy\DStest\pa.txt",'w')
for i in range(10):
    a=b[i,:,:]
    print(a)
    np.save('E:\GNSSR_DATA\TDS-1\DDM_numpy\DStest\\'+'a'+str(i), a, allow_pickle=True, fix_imports=True)
    file.write('E:\GNSSR_DATA\TDS-1\DDM_numpy\DStest\\' + 'a' + str(i)+ '.npy'+' '+'1' + "\n")
