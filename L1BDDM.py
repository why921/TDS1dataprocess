import netCDF4 as nc
from netCDF4 import Dataset
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import os

#E:\GNSSR_DATA\TDS-1\L1B\2018-12\01\H00

DDMs_path = r'E:\GNSSR_DATA\TDS-1\L1B\2018-12\01\H00\DDMs.nc'

DDMs_dataset = Dataset(DDMs_path)
for group_name in DDMs_dataset.groups:
    group1 = DDMs_dataset.groups[group_name]


metadata_path=r'E:\GNSSR_DATA\TDS-1\L1B\2018-12\01\H00\metadata.nc'
metadata_dataset = Dataset(metadata_path)
for group_name in metadata_dataset.groups:
    group2 = metadata_dataset.groups[group_name]
