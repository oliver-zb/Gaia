import csv
import os
import timeit
import math as m
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

start = timeit.default_timer()

# def preview_csv(filename, limit):
#     if not os.path.isfile(filename):
#         print('ERROR: "{0}" file not found'.format(filename))
#         exit()
#     d = open(filename)
#     with open(filename, 'r', encoding='utf-8') as csv_file:
#         reader = csv.reader(d, delimiter=limit)  # for some datasets use ; for other use ,
#         ncol = len(next(reader))
#         print("number of columns:", ncol)  # counts number of columns
#
#         dict = {rows[1]:[rows[5],rows[6],rows[7],rows[8],rows[9],rows[10],rows[11],rows[12],rows[13],rows[14],
#             rows[15],rows[16],rows[17],rows[18],rows[19],rows[20],rows[21],rows[22],rows[23],rows[24],
#             rows[25],rows[66],rows[67],rows[73],rows[74]] for rows in reader}
#         "values in dict: [0]: ra, [1]: ra_err, [2]: dec, [3]: dec_err, [4]: parallax, [5]: parallax_err," \
#         "[6]: parallax_over_err, [7]: pmra (mu_alpha*), [8]: pmra_err, [9]: pmdec (mu_delta), [10]: pmdec_err," \
#         "[11]: ra_dec_corr, [12]: ra_parallax_corr, [13]: ra_pmra_corr, [14]: ra_pmdec_corr," \
#         "[15]: dec_parallax_corr, [16]: dec_pmra_corr, [17]: dec_pmdec_corr, [18]: parallax_pmra_corr," \
#         "[19]: parallax_pmdec_corr, [20]: pmra_pmdec_corr, [21]: radial_velocity, [22]: radial_velocity_err," \
#         "[23]: l (galactig longitude), [24]: b (galactig latitude), [25]: ecliptic_longitude, [26]: ecliptic_latitude"
# #    print('len(dict) initially:', len(dict)) # from read from csv
#
#
#     delete = []
#
#     for key in dict:
#         if any(s == '' for s in dict[key][1:]):
#             delete.append(key)
#             "contains empty string, continue now"
#             continue
#
#     for i in delete:
#         dict.pop(i, None)
# #    print('len(dict) without empty cells', len(dict))
#     return dict
#
# data = preview_csv("data/GaiaSource_6714230465835878784_6917528443525529728.csv", ';') # approx 8 seconds
# data.update(preview_csv("data/GaiaSource_2851858288640_1584379458008952960.csv", ','))
# data.update(preview_csv("data/GaiaSource_1584380076484244352_2200921635402776448.csv", ','))
# data.update(preview_csv("data/GaiaSource_2200921875920933120_3650804325670415744.csv", ','))
# data.update(preview_csv("data/GaiaSource_3650805523966057472_4475721411269270528.csv", ','))
# data.update(preview_csv("data/GaiaSource_4475722064104327936_5502601461277677696.csv", ','))
# data.update(preview_csv("data/GaiaSource_5502601873595430784_5933051501826387072.csv", ','))
# data.update(preview_csv("data/GaiaSource_5933051914143228928_6714230117939284352.csv", ','))
#
# delete = []
# for key in data:
#     if eval(data[key][4]) <= 0.001:
#         delete.append(key)
#         "to delete stars with too small parallax (data too bad)"
#     elif eval(data[key][5])/eval(data[key][4]) > 0.1:
#         delete.append(key)
#         "delete parallaxes with error more than 10% because positionns far away with big error" \
#         "have bad influence on result"
#
# for i in delete:
#     data.pop(i, None)
#
# key = list(data.keys())
# ra = []
# dec = []
# parallax = []
# pmra = []
# pmdec = []
# rv = []
# rv_err = []
# par_err = []
# pmra_err = []
# pmdec_err = []
# ra_err = []
# dec_err = []
#
# for key in data:
#     ra.append(eval(data[key][0]))
#     ra_err.append(eval(data[key][1]))
#     dec.append(eval(data[key][2]))
#     dec_err.append(eval(data[key][3]))
#     parallax.append(eval(data[key][4]))
#     pmra.append(eval(data[key][7]))
#     pmdec.append(eval(data[key][9]))
#     rv.append(eval(data[key][21]))
#     rv_err.append(eval(data[key][22]))
#     par_err.append(eval(data[key][5]))
#     pmra_err.append(eval(data[key][8]))
#     pmdec_err.append(eval(data[key][10]))
#
# par_err=np.array([i for i in par_err])
#
# dist = np.array([1000 / i for i in parallax])  # * 1000 because of milliarcsec, dimension: parsec -> velocities make sense, positions not
#
# "correct method for positions"
# x = np.array(dist * np.cos(dec) * np.cos(ra))
# y = np.array(dist * np.cos(dec) * np.sin(ra))
# z = np.array(dist * np.sin(dec))
#
# q = np.array([x,y,z])
#
#
# "transverse velocities in ra, dec, pmx = mu_x(arcseconds/year) * distance * 4.740 " \
# "-> * 1/ 1000 because we have mas" \
# "4.740 to convert as/year*dist in parsec to km/sec to have same dimension as rv"
#
# v_tra = 1 / 1000 * np.array(pmra) * np.array(dist) * 4.74 # * 1000 because of mas
# v_tdec = 1 / 1000 * np.array(pmdec) * np.array(dist) * 4.74
# "cartesian velocities, 1/977780 to convert km/sec to pc/year"
# v_x = (rv * np.cos(dec) * np.cos(ra) - v_tra * np.sin(ra) - v_tdec * np.sin(dec) * np.cos(ra)) / 977780
# v_y = (rv * np.cos(dec) * np.sin(ra) + v_tra * np.cos(ra) - v_tdec * np.sin(dec) * np.cos(ra)) / 977780
# v_z = (rv * np.sin(dec) + v_tdec * np.cos(dec)) / 977780
# v = np.array([v_x,v_y,v_z])

