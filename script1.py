from math import *

def formula1(alpha):

    z1 = 1 - 0.25 * (sin(2 * alpha)**2) + cos(2 * alpha)
    print("{0:.4f}".format(z1))

def formula2(alpha):


    z2 = (cos(alpha) ** 2) + (cos(alpha) ** 4)
    print("{0:.4f}".format(z2))


a = float(input("Введите параметр a: "))
formula1(a)
formula2(a)