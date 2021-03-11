import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11
M = 1.989e30
m = 5.972e24
R = 1.496e11
omega = 1.991e-7

def fplus(r):
    '''Function to find L2'''
    return (((G*M)/r**2)+((G*m)/(R-r)**2)) - (omega**2*r)

def fminus(r):
    '''Function to find L1'''
    return (((G*M)/r**2)-((G*m)/(R-r)**2)) - (omega**2*r)

def fplusPrime(r):
    '''Derivative of fplus'''
    return ((((-2*G*M)/r**3)+((2*G*m)/(R-r)**3)) - omega**2)

def fminusPrime(r):
    '''Derivative of fminus'''
    return (((-2*G*M)/r**3)-((2*G*m)/(R-r)**3) - omega**2)

def newtonsMethod(func=None, deriv=None, startGuess=1, maxIter=100):
    '''Function to find the root using Newton's method'''
    for i in range(maxIter):
        startGuess = startGuess - (func(startGuess)/deriv(startGuess))
        #print(startGuess)
    return startGuess

def secantMethod(func=None, startGuess=10000, step=1, maxIter=100):
    '''Function to find the root using Secant Method.'''
    for i in range(maxIter):
        x2 = startGuess + step
        startGuess = x2 - (func(x2)*((x2-startGuess)/(func(x2)-func(startGuess))))
        #print(startGuess)
    return startGuess
    
if __name__ == '__main__':
    L1 = abs(R - newtonsMethod(fminus, fminusPrime, startGuess=1e6))
    L2 = abs(R-newtonsMethod(fplus, fplusPrime, startGuess=1e8))
    print('Lagrange 1 from Newtons Method is',L1)
    print('Lagrange 2 from Newtons Method is', L2)
    L1secant = abs(R-secantMethod(fminus))
    L2secant = abs(R-secantMethod(fplus))
    print('Lagrange1 from Secant Method is', L1secant)
    print('Lagrange2 from Secant Method is', L2secant)



    
    
    
    
