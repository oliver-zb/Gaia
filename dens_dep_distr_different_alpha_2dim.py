"densities have to be calculated with EnBid, alpha depends on densities"

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import timeit

start = timeit.default_timer()


x=np.load('data/x.npy')
y=np.load('data/y.npy')
z=np.load('data/z.npy')
# x=np.load('data/v_x.npy')
# y=np.load('data/v_y.npy')
# z=np.load('data/v_z.npy')
dens=np.load('data/dens.npy')
#alpha=np.load('data/alpha.npy')

dens = [i/(1.02269032*10**(-6)) for i in dens]
dens=np.log(dens)


class LinearColormap(LinearSegmentedColormap):

    def __init__(self, name, segmented_data, index=None, **kwargs):
        if index is None:
            # If index not given, RGB colors are evenly-spaced in colormap.
            index = np.linspace(0, 1, len(segmented_data['red']))
        for key, value in segmented_data.items():
            # Combine color index with color values.
            segmented_data[key] = zip(index, value)
        segmented_data = dict((key, [(y, z, z) for y, z in value])
                              for key, value in segmented_data.items())
        LinearSegmentedColormap.__init__(self, name, segmented_data, **kwargs)


color_spec = {'blue':  x,
           'green': y,
           'red':   z,
           'alpha': dens}
alpha_ = LinearColormap('alpha', color_spec)



fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
plt.scatter(x, y, c=dens,cmap='YlGnBu', s=2, edgecolors='none')
cbar=plt.colorbar()
cbar.set_label("Density")
plt.xlabel('x [pc]')
plt.ylabel('y [pc]')
#ax.set_zlabel('z [pc]')
plt.title('position distribution in x, y')
#plt.savefig('für_BA/pos_distr_dens_dep_com_rad_tan_vel_x_y.png', format='png', dpi=1200)



stop = timeit.default_timer()
print("calculation time:", round(stop - start),"s")

plt.show()