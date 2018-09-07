from numpy import matrix, cos, sin, pi

alphaG = 192.85948 * pi/180
deltaG = 27.12825 * pi/180
lOm = 32.93192 * pi/180

x = -lOm
A = matrix([ [ cos(x), -sin(x), 0 ],
             [ sin(x),  cos(x), 0 ],
             [        0,     0, 1 ] ])

x = pi/2 - deltaG
B = matrix([ [ 1,       0,       0 ],
             [ 0,  cos(x), -sin(x) ],
             [ 0,  sin(x),  cos(x) ] ])


x = alphaG + pi/2
C = matrix([ [ cos(x), -sin(x), 0 ],
             [ sin(x),  cos(x), 0 ],
             [      0,       0, 1 ] ])

S = matrix([ [  1,  0,  0 ],
             [  0, -1,  0 ],
             [  0,  0,  1 ] ])

M = S*A*B*C*S


