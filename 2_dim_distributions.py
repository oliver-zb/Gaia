import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors

# teff = np.load('coords/all/temp.npy')
# U=np.load('coords/all/U_s.npy')
# V=np.load('coords/all/V_s.npy')
# W=np.load('coords/all/W_s.npy')
# par=np.load('coords/all/parallax_s.npy')
# teff = np.load('good_values/small_rv/temp_all.npy')
# X=np.load('good_values/small_rv/x_small_rv.npy')
# Y=np.load('good_values/small_rv/x_small_rv.npy')
# Z=np.load('good_values/small_rv/z_small_rv.npy')
# U=np.load('good_values/small_rv/U_gal_small_rv.npy')
# V=np.load('good_values/small_rv/V_gal_small_rv.npy')
# W=np.load('good_values/small_rv/W_gal_small_rv.npy')
# par=np.load('good_values/small_rv/parallax_small_rv.npy')
# dens=np.load('good_values/small_rv/dens_gal_coords_rv_restr.npy')
# dens=np.log(dens)
# teff = np.load('CoM/normal/small_rv/temp_small_rv.npy')

"gut"
# U=np.load('CoM/normal/small_rv/U_com_small_rv.npy')
# V=np.load('CoM/normal/small_rv/V_com_small_rv.npy')
# W=np.load('CoM/normal/small_rv/W_com_small_rv.npy')
# X=np.load('CoM/normal/small_rv/X_com_small_rv.npy')
# Y=np.load('CoM/normal/small_rv/Y_com_small_rv.npy')
# Z=np.load('CoM/normal/small_rv/Z_com_small_rv.npy')
par=np.load('CoM/normal/small_rv/parallax_gal_small_rv.npy')

X=np.load('CoM/normal/small_rv_rad_tan_vel/x_com_small_rv_rad_tan_vel.npy')
Y=np.load('CoM/normal/small_rv_rad_tan_vel/y_com_small_rv_rad_tan_vel.npy')
Z=np.load('CoM/normal/small_rv_rad_tan_vel/z_com_small_rv_rad_tan_vel.npy')
U=np.load('CoM/normal/small_rv_rad_tan_vel/v_rad_com_small_rv_rad_tan_vel.npy')
V=np.load('CoM/normal/small_rv_rad_tan_vel/v_tan_com_small_rv_rad_tan_vel.npy')
W=np.load('CoM/normal/small_rv_rad_tan_vel/W_com_small_rv_rad_tan_vel.npy')

# X=np.load('new/x.npy')
# Y=np.load('new/y.npy')
# Z=np.load('new/z.npy')
# U=np.load('new/U_gal.npy')
# V=np.load('new/V_gal.npy')
# W=np.load('new/W_gal.npy')

dens=np.load('CoM/normal/small_rv_rad_tan_vel/dens_gal_small_rv_vrad_vtan.npy')
alpha=np.load('CoM/normal/small_rv_rad_tan_vel/alpha_gal_small_rv_vrad_vtan.npy')
dens=np.log(dens)
#par=np.load('CoM/normal/small_rv/parallax_gal_small_rv.npy')
# #
# print(len(X),len(dens))


r=np.array([1000/i for i in par])
sel = (r < 500)
# sel = ((r < 200) * (r > 150) * (abs(V) < 100) * (abs(W) < 100) * (abs(U) < 100))
# sel=((r < 200) * (r > 150) * (U < -39) * (U > -47) * (V < -18) * (V > -24))
# sel=((r < 200) * (r > 150) * (U < -39) * (U > -47) * (V < -18) * (V > -24)*(Y<-61)*(Y>-75)*(Z<107)*(Z>91))
#sel = ((r > 100) * (r < 150) * (X < -8231) * (X > -8254) * (Z < -11) * (Z > -23))
#sel = ((r < 100) * (U < -38) * (U > -45) * (V < -17) * (V > -22) * (X>-8254)*(X<-8231)*(Z>-24.5)*(Z<-10))
#sel = ((r < 100) * (X < -8231) * (X > -8254) * (Z < -11) * (Z > -23) )
#sel = ((r < 100) * (U < -38) * (U > -45) * (V < -17) * (V > -22)*(X < -8231) * (X > -8254) * (Z < -11) * (Z > -23))
#sel = ((r < 150) * (r > 100) * (X < -8312) * (X > -8329) * (Y < 36.8) * (Y > 21) *(U<-4)*(U>-10)*(V<-24)*(U>-32))
#sel = ((r < 450) * (r > 400) * (X>-8185)*(X<-8159)*(Y>-425)*(Y<-377)*(Z>-130)*(Z<-101))
#sel = ((r < 500) * (r > 450)*(X<-8026)*(X>-8047)*(Y<-426)*(Y>-480)*(Z<20)*(Z>-7))


print(r[sel].shape)
plt.hist2d(V[sel], W[sel], bins=150, norm=colors.LogNorm())
plt.xlabel('V')
plt.ylabel('W')
plt.gca().set_aspect('equal')
#plt.title('Y vs. Z 650pc < r < 700pc (v_rad, v_tan)')
#plt.savefig('CoM/normal/small_rv_rad_tan_vel/clusters/y_z_700pc.png', format='png', dpi=1200)

# sel = ((r < 1000) * (abs(X) < 1000) * (abs(Y) < 1000))
# print(r[sel].shape)
# dens=dens[sel]
# X,Y=X[sel],Y[sel]
# print(len(X),len(Y),len(dens))
# #plt.hist2d(X, Y, bins=150, norm=colors.LogNorm())
# plt.scatter(X,Y,c=dens)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.gca().set_aspect('equal')
# plt.title('X vs. V  r < 1000pc')

plt.show()