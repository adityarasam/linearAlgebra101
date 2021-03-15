# Matrix Decomposition

## 1. Introduction
Matrix decomposition or Matrix factorization, is a factorization of a matrix into a product of matrices. Its a way of reducing a matrix into its constituting parts. Each part has interesting algebraic properties and convey important geometrical insight.

### 1.1. Why do we do Matrix Decomposition
Many complex matrix operations cannot be solved efficiently/stably with limited precision of computers. Matrix decompositions are methods that reduce matrix into constituent parts that make it easier to calculate more complex matrix operations. Matrix decompositions are foundations of linear algebra in computers even for basic operations such as solving system of linear equations, calculating inverse and determinant of a matrix.  

### 1.2 Types

## 2. Eigen 

### 2.1 Matrix as a transformation on a vector
Consider a vector X = [1 0]. Any matrix A when multiplied with a vector X, can be thought of as a transformation on the vector X to produce a new vector A.X.

Lets say A is a 2d-rotation matrix
A = [[cos a  -sin a],[sin a  cos a]] 

so A will rotate vector X by 'a' deg to give A.X as shown in following figure (a=45 deg)

![Vector_transformation_with_Matrix_rotation](https://user-images.githubusercontent.com/34051411/110730097-dd99ab80-81ed-11eb-825c-b30421ec8f9a.png)

Fig. 1

Now say B = [[2 0],[0 9]]. B when multiplied to X will scale X, performing scaling transformation as shown in the Fig 2.

![Vector_transformation_with_Matrix_rotationA_scalingB](https://user-images.githubusercontent.com/34051411/110730204-0b7ef000-81ee-11eb-96b8-953528a56bae.png)

Fig. 2


Here matrix A performs rotation and scaling(shrinking) of vector X while B performs only scaling. If a matrix only performs a scaling transformation on any vector (on multiplication), then that vector is eigen vector of that matrix, and the amount of scaling is the eigen value.Here B does not change the direction of X but only scales it in its direction, So X can be called as eigen vector of B with 2 as the corresponding eigen value.

### 2.2 Eigen Values and Eigen Vector

Now lets consider a matrix C = [[3 2],[0 2]] and a group of vectors that represents a circle with unit radius. The vectors have general form X = [xi,yi] where xi^2 + yi^2 = 1. Multiplying these vectors with C gives following mapping from left figure to right

![eigen_explanation](https://user-images.githubusercontent.com/34051411/111101813-0d63ee80-8521-11eb-8769-3ffc5c8d934b.png)

Consider two sample vectors x1 and x2 which get mapped to Cx1 and Cx2. Here for x1 both magnitude and direction changes but for x2 only magnitude changes while direction is retained. So for vectors like x2 which only undergo change in magnitude on multiplying by C can be seen equivalent as to getting multiplied by a scalar lambda λ.  
```
Cx2 = λ.x2
```
This is not true for all the vectors of X. In fact for matrix C only some of the vectors of X satisfy this property/constraint. These special vectors are called as eigen vectors and their corresponding scaling factor 'λ' is called eigen value.

**Definition: So the eigenvector of an n×n matrix C is defined as a nonzero vector u such that **
```
C.u = λ.u
```
### 2.3 The thing with Symmetric matrices

### 2.4 Basis of Vector Space

### 2.5 Properties of a Symmetric matrix

## 3. Eigen Decomposition

### 3.1 Geometrical interpretation

3.1.1 Projection matrix

3.1.2 Rank

## 4. Singular Values

## 5. Singular Value Decomposition

