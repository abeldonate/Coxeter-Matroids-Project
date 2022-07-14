import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull 


tau = np.array([1,0,0,0])
s1 = np.array([1,1,0,0])
s2 = np.array([0,1,1,0])
s3 = np.array([0,0,1,1])

v = np.array([1,1,1,1])

#def reflect(point, plane):
#    return point -2*plane*(np.dot(plane, point))/(np.dot(plane, plane))

def ref(point, *plane):
    for rho in plane:
        point = point -2*rho*(np.dot(rho, point))/(np.dot(rho, rho))
    return point 


print(ref(v, s1, s2, s1, s2, s1, s2))
print(ref(v, tau, s2, tau, s2, tau, s2, tau, s2))

print(ref(v, tau, s2, tau, s2))


#Graphic design is my passion
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

points= np.array([[0,0,0],
            [4,0,0],
            [4,4,0],
            [0,4,0],
            [0,0,4],
            [4,0,4],
            [4,4,4],
            [0,4,4]])

hull=ConvexHull(points)


for i in hull.simplices:
    plt.plot(points[i,0], points[i,1], points[i,2], 'r-')


plt.show()

