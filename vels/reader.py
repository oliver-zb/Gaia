import pickle
import numpy

cols = (5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 66, 67, 78, 79, 80)

fnum = 0

for fname in ('GaiaSource_1584380076484244352_2200921635402776448.csv',
              'GaiaSource_2200921875920933120_3650804325670415744.csv',
              'GaiaSource_2851858288640_1584379458008952960.csv',
              'GaiaSource_3650805523966057472_4475721411269270528.csv',
              'GaiaSource_4475722064104327936_5502601461277677696.csv',
              'GaiaSource_5502601873595430784_5933051501826387072.csv',
              'GaiaSource_5933051914143228928_6714230117939284352.csv',
              'GaiaSource_6714230465835878784_6917528443525529728.csv',
             ):
    
    print(fname,fnum)

    if fnum==0:
        fil = open(fname)
        head = fil.readline().split(',')
        for i in cols:
            print(head[i])
        for s in range(0):
            star = fil.readline().split(',')
            for i in (5,7,9,12,14,66,78):
                print(head[i],end=' ')
            print()
            for i in (5,7,9,12,14,66,78):
                print(star[i],end=' ')
            print()
        fil.close()

    lots = numpy.genfromtxt(fname, delimiter=',', skip_header=1,
                            filling_values=-999, usecols=cols)

    near = lots[:,4] > 10
    parallax_ok = 10*lots[:,5] < lots[:,4]
    pmra_ok = 10*lots[:,7] < abs(lots[:,6])
    pmdec_ok = 10*lots[:,9] < abs(lots[:,8])
    rv_ok = 10*lots[:,11] < abs(lots[:,10])
    teff_ok = 5*(lots[:,14]-lots[:,13]) < lots[:,12]

    lots = lots[near*parallax_ok*pmra_ok*pmdec_ok*rv_ok*teff_ok,:]
    print(lots.shape)


    pkfname = 'stars'+str(fnum)+'.pkl'
    fil = open(pkfname,'wb')
    pickle.dump(lots,fil)
    fil.close()
    print(pkfname)
    fnum += 1

    ra, dec, parallax = lots[:,0], lots[:,2], lots[:,4]
    pmra, pmdec, rv = lots[:,6], lots[:,8], lots[:,10]
    teff = lots[:,12]
    for s in range(1):
        print(ra[s],dec[s],parallax[s],pmra[s],pmdec[s],rv[s],teff[s])



