"here, the entire data set is searched for objects that potentially have left one of the confirmed clusters"
"because the result gives too many possible candidates, no further examination is done." \
"However, one could store the information of the candidates for further studies, if desired." \
"See thesis for further description."

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import timeit

start = timeit.default_timer()

"all data, not shifted"

X=np.load('data/x_com.npy')
Y=np.load('data/y_com.npy')
Z=np.load('data/z_com.npy')
U=np.load('data/v_rad_com.npy')
V=np.load('data/v_tan_com.npy')
W=np.load('data/w_com.npy')
b=np.load('new/b.npy')
l=np.load('new/l.npy')
name=np.load('new/name.npy')


dens=np.load('data/dens_gal.npy')
temp=np.load('data/temp.npy')

"data of clusters"

X1=np.load('data/clusters/1/new/X1.npy')
Y1=np.load('data/clusters/1/new/Y1.npy')
Z1=np.load('data/clusters/1/new/Z1.npy')
U1=np.load('data/clusters/1/new/v_rad1.npy')
V1=np.load('data/clusters/1/new/v_tan1.npy')
W1=np.load('data/clusters/1/new/W1.npy')
dens1=np.load('data/clusters/1/new/dens1.npy')
temp1=np.load('data/clusters/1/new/temp1.npy')


X2=np.load('data/clusters/2/new/X2.npy')
Y2=np.load('data/clusters/2/new/Y2.npy')
Z2=np.load('data/clusters/2/new/Z2.npy')
U2=np.load('data/clusters/2/new/v_rad2.npy')
V2=np.load('data/clusters/2/new/v_tan2.npy')
W2=np.load('data/clusters/2/new/W2.npy')
dens2=np.load('data/clusters/2/new/dens2.npy')
temp2=np.load('data/clusters/2/new/temp2.npy')


def dist(x,y,z):
    dd=[]
    d=np.sqrt(x**2+y**2+z**2)
    dd.append(d)
    dd=np.array(dd)
    return dd[0]

def phase_dist(x,y,z,u,v,w):
    dd=[]
    d=np.sqrt(x**2+y**2+z**2+u**2+v**2+w**2)
    dd.append(d)
    dd=np.array(dd)
    return dd[0]

def di(a,b):
    d=a-np.mean(b)
    return(d)

"distane of clusters mean and individual stars of entire sample in each component"
dx1,dy1,dz1=di(X,X1),di(Y,Y1),di(Z,Z1)
dx2,dy2,dz2=di(X,X2),di(Y,Y2),di(Z,Z2)
du1,dv1,dw1=di(U,U1),di(V,V1),di(W,W1)
du2,dv2,dw2=di(U,U2),di(V,V2),di(W,W2)

#print('dx1',dx1)

"distance (vector norm) in position and velocity space"

dp1=dist(dx1,dy1,dz1)
# dv1_unshift=dist(U1,V1,W1) #velocity not shifted
dvel1=dist(du1,dv1,dw1) #velocity shifted
dvel1=dvel1*((1/1.02269032)*10**-6) # to converk km/s to pc/yr



dp2=dist(dx2,dy2,dz2)
#dv2_unshift=dist(U2,V2,W2) #velocity not shifted
dvel2=dist(du2,dv2,dw2) #velocity shifted
dvel2=dvel2*((1/1.02269032)*10**-6) # to converk km/s to pc/yr

print('min dp1',min(dp1),'max(dp2)',max(dp2))
print('min dv1',min(dv1),'max(dv2)',max(dv2))

print('dp1[0]',dp1[0],'dp2[0]',dp2[0])
print('dvel1[0]',dvel1[0],'dvel2[0]',dvel2[0])

t1=[]
for i in range(0,len(dv1),1):
    t=abs(dp1[i]/dvel1[i])
    t1.append(t)
t2=[]
for i in range(0,len(dv2),1):
    t=abs(dp2[i]/dvel2[i])
    t2.append(t)
t1,t2=np.array(t1),np.array(t2)

print('min(t1)',min(t1),'max(t1)',max(t1),'min(t2)',min(t2),'max(t2)',max(t2))
sel1=((abs(t1)<680*10**6)*(abs(t1)>10**5))
sel2=((abs(t2)<160*10**6)*(abs(t2)>10**5))

x1=X[sel1]
y1=Y[sel1]
z1=Z[sel1]
x2=X[sel2]
y2=Y[sel2]
z2=Z[sel2]

u1=U[sel1]
v1=V[sel1]
w1=W[sel1]
u2=U[sel2]
v2=V[sel2]
w2=W[sel2]

b1=b[sel1]
l1=l[sel1]
b2=b[sel2]
l2=l[sel2]
name1=name[sel1]
name2=name[sel2]


vdist1=dist(U1,V1,W1)
mv1=np.mean(vdist1)
std1=np.std(vdist1)
vdist2=dist(U2,V2,W2)
mv2=np.mean(vdist2)
std2=np.std(vdist2)


s1=dist(u1,v1,w1)
s2=dist(u2,v2,w2)

sel1=((s1<(mv1+1.25*std1)*(s1>=mv1)))
sel2=((s2<(mv2+1.25*std2)*(s2>=mv2)))

x1=x1[sel1]
y1=y1[sel1]
z1=z1[sel1]
x2=x2[sel2]
y2=y2[sel2]
z2=z2[sel2]

u1=u1[sel1]
v1=v1[sel1]
w1=w1[sel1]
u2=u2[sel2]
v2=v2[sel2]
w2=w2[sel2]

b1=b1[sel1]
l1=l1[sel1]
b2=b2[sel2]
l2=l2[sel2]
name1=name1[sel1]
name2=name2[sel2]

print(len(x1))
print(len(x2))

# print('l1',l1)
# print('b1',b1)
# print('l2',l2)
# print('b2',b2)
# print('name1',name1)
# print('name2',name2)


"plots"

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x1, y1, z1, color='red',marker='.', markersize=2, linestyle='',alpha=1,label='candidates')
ax.plot(X1, Y1, Z1,color='blue', marker='.', markersize=2, linestyle='', alpha=1,label='Hyades')
plt.title('Objects that possibly left Hyades')
plt.legend()
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x2, y2, z2, color='red',marker='.', markersize=2, linestyle='',alpha=1,label='candidates')
ax.plot(X2, Y2, Z2,color='blue', marker='.', markersize=2, linestyle='', alpha=1,label='Pleiades')
plt.title('Objects that possibly left Pleiades')
plt.legend()
plt.show()


stop = timeit.default_timer()
print("calculation time:", round(stop - start),"s")