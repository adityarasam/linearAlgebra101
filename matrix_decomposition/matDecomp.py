import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import math 
from numpy import linalg 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import fetch_olivetti_faces

PI = math.pi
debug = "false"

X=np.array([1,0])
theta = 45 * PI / 180

A = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta),  np.cos(theta)]])
if(debug=="true"):
    print(X)
    print(A)
    print(A@X)

AX  = A@X

tmp = np.concatenate([X.reshape(1,2), AX.reshape(1,2)])
if(debug=="true"):
    print("tmp",tmp)
    print("tmp[:,0], tmp[:,1]",tmp[:,0], tmp[:,1])
orig = [0,0]


fig, ax1 = plt.subplots(1,1,  figsize=(5,5))
plt.subplots_adjust(wspace=0.4)


# Plotting tmp

ax1.quiver(orig,orig, tmp[:,0], tmp[:,1], angles='xy', width=0.008,scale_units='xy', scale=1, color=['b', 'g'])

ax1.set_xlabel('x', fontsize=14)
ax1.set_ylabel('y', fontsize=14)
ax1.set_xlim([-1.5,1.5])
ax1.set_ylim([-1.5,1.5])

ax1.set_aspect('equal')
ax1.grid(True)
ax1.set_axisbelow(True)
ax1.set_title("Rotation (A) transform")
ax1.axhline(y=0, color='k')
ax1.axvline(x=0, color='k')
ax1.text(1, 0.1, "$\mathbf{X}$", fontsize=16)
ax1.text(0.8, 0.8, "$\mathbf{AX}$", fontsize=16)

plt.savefig('Vector_transformation_with_Matrix_rotation.png')


B = np.array([[2,0],[0,9]])
BX  = B@X

tmp = np.concatenate([tmp, BX.reshape(1,2)])
#if(debug=="true"):
print("tmpB", tmp)

orig = [0,0,0]
ax1.quiver(orig,orig, tmp[:,0], tmp[:,1], angles='xy', width=0.008,scale_units='xy', scale=1, color=['b', 'g', 'orange'])

ax1.set_xlabel('x', fontsize=14)
ax1.set_ylabel('y', fontsize=14)
ax1.set_xlim([-2.5,2.5])
ax1.set_ylim([-2.5,2.5])

ax1.set_aspect('equal')
ax1.grid(True)
ax1.set_axisbelow(True)
ax1.set_title("Rotation (A), Scaling (B) transform")
ax1.axhline(y=0, color='k')
ax1.axvline(x=0, color='k')
ax1.text(1, 0.1, "$\mathbf{X}$", fontsize=16)
ax1.text(0.8, 0.8, "$\mathbf{AX}$", fontsize=16)
ax1.text(2, 0.1, "$\mathbf{BX}$", fontsize=16)
plt.savefig('Vector_transformation_with_Matrix_rotationA_scalingB.png')




#eigen

xi1 = np.linspace(-1.0, 1.0, 100)
xi2 = np.linspace(1.0, -1.0, 100)
yi1 = np.sqrt(1 - xi1**2)
yi2 = -np.sqrt(1 - xi2**2)
xi = np.concatenate((xi1, xi2),axis=0)
yi = np.concatenate((yi1, yi2),axis=0)
x = np.vstack((xi, yi))


x_sample1 = x[:, 65]
x_sample2 = x[:, 100]
C = np.array([[3, 2], [0, 2]])


CX = C@x # Vectors in t are the transformed vectors of x
CX_sample1 = CX[:, 65]
CX_sample2 = CX[:, 100]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,15))
plt.subplots_adjust(wspace=0.4)
# Plotting x
ax1.plot(x[0,:], x[1,:], color='black')
orig = [0,0]
ax1.quiver(orig,orig, x_sample1[0], x_sample1[1], color=['b'], width=0.008, angles='xy', scale_units='xy', scale=1)
ax1.quiver(orig,orig, x_sample2[0], x_sample2[1], color=['g'], width=0.008, angles='xy', scale_units='xy', scale=1)
ax1.set_xlabel('x', fontsize=14)
ax1.set_ylabel('y', fontsize=14)
ax1.set_xlim([-4,4])
ax1.set_ylim([-4,4])
ax1.set_aspect('equal')
ax1.grid(True)
ax1.set_axisbelow(True)
ax1.set_title("Original vectors")
ax1.axhline(y=0, color='k')
ax1.axvline(x=0, color='k')
ax1.text(0.3, 1.2, "$\mathbf{x_1}$", color='b', fontsize=14)
ax1.text(1.2, 0.2, "$\mathbf{x_2}$", color='g', fontsize=14)




ax2.plot(CX[0, :], CX[1, :], color='black')
ax2.quiver(orig,orig, CX_sample1[0], CX_sample1[1], color=['b'], width=0.008, angles='xy', scale_units='xy', scale=1)
ax2.quiver(orig,orig, CX_sample2[0], CX_sample2[1], color=['g'], width=0.008, angles='xy', scale_units='xy', scale=1)
ax2.set_xlabel('x', fontsize=14)
ax2.set_ylabel('y', fontsize=14)


ax2.set_xlim([-4,4])
ax2.set_ylim([-4,4])
ax2.set_aspect('equal')
ax2.grid(True)
ax2.set_axisbelow(True)
ax2.set_title("New vectors after transformation")
ax2.axhline(y=0, color='k')
ax2.axvline(x=0, color='k')
ax2.text(2.5, 2.3, "$\mathbf{Cx_1}$", color='b', fontsize=14)
ax2.text(2.6, 0.4, "$\mathbf{Cx_2}$", color='g', fontsize=14)
plt.savefig('eigen_explanation.png', dpi=300, bbox_inches='tight')