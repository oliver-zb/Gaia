import pickle
from numpy import concatenate, pi, sin, cos, mean, median
from rotmatr import M
import matplotlib.pyplot as pl

lyst = []

for fnum in range(8):
    pkfname = 'stars'+str(fnum)+'.pkl'
    fil = open(pkfname,'rb')
    arr = pickle.load(fil)
    lyst.append(arr)
    fil.close()

lots = concatenate(lyst, axis=0)
print(lots.shape)

ra, dec, parallax = lots[:,0], lots[:,2], lots[:,4]
pmra, pmdec, rv = lots[:,6], lots[:,8], lots[:,10]
teff = lots[:,12]

ra *= pi/180
dec *= pi/180
r = 1e3/parallax

f = 149597870.7/(86400*365.25) * pi/180 / 3600
    # au/yr to km/s and arcsec to radian

pmra *= f
pmdec *= f

csra, snra = cos(ra), sin(ra)
csdec, sndec = cos(dec), sin(dec)

x = r*csdec*csra
y = r*csdec*snra
z = r*sndec

vx = csdec*csra*rv - r*sndec*csra*pmdec - r*csdec*snra*pmra
vy = csdec*snra*rv - r*sndec*snra*pmdec + r*csdec*csra*pmra
vz = sndec*rv      + r*csdec*pmdec

X = M[0,0]*x + M[0,1]*y + M[0,2]*z
Y = M[1,0]*x + M[1,1]*y + M[1,2]*z
Z = M[2,0]*x + M[2,1]*y + M[2,2]*z

U = M[0,0]*vx + M[0,1]*vy + M[0,2]*vz
V = M[1,0]*vx + M[1,1]*vy + M[1,2]*vz
W = M[2,0]*vx + M[2,1]*vy + M[2,2]*vz

sel = teff > 6000
rsel = r[sel]
print(rsel.shape)
Xsel = X[sel]
Ysel = Y[sel]
Zsel = Z[sel]
Usel = U[sel]
Vsel = V[sel]
Wsel = W[sel]

print(median(Usel),median(Vsel),median(Wsel))
print((median(Usel)**2+median(Vsel)**2+median(Wsel)**2)**.5)

pl.plot(x[sel],vx[sel],'.')
#pl.hist(Usel,bins=100)
#pl.gca().set_aspect('equal')
pl.show()
