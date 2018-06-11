from rsvg import rsvg
import numpy as np


def vrdmg(d):
    A = np.zeros((d, d), dtype = complex); N = 0.0
    b=rsvg(d)
    bc=np.conjugate(b)
    for l in range (0,d):
        for k in range (0,d):
            A[l][k]=(b[l].real*bc[k].real)+(b[l].imag*bc[k].imag)+(1j)*(b[l].real*bc[k].imag + b[l].imag*bc[k].real)
    vrdm=A
    return vrdm
print(vrdmg(2))