# "saves values, reading those is much faster than doing all the things above every time"
# # np.save('x_final', x)
# # np.save('y_final', y)
# # np.save('z_final', z)
# # np.save('q_final', q)
# #
# # v_x = np.array(v_x)
# # v_y = np.array(v_y)
# # v_z = np.array(v_z)
# #
# # np.save('v_x_final', v_x)
# # np.save('v_y_final', v_y)
# # np.save('v_z_final', v_z)
# # np.save('v_final1', v)
# #
# # np.save('par_err', par_err)
# # np.save('parallax', parallax)
# # np.save('pmra', pmra)
# # np.save('pmra_err',pmra_err)
# # np.save('pmdec', pmdec)
# # np.save('pmdec_err', pmdec_err)
# # np.save('ra', ra)
# # np.save('dec', dec)
# # np.save('rv', rv)
# # np.save('rv_err', rv_err)
# # np.save('ra_err',ra_err)
# # np.save('dec_err', dec_err)

" -> loading those is much faster than compiling dict every time"

x = np.load('x_final.npy')
y = np.load('y_final.npy')
z = np.load('z_final.npy')
q = np.load('q_final.npy')
v_x = np.load('v_x_final.npy')
v_y = np.load('v_y_final.npy')
v_z = np.load('v_z_final.npy')
v = np.load('v_final.npy')

# np.load('par_err.npy')
# np.load('parallax.npy')
# np.load('pmra.npy')
# np.load('pmra_err.npy')
# np.load('pmdec.npy')
# np.load('pmdec_err.npy')
# np.load('ra.npy')
# np.load('dec.npy')
# np.load('rv.npy')
# np.load('rv_err.npy')
# np.load('ra_err.npy')
# np.load('dec_err.npy')

"velocity distribution in cartesian coordinates"

# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot(v_x,v_y,v_z,marker='.', markersize=0.35,linestyle='',alpha=2) # markersize 0.5 oder 0.35 gut
# ax.set_title('velocity vectors in cartesian coordinates')
# ax.set_xlabel("x [pc/year]")
# ax.set_ylabel("y [pc/year]")
# ax.set_zlabel('z [pc/year]')
# # plt.xlim(-50,50)
# # plt.ylim(-50,50)
# # ax.set_zlim(-50,50)
# plt.savefig('vel_distr_final.png', format='png', dpi=1200)
#
# plt.show()

"positions in cartesian coordinates"

# fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot(x, y, z, marker='.', markersize=0.35, linestyle='', alpha=2)  # markersize 0.5 oder 0.35 gut
# ax.set_xlabel("x [pc]")
# ax.set_ylabel("y [pc]")
# ax.set_zlabel('z [pc]')
# ax.set_title('positions in cartesian coordinates')
# plt.savefig('pos_distr_final.png', format='png', dpi=1200)
#
# plt.show()

"cartesian coordinates at time t"

# def q_t(x,y,z,v_x,v_y,v_z,t):
#     x_t = x + v_x * t
#     y_t = y + v_y * t
#     z_t = z + v_z * t
#     q_t = np.array([x_t,y_t,z_t])
# #    v_tot = np.linalg.norm(q_t)
#     return q_t
#
# #print('q_t', q_t(x,y,z,v_x,v_y,v_z,10))
# q_t1 = q_t(x,y,z,v_x,v_y,v_z,10)
# q_t2 = q_t(x,y,z,v_x,v_y,v_z,100)

