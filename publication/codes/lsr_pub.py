""
"After the program load_data.py finished, one can run this program to get the plot with its " \
"corresponding values that can be found in the research notes."
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import gridspec

teff=np.load('publication/data/temp.npy')
t_up=np.load('publication/data/temp_upp_err.npy')
t_low=np.load('publication/data/temp_low_err.npy')
x=np.load('publication/data/x_gal.npy')
y=np.load('publication/data/y_gal.npy')
z=np.load('publication/data/z_gal.npy')

U=np.load('publication/data/U_gal.npy')
V=np.load('publication/data/V_gal.npy')
# U=np.load('CoM/normal/small_rv_rad_tan_vel/v_rad_com_small_rv_rad_tan_vel.npy')
# V=np.load('CoM/normal/small_rv_rad_tan_vel/v_tan_com_small_rv_rad_tan_vel.npy')
W=np.load('publication/data/W_gal.npy')
#
U_err_up=np.load('publication/data/U_err_up_gal.npy')
V_err_up=np.load('publication/data/V_err_up_gal.npy')
W_err_up=np.load('publication/data/W_err_up_gal.npy')
U_err_low=np.load('publication/data/U_err_low_gal.npy')
V_err_low=np.load('publication/data/V_err_low_gal.npy')
W_err_low=np.load('publication/data/W_err_low_gal.npy')

u_up,v_up,w_up=np.array(np.absolute(U-U_err_up)),np.array(np.absolute(V-V_err_up)),np.array(np.absolute(W-W_err_up))
u_low,v_low,w_low=np.array(np.absolute(U-U_err_low)),np.array(np.absolute(V-V_err_low)),np.array(np.absolute(W-W_err_low))
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

#t_err=[(t_up[i]+t_low[i])/2 - teff[i] for i in range(0,len(teff),1)]

su=[]
sv=[]
sw=[]

fig = plt.figure()
gs=gridspec.GridSpec(1,2,width_ratios=[3,1])
# ax1 = fig.add_subplot(1, 2, 1)
#plt.subplot(1,2,1)
ax1=plt.subplot(gs[0])


"fuer alle: temp von 3400 bis 7800, sonst 3600 bis 6600"
for T in range(3600,7000,200):
    sel = (teff >= T-100) * (teff < T+100)
    # plt.plot(T,np.mean(U[sel]),marker='.',color='cyan',label='U')
    # plt.plot(T,np.mean(V[sel]),marker='.',color='magenta',label='V')
    # plt.plot(T,np.mean(W[sel]),marker='.',color='red',label='W')

    uerr=(np.std(U[sel])/(len(U[sel]))**0.5)
    verr=(np.std(V[sel])/(len(V[sel]))**0.5)
    werr=(np.std(W[sel])/(len(W[sel]))**0.5)
    # teff,t_up,t_low=teff[sel],t_up[sel],t_low[sel]

#    t_err = [((t_up[sel])[i] + (t_low[sel])[i]) / 2 - (teff[sel])[i] for i in range(0, len(teff[sel]), 1)]
    t_err = [((t_up[sel])[i] + (t_low[sel])[i]) / 2 - (teff[sel])[i] for i in range(0, len(teff[sel]), 1)]
    t_err=np.mean(t_err)
    #t_err=(np.std(teff[sel])/(len(teff[sel]))**0.5)

    su.append(np.mean(U[sel]))
    sv.append(np.mean(V[sel]))
    sw.append(np.mean(W[sel]))

    ax1.errorbar(T,-np.mean(U[sel]),xerr=(t_err),yerr=-uerr,marker='o',markersize=4,color='cyan',
                 label='U',ecolor='black',capsize=2)
    ax1.errorbar(T,-np.mean(V[sel]),xerr=(t_err),yerr=-verr,marker='^',markersize=4,color='magenta',
                 label='V',ecolor='black',capsize=2)
    ax1.errorbar(T,-np.mean(W[sel]),xerr=(t_err),yerr=-werr,marker='s',markersize=4,color='red',
                 label='W',ecolor='black',capsize=2)
    print(T,len(U[sel]),'U',np.mean(U[sel]),'uerr',
          uerr,'V', np.mean(V[sel]),'verr',verr,'W',np.mean(W[sel]),'werr',werr,'terr',t_err)
    # print(T,'&',len(U[sel]), '&', -round(np.mean(U[sel]),2), '$\pm$', round(uerr,2), '&',
    #       -round(np.mean(V[sel]),2), '$\pm$', round(verr,2), '&', -round(np.mean(W[sel]),2),
    #       '$\pm$', round(werr,2),"\\\\")
    # print('')


ax1.legend()

plt.title('Temperature dependent local velocities 100 pc')
plt.xlabel('Temperature in K')
plt.ylabel('U,V,W in $km s^{-1}$')

ax2=plt.subplot(gs[1],sharey=ax1)

ax2.errorbar([1,2,3,4],[11.1,8.16,14.1,8.63],yerr=[0.75,0.48,1.1,0.64],marker='o',markersize=4,color='cyan',
                 label='U',ls='none',ecolor='black',capsize=3)
ax2.errorbar([1,2,3,4],[12.24,11.19,14.6,4.76],yerr=[0.47,0.56,0.4,0.49],marker='^',markersize=4,color='magenta',
                 label='V',ls='none',ecolor='black',capsize=3)
ax2.errorbar([1,2,3,4],[7.25,8.55,6.9,7.26],yerr=[0.39,0.48,0.2,0.36],marker='s',markersize=4,color='red',
                 label='W',ls='none',ecolor='black',capsize=3)

ax2.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.title('Other LSR velocities')
plt.text(1, 23, '1: Schönrich et al.')
plt.text(1, 22, '2: Bobylev et al.')
plt.text(1, 21, '3: Francis et al.')
plt.text(1, 20, '4: Ding et al.')

plt.legend()

plt.savefig('plot.eps', format='eps', dpi=2400)
plt.show()