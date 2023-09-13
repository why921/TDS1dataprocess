import shapefile
from matplotlib import pyplot as plt
import pyproj
from mpl_toolkits.basemap import Basemap

#"E:\why2023\CIS_SIGRID-3\Eastern_Arctic\2018\cis_SGRDREA_20180101T1800Z_pl_a\cis_SGRDREA_20180101T1800Z_pl_a.shp"
file = shapefile.Reader("E:\why2023\CIS_SIGRID-3\Eastern_Arctic\\2018\cis_SGRDREA_20180101T1800Z_pl_a\cis_SGRDREA_20180101T1800Z_pl_a.shp")#读取

print(str(file.shapeType))
print(file.encoding)
print(file.bbox)
print(file.numRecords)
print(file.fields)

border_shape = file
border = border_shape.shapes()
mun=len(border)

border_points = border[1].points

x, y = zip(*border_points)
# x=(x1,x2,x3,…)
# y=(y1,y2,y3,…)

p=pyproj.Proj('+proj=lcc +lon_0=-100 +lat_0=40 +lat_1=49 +lat_2=77 +ellps=WGS84')
#PROJCS["WGS_1984_Lambert_Conformal_Conic",GEOGCS["GCS_WGS_1984",
#DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],
#PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],
#PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",0.0],
#PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-100.0],
#PARAMETER["Standard_Parallel_1",49.0],PARAMETER["Standard_Parallel_2",77.0],
#PARAMETER["Latitude_Of_Origin",40.0],UNIT["Meter",1.0]]


lon, lat = p(x, y, inverse=True)

print(lon)

m = Basemap(width=12000000,height=12000000,projection='lcc',lat_0=40,lon_0=-100,lat_1=49,lat_2=77,resolution=None)
#m.bluemarble()
m.etopo()
#m.tissot(70,80,1,100,facecolor='red',zorder=10)
#m.scatter(75.2,85.3,s=100,marker='o',color='#FF5600')

xpt, ypt = m(lon, lat)

m.plot(xpt,ypt,'r')

plt.show()