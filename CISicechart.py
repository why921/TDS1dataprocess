import shapefile
from matplotlib import pyplot as plt
import pyproj
from mpl_toolkits.basemap import Basemap
import numpy as np
from shapely.geometry import Polygon
from shapely.geometry import Point
#"E:\why2023\CIS_SIGRID-3\Eastern_Arctic\2018\cis_SGRDREA_20180101T1800Z_pl_a\cis_SGRDREA_20180101T1800Z_pl_a.shp"
#"E:\why2023\CIS_SIGRID-3\Eastern_Arctic\2018\cis_SGRDREA_20180430T1800Z_pl_a\cis_SGRDREA_20180430T1800Z_pl_a.shp"
#"E:\why2023\CIS_SIGRID-3\Western_Arctic\2018\cis_SGRDRWA_20180430T1800Z_pl_a\cis_SGRDRWA_20180430T1800Z_pl_a.shp"
file = shapefile.Reader("E:\why2023\CIS_SIGRID-3\Eastern_Arctic\\2018\\cis_SGRDREA_20180430T1800Z_pl_a\cis_SGRDREA_20180430T1800Z_pl_a.shp")#读取

print(str(file.shapeType))
print(file.encoding)
print(file.bbox)
print(file.numRecords)
print(file.fields)

p=pyproj.Proj('+proj=lcc +lon_0=-100 +lat_0=40 +lat_1=49 +lat_2=77')
#PROJCS["WGS_1984_Lambert_Conformal_Conic",GEOGCS["GCS_WGS_1984",
#DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],
#PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],
#PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",0.0],
#PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-100.0],
#PARAMETER["Standard_Parallel_1",49.0],PARAMETER["Standard_Parallel_2",77.0],
#PARAMETER["Latitude_Of_Origin",40.0],UNIT["Meter",1.0]]

aa=70
bb=70

XY=p(aa, bb)
XYpoint = Point(XY)
border_shape = file
border = border_shape.shapes()
num=len(border)

object = Polygon(border[1].points)

IsIn=object.contains(XYpoint)
print(IsIn)

path='E:\GNSSR_DATA\CISchart\\20180430EA\\'
for i in range(num):
    border_points = border[i].points
    x, y = zip(*border_points)
    # x=(x1,x2,x3,…)
    # y=(y1,y2,y3,…)
    lon, lat = p(x, y, inverse=True)
    LON = np.array(lon, dtype=float)
    LAT = np.array(lat, dtype=float)
    LONLAT = np.column_stack((LON.T, LAT.T))
    if (len(border[i].parts) == 1):
       np.savetxt(path+'LL' + str(i) + '.txt', LONLAT)
    else:
        for j in range(len(border[i].parts)):
            if(j+1==len(border[i].parts)):
                llpart=LONLAT[border[i].parts[j]:,:]
                np.savetxt(path+'LL' + str(i)+'_' + str(j+1) + '.txt', llpart)
            else:
                llpart = LONLAT[border[i].parts[j]:border[i].parts[j + 1], :]
                np.savetxt(path+'LL' + str(i)+'_' + str(j+1) + '.txt', llpart)



#E:\GNSSR_DATA\CISchart\20180430EA
