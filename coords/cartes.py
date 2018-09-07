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

k = 149597870.7/(86400*365.25) * 1e-3   # au/yr to km/s

pmra *= k
pmdec *= k

csra, snra = cos(ra), sin(ra)
csdec, sndec = cos(dec), sin(dec)

x = r*csdec*csra
y = r*csdec*snra
z = r*sndec

vx = csdec*csra*rv - r*sndec*csra*pmdec - r*snra*pmra
vy = csdec*snra*rv - r*sndec*snra*pmdec + r*csra*pmra
vz = sndec*rv      + r*csdec*pmdec

X = M[0,0]*x + M[0,1]*y + M[0,2]*z
Y = M[1,0]*x + M[1,1]*y + M[1,2]*z
Z = M[2,0]*x + M[2,1]*y + M[2,2]*z

U = M[0,0]*vx + M[0,1]*vy + M[0,2]*vz
V = M[1,0]*vx + M[1,1]*vy + M[1,2]*vz
W = M[2,0]*vx + M[2,1]*vy + M[2,2]*vz

for T in range(3000,7200,200):
    sel = (teff >= T-100) * (teff < T+100)
    pl.plot(T,median(U[sel]),'.',color='cyan',label='U')
    pl.plot(T,median(V[sel]),'.',color='magenta',label='V')
    pl.plot(T,median(W[sel]),'.',color='red',label='W')
    print(T,(median(U[sel])**2+median(V[sel])**2+median(W[sel])**2)**.5)
pl.legend()
pl.show()