"shows how distances are distrbuted"

#plt.plot(dist)

#plt.show()

"plots time dependant positions"

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(ra_new, dec_new, parallax_new, c='b', marker='x')
# ax.scatter(q[0], q[1], q[2], c='y', label='q(0)', marker='x')
# ax.scatter(q_t1[0],q_t1[1], q_t1[2], c='c', label='q(t=10)', marker='x')
# ax.scatter(q_t2[0],q_t2[1], q_t2[2], c='m', label='q(t=100)', marker='x')
#ax.scatter(list(q[0])[:10], list(q[1])[:10], list(q[2])[:10], c='y', label='q(0)', marker='x')
#ax.scatter(list(q_t1[0])[:10],list(q_t1[1])[:10],list(q_t1[2])[:10], c='c', label='q(t=10)', marker='x')
#ax.scatter(list(q_t2[0])[:10],list(q_t2[1])[:10], list(q_t2[2])[:10], c='m', label='q(t=100)', marker='x')
#ax = fig.add_subplot(122, projection='3d')
#ax.scatter(v_x, v_y, v_z, c='b', marker='x')
#plt.xlim(-1,1)
#plt.ylim(-1,1)
#ax.set_zlim(-1,1)
#ax.set_title("positions of stars")
#plt.legend(loc=2)
#ax.set_xlabel("x [pc]")
#ax.set_ylabel("y [pc]")
#ax.set_zlabel('z [pc]')
#ax.set_zlabel('rv')
#plt.show()

"animation of 3d velocities"
"d/1000, 4.47 -> animation does not make sense, much too fast"
"d*1, 0.0047 -> animation makes sense"

# fig = plt.figure()
# ax = Axes3D(fig)
#
#
# points, = ax.plot(x, y, z, linestyle='', marker='.',markersize=1.75)
# txt = fig.suptitle('')
#
# def update_points(t, x, y, z, points):
#     txt.set_text('{:d} * 1000 years'.format(t)) # for debug purposes
#      #"calculate the new sets of coordinates here. The resulting arrays should have the same shape " \
#      #"as the original x,y,z"
#
#
#     new_x = x[: ]+v_x[: ]*t*1000
#     new_y = y[: ]+v_y[: ]*t*1000
#     new_z = z[: ]+v_z[: ]*t*1000
#     #print('t:', t)
#     # update properties
#     points.set_data(new_x,new_y)
#     points.set_3d_properties(new_z, 'z')
#
#     # return modified artists
#     return points,txt
#
# ani=animation.FuncAnimation(fig, update_points, frames=3000, interval=5, fargs=(x, y, z, points))
#
# ax.set_xlabel("x [pc]")
# ax.set_ylabel("y [pc]")
# ax.set_zlabel('z [pc]')
# # plt.xlim(-200,200)
# # plt.ylim(-200,200)
# # ax.set_zlim(-200,200)
#
# plt.show()

"animation of 2d velocities (xz-plane)"

# fig = plt.figure()
# ax = plt.axes()
# line, = ax.plot(x, z, '.')
#
# frames = 500
#
# y_new = []
# for t in range(0,frames,1):
#     ynew = y + v_y * t
#     y_new.append(ynew)
#
# # initialization function: plot the background of each frame
# def init():
#     line.set_data([], [])
#     return line,
#
# # animation function.  This is called sequentially
# def animate(i):
#     new_x = x[:10000] + v_x[:10000] * i
#     new_z = z[:10000] + v_z[:10000] * i
#     line.set_data(new_x,new_z)
# #    plt.plot(X,Z,'.')
#     return line,
#
# # call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate,
#                                frames=frames, interval=1, blit=False, init_func=init)
#
#
#
# plt.xlim(-2000,2000)
# plt.ylim(-2000,2000)
# plt.show()

"anaglyphic animation"

