import netCDF4 as nc
from netCDF4 import Dataset
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import os

#E:\GNSSR_DATA\TDS-1\L1B\2018-12\01\H00




def DDMs(DDMs_path, numpy_path):
    DDMs_dataset = Dataset(DDMs_path)
    for group_name in DDMs_dataset.groups:
        group1 = DDMs_dataset.groups[group_name]
        DDMe = group1.variables['DDM'][:].data
        DDMe.transpose(2, 1, 0)
        path=numpy_path+'\\'+group_name+'.npy'
        np.save(path, DDMe, allow_pickle=True, fix_imports=True)



def lonlat(meta_path, lonlat_path):
    metadata_dataset = Dataset(meta_path)
    for group_name in metadata_dataset.groups:
        group2 = metadata_dataset.groups[group_name]
        lat=group2.variables['SpecularPointLat'][:].data
        lon=group2.variables['SpecularPointLon'][:].data
        lonlat=np.array([lon, lat])
        path=lonlat_path+'\\'+group_name+'.npy'
        np.save(path, lonlat, allow_pickle=True, fix_imports=True)



if __name__ == "__main__":
    Year = '2018'
    Month = '12'
    Day = '01'
    Product = 'H00'
    dir_ddm='E:\GNSSR_DATA\TDS-1\DDM_numpy\\'+Year+Month+'\\'+Day+'\\'+Product
    dir_lonlat='E:\GNSSR_DATA\TDS-1\lonlat_numpy\\'+Year+Month+'\\'+Day+'\\'+Product
    if not os.path.isdir(dir_ddm):
        os.makedirs(dir_ddm)
    if not os.path.isdir(dir_lonlat):
        os.makedirs(dir_lonlat)
    DDMs_path = r'E:\GNSSR_DATA\TDS-1\L1B\\'+Year+'-'+Month+'\\'+Day+'\\'+Product+'\\'+'DDMs.nc'
    metadata_path = r'E:\GNSSR_DATA\TDS-1\L1B\\'+Year+'-'+Month+'\\'+Day+'\\'+Product+'\\'+'metadata.nc'
    DDMs(DDMs_path,dir_lonlat)
    lonlat(metadata_path, dir_lonlat)