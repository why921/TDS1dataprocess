import netCDF4 as nc
from netCDF4 import Dataset
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

lonlat=np.load("E:\GNSSR_DATA\TDS-1\lonlat_numpy\\201812\\01\\H00\\000001.npy")

#m = Basemap(projection='nplaea',boundinglat=60,lon_0=270,resolution='l')
m = Basemap(width=12000000,height=9000000,projection='ortho',lat_0=-90,lon_0=120,resolution='l')
#m.bluemarble()
m.shadedrelief()
#m.tissot(70,80,1,100,facecolor='red',zorder=10)
#m.scatter(75.2,85.3,s=100,marker='o',color='#FF5600')
lon=lonlat[0,:]
lat=lonlat[1,:]



xpt, ypt = m(lon, lat)
m.plot(xpt,ypt,'r')

plt.show()


