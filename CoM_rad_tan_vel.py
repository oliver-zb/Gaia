"for determining radial and tangential velocity of each star w.r.t. to galactic center"

import numpy as np
import timeit

start = timeit.default_timer()

x=np.load('data/x_com.npy')
y=np.load('data/y_com.npy')
U=np.load('data/U_com.npy')
V=np.load('data/V_com.npy')


M = [np.arctan(y[i]/x[i]) for i in range(0,len(x),1)]

v_rad=[np.cos(M[i])*U[i]-np.sin(M[i]*V[i]) for i in range(0,len(x),1)]
v_rad=np.array(v_rad)
v_tan=[np.sin(M[i])*U[i]+np.cos(M[i])*V[i] for i in range(0,len(x),1)]
v_tan=np.array(v_tan)

np.save('data/v_rad_com',v_rad)
np.save('data/v_tan_com',v_tan)




stop = timeit.default_timer()
print("calculation time:", round(stop - start),"s")