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