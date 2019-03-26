"calculates local kinematics using median average"

import numpy as np
import matplotlib.pyplot as plt

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


d=np.sqrt(x**2+y**2+z**2)

sel=(d<=100)

d=d[sel]

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
    t_err = [((t_up[sel])[i] + (t_low[sel])[i]) / 2 - (teff[sel])[i] for i in range(0, len(teff[sel]), 1)]
    t_err=np.mean(t_err)

    "use these without error bars"
    # plt.plot(T,np.median(U[sel]),marker='.',color='cyan',label='U')
    # plt.plot(T,np.median(V[sel]),marker='.',color='magenta',label='V')
    # plt.plot(T,np.median(W[sel]),marker='.',color='red',label='W')

    du=(np.percentile(U[sel],84)-np.percentile(U[sel],16))/(len(U[sel]))**0.5
    dv=(np.percentile(V[sel],84)-np.percentile(V[sel],16))/(len(V[sel]))**0.5
    dw=(np.percentile(W[sel],84)-np.percentile(W[sel],16))/(len(W[sel]))**0.5
    print(T,du,dv,dw)

    "use these for plots with error bars"
    plt.errorbar(T,np.median(U[sel]),xerr=(t_err),yerr=du,marker='.',markersize=6,color='cyan',label='U',ecolor='black')
    plt.errorbar(T,np.median(V[sel]),xerr=(t_err),yerr=dv,marker='.',markersize=6,color='magenta',label='V',ecolor='black')
    plt.errorbar(T,np.median(W[sel]),xerr=(t_err),yerr=dw,marker='.',markersize=6,color='red',label='W',ecolor='black')

    su.append(np.median(U[sel]))
    sv.append(np.median(V[sel]))
    sw.append(np.median(W[sel]))

    "here, one can uncomment parts if the numerical values are desired"
    #print(T,len(U[sel]),np.median(U[sel]),np.median(V[sel]),np.median(W[sel]))
    # print(T,'U 25%',np.percentile(U[sel],25),'U 75%',np.percentile(U[sel],75),'V 25%', np.percentile(V[sel], 25),
    #       'V 75%', np.percentile(V[sel], 75),'W 25%',np.percentile(W[sel],25), 'W 75%',np.percentile(W[sel],75))

#    print(T,len(U[sel]),np.median(U[sel]),np.median(V[sel]),np.median(W[sel]))


"avergage velocity components"

ou=np.std(su)/np.sqrt(len(su))
ov=np.std(sv)/np.sqrt(len(sv))
ow=np.std(sw)/np.sqrt(len(sw))
mu,mv,mw=np.mean(su),np.mean(sv),np.mean(sw)
print(mu,mv,mw)
print(ou,ov,ow)


plt.legend()
plt.title('Temperature dependent LSR-velocities, median')
plt.xlabel('$T_{eff}$ in K')
plt.ylabel('U,V,W in km/sec')
#plt.savefig('temp_dep_vel_100_median_errorbar.png', format='png', dpi=1200)
plt.show()

# plt.hist(teff,bins='auto',alpha=0.5,label='in pc')
# plt.title('Histogram of temperatures')
# plt.xlabel('temperature [K]')
# plt.grid()
# #plt.savefig('fuer_BA/temp_hist_100.png', format='png', dpi=1200)
# plt.show()