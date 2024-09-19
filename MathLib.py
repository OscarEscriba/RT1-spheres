import numpy as np
from math import pi, sin, cos, isclose

def barycentricCoords(A, B, C, P):
	
	# Se saca el area de los subtriangulos y del triangulo
	# mayor usando el Shoelace Theorem, una farmula que permite
	# sacar el area de un polagono de cualquier cantidad de vartices.
 
	areaPCB = abs((P[0]*C[1] + C[0]*B[1] + B[0]*P[1]) - 
				  (P[1]*C[0] + C[1]*B[0] + B[1]*P[0]))

	areaACP = abs((A[0]*C[1] + C[0]*P[1] + P[0]*A[1]) - 
				  (A[1]*C[0] + C[1]*P[0] + P[1]*A[0]))

	areaABP = abs((A[0]*B[1] + B[0]*P[1] + P[0]*A[1]) - 
				  (A[1]*B[0] + B[1]*P[0] + P[1]*A[0]))

	areaABC = abs((A[0]*B[1] + B[0]*C[1] + C[0]*A[1]) - 
				  (A[1]*B[0] + B[1]*C[0] + C[1]*A[0]))

	# Si el area del triangulo es 0, retornar nada para
	# prevenir divisian por 0.
	if areaABC == 0:
		return None

	# Determinar las coordenadas baricentricas dividiendo el 
	# area de cada subtri�ngulo por el area del triangulo mayor.
	u = areaPCB / areaABC
	v = areaACP / areaABC
	w = areaABP / areaABC


	# Si cada coordenada esta entre 0 a 1 y la suma de las tres
	# es igual a 1, entonces son validas.
	if 0<=u<=1 and 0<=v<=1 and 0<=w<=1:
		return (u, v, w)
	else:
		return None
	

def TranslationMatrix(x, y, z):
	
	return np.matrix([[1, 0, 0, x],
					  [0, 1, 0, y],
					  [0, 0, 1, z],
					  [0, 0, 0, 1]])

def ScaleMatrix(x, y, z):
	
	return np.matrix([[x, 0, 0, 0],
					  [0, y, 0, 0],
					  [0, 0, z, 0],
					  [0, 0, 0, 1]])

def RotationMatrix(pitch, yaw, roll):
	
	# Convertir a radianes
	pitch *= pi/180
	yaw *= pi/180
	roll *= pi/180
	
	# Creamos la matriz de rotaci�n para cada eje.
	pitchMat = np.matrix([[1,0,0,0],
						  [0,cos(pitch),-sin(pitch),0],
						  [0,sin(pitch),cos(pitch),0],
						  [0,0,0,1]])
	
	yawMat = np.matrix([[cos(yaw),0,sin(yaw),0],
						[0,1,0,0],
						[-sin(yaw),0,cos(yaw),0],
						[0,0,0,1]])
	
	rollMat = np.matrix([[cos(roll),-sin(roll),0,0],
						 [sin(roll),cos(roll),0,0],
						 [0,0,1,0],
						 [0,0,0,1]])
	
	return pitchMat * yawMat * rollMat
	

def reflectVector (normal, direction):
	#R = 2 * (N.L) * N-L
	reflect = 2* np.dot(normal,direction)
	reflect = np.multiply(reflect, normal)
	reflect = np.subtract(reflect, direction)
	reflect /= np.linalg.norm(reflect)
	return reflect

# Resta de vectores
def subVectors(v0, v1):
    return [v0[0] - v1[0], v0[1] - v1[1], v0[2] - v1[2]]

# Suma de vectores
def addVectors(v0, v1):
    return [v0[0] + v1[0], v0[1] + v1[1], v0[2] + v1[2]]

# Producto punto
def dotProduct(v0, v1):
    return v0[0] * v1[0] + v0[1] * v1[1] + v0[2] * v1[2]

# Multiplicación de un vector por un escalar
def scalarMultiply(v, scalar):
    return [v[0] * scalar, v[1] * scalar, v[2] * scalar]

# Normalización de un vector
def normalize(v):
    length = np.linalg.norm(v)
    if length == 0:
        return [0, 0, 0]
    return [v[0] / length, v[1] / length, v[2] / length]
