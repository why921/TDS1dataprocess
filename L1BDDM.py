import netCDF4 as nc
from netCDF4 import Dataset
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import os

#E:\GNSSR_DATA\TDS-1\L1B\2018-12\01\H00




def DDMs(path):
    DDMs_dataset = Dataset(path)
    for group_name in DDMs_dataset.groups:
        group1 = DDMs_dataset.groups[group_name]
    return group1


def lonlat(path):
    metadata_dataset = Dataset(path)
    for group_name in metadata_dataset.groups:
        group2 = metadata_dataset.groups[group_name]



if __name__ == "__main__":
    DDMs_path = r'E:\GNSSR_DATA\TDS-1\L1B\2018-12\01\H00\DDMs.nc'
    metadata_path = r'E:\GNSSR_DATA\TDS-1\L1B\2018-12\01\H00\metadata.nc'
    print(DDMs(DDMs_path))