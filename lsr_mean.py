
"calculates local kinematics using mean average"

import numpy as np
import matplotlib.pyplot as plt

"it does not make a difference if i take the values from CoM or good_values, result is the same"

teff=np.load('data/temp_small_rv.npy')
t_up=np.load('data/temp_upp_err_all.npy')
t_low=np.load('data/temp_low_err_all.npy')
x=np.load('data/x_com_small_rv.npy')
y=np.load('data/y_com_small_rv.npy')
z=np.load('data/z_com_small_rv.npy')

U=np.load('data/U_com_small_rv.npy')
V=np.load('data/V_com_small_rv.npy')
W=np.load('data/W_com_small_rv.npy')

U_err_up=np.load('data/U_err_up_gal_small_rv.npy')
V_err_up=np.load('data/V_err_up_gal_small_rv.npy')
W_err_up=np.load('data/W_err_up_gal_small_rv.npy')
U_err_low=np.load('data/U_err_low_gal_small_rv.npy')
V_err_low=np.load('data/V_err_low_gal_small_rv.npy')
W_err_low=np.load('data/W_err_low_gal_small_rv.npy')

u_up,v_up,w_up=np.array(np.absolute(U-U_err_up)),np.array(np.absolute(V-V_err_up)),np.array(np.absolute(W-W_err_up))
u_low,v_low,w_low=np.array(np.absolute(U-U_err_low)),np.array(np.absolute(V-V_err_low)),np.array(np.absolute(W-W_err_low))
print(x[0])
x=x+8200
print(x[0])

d=np.sqrt(x**2+y**2+z**2)
print('min d', np.min(d),'max d', np.max(d))

sel=(d<=100)

teff=teff[sel]
t_up=t_up[sel]
t_low=t_low[sel]
U=U[sel]
V=V[sel]
W=W[sel]

U_err_up=U_err_up[sel]
V_err_up=V_err_up[sel]
W_err_up=W_err_up[sel]
U_err_low=U_err_low[sel]
V_err_low=V_err_low[sel]
W_err_low=W_err_low[sel]

print(len(U))

def error(up,low):
    err=[]
    for i in range(0,len(up),1):
        if up[i] > low[i]:
            err.append(up[i])
        elif up[i] < low[i]:
            err.append(low[i])
    err = np.array(err)
    return err


su=[]
sv=[]
sw=[]

"here, the upper and lower bounds for temperature can be chosen:" \
"temp from 3400 to 7800 for (almost) all data within 100 pc," \
"from 3600 to 6600 in the linear are for U and W"
for T in range(3400,7800,200):
    sel = (teff >= T-100) * (teff < T+100)

    "use these without error bars"
    # plt.plot(T,np.mean(U[sel]),marker='.',color='cyan',label='U')
    # plt.plot(T,np.mean(V[sel]),marker='.',color='magenta',label='V')
    # plt.plot(T,np.mean(W[sel]),marker='.',color='red',label='W')

    uerr=(np.std(U[sel])/(len(U[sel]))**0.5)
    verr=(np.std(V[sel])/(len(V[sel]))**0.5)
    werr=(np.std(W[sel])/(len(W[sel]))**0.5)

    t_err = [((t_up[sel])[i] + (t_low[sel])[i]) / 2 - (teff[sel])[i] for i in range(0, len(teff[sel]), 1)]
    t_err=np.mean(t_err)

    su.append(np.mean(U[sel]))
    sv.append(np.mean(V[sel]))
    sw.append(np.mean(W[sel]))

    "use these for plots with error bars"
    plt.errorbar(T,np.mean(U[sel]),xerr=(t_err),yerr=uerr,marker='.',markersize=6,color='cyan',
                 label='U',ecolor='black')
    plt.errorbar(T,np.mean(V[sel]),xerr=(t_err),yerr=verr,marker='.',markersize=6,color='magenta',
                 label='V',ecolor='black')
    plt.errorbar(T,np.mean(W[sel]),xerr=(t_err),yerr=werr,marker='.',markersize=6,color='red',
                 label='W',ecolor='black')

    "here, one can uncomment parts if the numerical values are desired"
    # print(T,len(U[sel]),'U',np.mean(U[sel]),'uerr',
    #       uerr,'V', np.mean(V[sel]),'verr',verr,'W',np.mean(W[sel]),'werr',werr,'terr',t_err)
    # print('')


ou=np.std(su)/np.sqrt(len(su))
ov=np.std(sv)/np.sqrt(len(sv))
ow=np.std(sw)/np.sqrt(len(sw))
mu,mv,mw=np.mean(su),np.mean(sv),np.mean(sw)
print(mu,mv,mw)
print(ou,ov,ow)



#plt.legend()
plt.title('Temperature dependent LSR-velocities, mean')
plt.xlabel('$T_{eff}$ in K')
plt.ylabel('U,V,W in km/sec')
#plt.savefig('fuer_BA/temp_dep_vel_100_mean.png', format='png', dpi=1200)
plt.show()