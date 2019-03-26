"this file is used to find over-densities in velocity- or position-space to find star clusters"

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

teff=np.load('data/temp_small_rv.npy')
X=np.load('data/x_com_small_rv.npy')
Y=np.load('data/y_com_small_rv.npy')
Z=np.load('data/z_com_small_rv.npy')
U=np.load('data/U_com_small_rv.npy')
V=np.load('data/V_com_small_rv.npy')
W=np.load('data/W_com_small_rv.npy')
par=np.load('data/parallax.npy')



r=np.array([1000/i for i in par])

"selection criteria for different distances from the Sun. upper and lower distance can be set by" \
"choosing different vlalues in (r > lower)*(r < upper)"
sel = (( r >100) * (r < 150) * (abs(U) < 100) * (abs(V) < 100) * (abs(W) < 100))

"if velocity-space does not give a meaningful result, one can instead first look for structures" \
"in position space and then apply restrictions, according to the locations of the over-density in" \
"position space, in velocity space"
#sel = ((r>100)*(r < 150) * (X < 0) * (X > -24) * (Y < -1) * (Y > -14))



print(r[sel].shape)
plt.hist2d(U[sel], V[sel], bins=150, norm=colors.LogNorm())
plt.xlabel('v_rad')
plt.ylabel('v_tan')
plt.gca().set_aspect('equal')
plt.title('v_rad vs. v_tan, 150 pc < r < 200 pc')
#plt.title('X vs. Y, 150pc < r < 200pc, -24km/s < U < 0km/s, -14km/s < V < -1km/s')
#plt.savefig('für_BA/vrad_vtan_150pc.png', format='png', dpi=1200)


plt.show()