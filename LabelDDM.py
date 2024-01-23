import os
import shapefile
from matplotlib import pyplot as plt
import pyproj
from mpl_toolkits.basemap import Basemap
import numpy as np
from shapely.geometry import Polygon
from shapely.geometry import Point

file = shapefile.Reader("E:\why2023\CIS_SIGRID-3\Eastern_Arctic\\2018\cis_SGRDREA_20180430T1800Z_pl_a\cis_SGRDREA_20180430T1800Z_pl_a.shp")#读取

p=pyproj.Proj('+proj=lcc +lon_0=-100 +lat_0=40 +lat_1=49 +lat_2=77')

border_shape = file
border = border_shape.shapes()
num=len(border)


# "E:\GNSSR_DATA\TDS-1\lonlat_numpy\201804\30\H00\000013.txt"E:\GNSSR_DATA\TDS-1\label
# E:\GNSSR_DATA\TDS-1\DDM_numpy\201804\30\H00
Area='EA'
Year = '2018'
Month = '04'
Day = '30'
Product = 'H00'
Num='37'

file = open('E:\GNSSR_DATA\TDS-1\label\\'+Area+'\\'+Year+Month+Day+Product+'_'+Num+'.txt','w')

for idborder in range(len(border)):
    with open('E:\GNSSR_DATA\TDS-1\lonlat_numpy\\'+Year+Month+'\\'+Day+'\\'+Product+'\\'+'0000'+Num+'.txt', "r") as filetxt, open('E:\GNSSR_DATA\TDS-1\label\\'+Area+'\\'+Year+Month+Day+Product+'_'+Num+'.txt', "a") as filelabel:
        lonlat = np.loadtxt(filetxt)
        print(len(lonlat))
        print(idborder)
        for idlonlat in range(len(lonlat)):
            XY = p(lonlat[idlonlat, 0], lonlat[idlonlat, 1])
            XYpoint = Point(XY)
            object = Polygon(border[idborder].points)
            IsIn = object.contains(XYpoint)
            if (IsIn):
                filelabel.write('E:\GNSSR_DATA\TDS-1\DDM_numpy\\'+Year+Month+'\\'+Day+'\\'+Product+'\\'+'0000'+Num+'.npy'+' '+str(idlonlat)+' '+str(idborder) + "\n")




