import netCDF4 as nc
from netCDF4 import Dataset
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
from osgeo import gdal

DDMs_path = r'E:\GNSSR_DATA\TDS-1\L1B\2018-12\01\H00\DDMs.nc'
metadata_path = r'E:\GNSSR_DATA\TDS-1\L1B\2018-12\01\H00\metadata.nc'

DDMs_dataset = Dataset(DDMs_path)
for group_name in DDMs_dataset.groups:
    group1 = DDMs_dataset.groups[group_name]
    a=group_name

DDMe = group1.variables['DDM'][:].data
c=DDMe.transpose(2,1,0)
img=c[:,:,20]
plt.imshow(img)

np.save('test.npy', c, allow_pickle=True, fix_imports=True)
