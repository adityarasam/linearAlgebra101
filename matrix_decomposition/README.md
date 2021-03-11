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
A = [[cos a -sin a],[sin a cos a]] 

so A will rotate vector X by 'a' deg to give A.X as shown in following figure

![Vector_transformation_with_Matrix_rotation](https://user-images.githubusercontent.com/34051411/110730097-dd99ab80-81ed-11eb-825c-b30421ec8f9a.png)

Fig. 1

Now say B = [[2 0],[0 9]]. B when multiplied to X will scale X, performing scaling transformation as shown in the Fig 2.

![Vector_transformation_with_Matrix_rotationA_scalingB](https://user-images.githubusercontent.com/34051411/110730204-0b7ef000-81ee-11eb-96b8-953528a56bae.png)

Fig. 2

### 2.2 Eigen Values and Eigen Vector

### 2.3 The thing with Symmetric matrices

### 2.4 Basis of Vector Space

### 2.5 Properties of a Symmetric matrix

## 3. Eigen Decomposition

### 3.1 Geometrical interpretation

3.1.1 Projection matrix

3.1.2 Rank

## 4. Singular Values

## 5. Singular Value Decomposition

