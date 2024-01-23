import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


DDM=np.load('E:\GNSSR_DATA\TDS-1\DDM_numpy\\201804\\30\H00\\000036.npy')
plt.figure("figure name screenshot") #图像窗口名称
plt.imshow(DDM[175])
plt.show()


def color_map(data, cmap):
    """数值映射为颜色"""

    dmin, dmax = np.nanmin(data), np.nanmax(data)
    cmo = plt.cm.get_cmap(cmap)
    cs, k = list(), 256 / cmo.N

    for i in range(cmo.N):
        c = cmo(i)
        for j in range(int(i * k), int((i + 1) * k)):
            cs.append(c)
    cs = np.array(cs)
    data = np.uint8(255 * (data - dmin) / (dmax - dmin))

    return cs[data]




ax = plt.figure().add_subplot(projection='3d')
#x=10
#x=x*np.ones(128)
y=np.linspace(0, 128, 128)
z1=DDM[175][0,:]
z2=DDM[175][10,:]

ax.plot(y, z1,zs=0, zdir='x', label='curve in (x, y)')
ax.plot(y, z2,zs=0, zdir='x', label='curve in (x, y)')

plt.show()