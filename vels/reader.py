import pickle

fil = open('GaiaSource_1584380076484244352_2200921635402776448.csv')
head = fil.readline().split(',')

#for i,x in enumerate(head):
#    print(i,x)

dic = { 'ra': 5, 'dec': 7, 'parallax': 9,
        'pmra': 12, 'pmdec': 14, 'radial_velocity': 66,
        'teff_val': 78
      }

cols = (dic['ra'],dic['ra']+1,
        dic['dec'],dic['dec']+1,
        dic['parallax'],dic['parallax']+1,
        dic['pmra'],dic['pmra']+1,
        dic['pmdec'],dic['pmdec']+1,
        dic['radial_velocity'],dic['radial_velocity']+1,
        dic['teff_val'],dic['teff_val']+1,dic['teff_val']+2)

print(cols)
for i in cols:
    print(head[i])

for s in range(2):
    star = fil.readline().split(',')
    for i in (5,7,9,12,14,66,78):
        print(head[i],end=' ')
    print()
    for i in (5,7,9,12,14,66,78):
        print(star[i],end=' ')
    print()

fil.close()

import numpy

fname = 'GaiaSource_1584380076484244352_2200921635402776448.csv'

lots = numpy.genfromtxt(fname, delimiter=',', skip_header=1,
       filling_values=-999, usecols=cols)

parallax_ok = 10*lots[:,5] < lots[:,4]
pmra_ok = 10*lots[:,7] < abs(lots[:,6])
pmdec_ok = 10*lots[:,9] < abs(lots[:,8])
rv_ok = 10*lots[:,11] < abs(lots[:,10])
teff_ok = 5*(lots[:,14]-lots[:,13]) < lots[:,12]

lots = lots[parallax_ok*pmra_ok*pmdec_ok*rv_ok*teff_ok,:]

fil = open('star1.pkl','wb')
pickle.dump(lots,fil)
fil.close()

ra, dec, parallax = lots[:,0], lots[:,2], lots[:,4]
pmra, pmdec, rv = lots[:,6], lots[:,8], lots[:,10]
teff = lots[:,12]

for s in range(1):
    print(ra[s],dec[s],parallax[s],pmra[s],pmdec[s],rv[s],teff[s])

print(lots.shape)