# fig = plt.figure()
# ax = plt.axes()
# txt = fig.suptitle('')
# frames = 1000
#
#
# z_c = 0  # let cameras be placed on x-axis
# #y_c = 0
# x_c = 10   # assume first only one camera in origin, later two cameras separated by distance of the eyes (65mm)
#
# "könnte noch faktor  3.086e+2 (von 3.086e+16 für pc -> m) mit position und geschwindigkeit multiplizieren)"
# "dann aber abstand zwischen rot und blau kleiner"
#
# x_s = np.array(q[0][:20000])
# y_s = np.array(q[1][:20000])
# z_s = np.array(q[2][:20000])
# v_x = np.array(v[0][:20000])
# v_y = np.array(v[1][:20000])
# v_z = np.array(v[2][:20000])
#
# y_c = 0.5
# # z_c = 0.5
#
# y_min = min(q[1])
# y_sc = y_min + y_s
# # z_min = min(q[2])
# # z_sc = z_min + z_s
#
# "zusätzlicher faktor zu lambda vergrössert abstand zwischen rot und blau"
# "jeweils erster teil: y-achse 3dim, zweiter teil: z-achse 3dim"
# lambd = (y_c / (y_c - y_sc))
# x_sc = lambd * (x_s - x_c) + x_c
# z_sc = lambd * (z_s - z_c) + z_c
# x_sc_1 = x_sc + lambd / 2
# x_sc_2 = x_sc - lambd / 2
# z_sc_1 = z_sc + lambd / 2
# z_sc_2 = z_sc - lambd / 2
# # lambd = (z_c / (z_c - z_sc))
# # x_sc = lambd * (x_s - x_c) + x_c
# # y_sc = lambd * (y_s - y_c) + y_c
# # x_sc_1 = x_sc + lambd / 2
# # x_sc_2 = x_sc - lambd / 2
# # y_sc_1 = y_sc + lambd / 2
# # y_sc_2 = y_sc - lambd / 2
#
# y_new = []
# #z_new = []
# lambd = []
# for t in range(0,frames,1):
#     y_min = min(y_s + v_y * t * 100)
#     y_sc = y_min + y_s * v_y * t * 100
#     lambd_new = y_c / (y_c - y_sc)
#     y_new.append(y_sc)
#     lambd.append(lambd_new)
# # for t in range(0,frames,1):
# #     z_min = min(z_s + v_z * t * 100)
# #     z_sc = z_min + z_s * v_z * t * 100
# #     lambd_new = z_c / (z_c - z_sc)
# #     z_new.append(z_sc)
# #     lambd.append(lambd_new)
#
# line_1, = ax.plot(x_sc_1, z_sc_1,c='r',linestyle='', marker='.',markersize=5, alpha=0.8)
# line_2, = ax.plot(x_sc_2, z_sc_2, c='c',linestyle='', marker='.',markersize=5, alpha=0.4)
# # line_1, = ax.plot(x_sc_1, y_sc_1,c='r',linestyle='', marker='.',markersize=5, alpha=0.8)
# # line_2, = ax.plot(x_sc_2, y_sc_2, c='c',linestyle='', marker='.',markersize=5, alpha=0.4)
#
# # initialization function: plot the background of each frame
#
# def init():
#     line_1.set_data([], [])
#     line_2.set_data([], [])
#     return line_1, line_2,
#
# "animation function.  This is called sequentially"
# def animate(i):
#     txt.set_text('{:d} * 100 years'.format(i))  # for debug purposes
#     new_x_1 = x_sc_1[:] + v_x[:] * i * 100
#     new_z_1 = z_sc_1[:] + v_z[:] * i * 100
#     # new_x_1 = x_sc_1 + v_x * i * 100
#     # new_z_1 = z_sc + v_z * i * 100
#
#     # new_x_2 = x_sc_2[:10000] + v_x[:10000] * i * 100
#     # new_z_2 = z[:10000] + v_z[:10000] * i * 100
#     new_x_2 = x_sc_2[:] + v_x[:] * i * 100
#     new_z_2 = z_sc_2[:] + v_z[:] * i * 100
#     line_1.set_data(new_x_1, new_z_1)
#     line_2.set_data(new_x_2, new_z_2)
#     return line_1, line_2,
#
# # def animate(i):
# #     txt.set_text('{:d} * 100 years'.format(i))  # for debug purposes
# #     new_x_1 = x_sc_1[:] + v_x[:] * i * 100
# #     new_y_1 = y_sc_1[:] + v_y[:] * i * 100
# #     # new_x_1 = x_sc_1 + v_x * i * 100
# #     # new_z_1 = z_sc + v_z * i * 100
# #
# #     # new_x_2 = x_sc_2[:10000] + v_x[:10000] * i * 100
# #     # new_z_2 = z[:10000] + v_z[:10000] * i * 100
# #     new_x_2 = x_sc_2[:] + v_x[:] * i * 100
# #     new_y_2 = y_sc_2[:] + v_y[:] * i * 100
# #     line_1.set_data(new_x_1, new_y_1)
# #     line_2.set_data(new_x_2, new_y_2)
# #     return line_1, line_2,
#
#
# # call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate,
#                                frames=frames, interval=50, blit=False, init_func=init)
#
# plt.xlim(-10,40)
# plt.ylim(-20,20)
#
# plt.show()

print('considered data points :',len(x))  # final number of data points that was used

stop = timeit.default_timer()
print("calculation time:", round(stop - start),"s")
