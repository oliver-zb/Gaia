"This is used to do the rotations in velocity-space (U and V components). Similar for rotations in position space"

import numpy as np
import timeit

start = timeit.default_timer()

U=np.load('data/U_com.npy')
V=np.load('data/V_com.npy')

M = np.random.randint(low=1, high=360, size=len(x))


U_rot=[np.cos(M[i])*U[i]-np.sin(M[i]*V[i]) for i in range(0,len(x),1)]
V_rot=[np.sin(M[i])*U[i]+np.cos(M[i]*V[i]) for i in range(0,len(x),1)]

np.save('data/z_com_vel_rot.npy',z)
np.save('data/U_com_vel_rot.npy',U_rot)
np.save('data/V_com_vel_rot.npy',V_rot)

stop = timeit.default_timer()
print("calculation time:", round(stop - start),"s")