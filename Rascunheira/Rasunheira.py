from rsvg import rsvg
import numpy as np

def pext(d):
    A = np.zeros((d, d), dtype = complex); N = 0.0
    b=rsvg(d)
    bc=np.ndarray.conjugate(b)
    for l in range (0,d):
        for k in range (0,d):
            A[l][k]=(bc[l].real)*(b[k].real) + (bc[l].imag) * (b[k].imag)-1j*((bc[l].real) * (b[k].imag) - (bc[l].imag) * (b[k].real))
            N = N + (A[l][k].real) ** 2.0 + (A[l][k].imag) ** 2.0

    rdm=A/N
    print (N)
    return rdm
print(pext(2))
b = rsvg(2)
bc = np.conjugate(b)
print("ESPAÇO")
print(b)
print("ESPAÇO")
print(bc)
print("ESPAÇO")
aham= b*bc
print(aham)








# print(''ESPAÇO'')
# print(b)
# print(''ESPAÇO'')
# print(bc)
# print(''ESPAÇO'')
# print(N)
#   TRETA   (b[l].real)*(bc[k].real) + (b[l].imag) * (bc[k].imag) - 1j*((b[l].real) * (bc[k].imag) - (b[l].imag) * (bc[k].real))
# i=rsvg(2)
# h=np.conjugate(i)
# abelha=i*h
# print (abelha)
# def test():
#   from numpy import random, zeros;  random.seed()
#   from coherence import coh_l1n, coh_re
#   ns = 10**3 # number of samples for the average
#   nqb = 5 # maximum number of qubits regarded
#   Cavg = zeros(nqb);  d = zeros(nqb, dtype = int)
#   for j in range(0,nqb):
#     d[j] = 2**(j+1);
#     Cavg[j] = 0.0
#     for k in range(0,ns):
#       rdm = pext(d[j]);  Cavg[j] = Cavg[j] + coh_re(d[j], rdm)
#     Cavg[j] = Cavg[j]/ns
#   import matplotlib.pyplot as plt
#   plt.plot(d, Cavg, label = '')
#   plt.xlabel('d');  plt.ylabel('C');  plt.legend()
#   plt.show()
#
# test()
# from rdmg import    rdm_ginibre
# po=rdm_ginibre(3)
# print (po)