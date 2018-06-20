from QRNG import GetAnysizeArray; import math; from plots import plotScatter; from QRNG import Contador; import random as rd
import numpy as np
from numpy import random
from QRNG import GetAnysizeArrayNormalized
from plots import plotScatterQ
def TDtE(a,d):
    #q=GetAnysizeArray(d)
    q=[rd.random() for i in range(0,d)]
    x=Contador(0,d)
    e=2.718281828459
    y=[(-1/a) * math.log(q[i])for i in range(0,d)]
    plotScatter(x,y)

def Gaussian():
    u1=rd.random()
    u2=rd.random()
    x=np.sqrt(-2*math.log(u2))*math.cos(2*math.pi*u1)
    y=np.sqrt(-2*math.log(u2))*math.sin(2*math.pi*u1)
    print (u1,u2)
    print (x,y)

def testPRNGaussian(d):
    D=[rd.random() for i in range(0,d)]
    x=np.zeros(d,dtype = complex)
    for i in range(0,d,2):
        x[i]=np.sqrt(-2*math.log(D[i+1]))*math.cos(2*math.pi*D[i])
        x[i+1]=np.sqrt(-2*math.log(D[i+1]))*math.sin(2*math.pi*D[i])
    dim=Contador(0,d)
    plotScatterQ(x,dim)

def testQRNGaussian(d):
    D=GetAnysizeArray(d)
    aux=np.zeros(d)
    for i in range(0,d):    # Looping para limitar o vetor entre [0,1)
        aux[i]=65535        # O teste requer valores neste intervalo...
    D=D/aux
    x=np.zeros(d,dtype = complex)
    for i in range(0,d,2):
        x[i]=np.sqrt(-2*math.log(D[i+1]))*math.cos(2*math.pi*D[i]) # x=
        x[i+1]=np.sqrt(-2*math.log(D[i+1]))*math.sin(2*math.pi*D[i])
    dim=Contador(0,d)
    plotScatterQ(x,dim)
#####################################################################
#--------------------------------------------------------------------
#####################################################################
#------------------------------------------------------------------------------------------------------------------------------------
def test():
  from numpy import random, zeros;  random.seed()
  from coherence import coh_l1n, coh_re
  ns = 10**3 # number of samples for the average
  nqb = 5 # maximum number of qubits regarded
  Cavg = zeros(nqb);  d = zeros(nqb, dtype = int)
  for j in range(0,nqb):
    d[j] = 2**(j+1);  rdm = zeros((d[j],d[j]), dtype = complex)
    Cavg[j] = 0.0
    for k in range(0,ns):
      rdm = rdm_ginibre(d[j]);  Cavg[j] = Cavg[j] + coh_re(d[j], rdm)
    Cavg[j] = Cavg[j]/ns
  import matplotlib.pyplot as plt
  plt.plot(d, Cavg, label = '')
  plt.xlabel('d');  plt.ylabel('C');  plt.legend()
  plt.show()
#------------------------------------------------------------------------------------------------------------------------------------
def rdm_ginibre(d):
  from numpy import zeros;  rdm = zeros((d,d), dtype = complex);  G = ginibre(d)
  from distances import normHS;  N2 = (normHS(d, G))**2.0
  for j in range(0,d):
    for k in range(0,d):
      rdm[j][k] = 0.0
      for l in range(0,d):
        rdm[j][k] = rdm[j][k] + (G[j][l].real)*(G[k][l].real) + (G[j][l].imag)*(G[k][l].imag) \
                              - (1j)*((G[j][l].real)*(G[k][l].imag) - (G[j][l].imag)*(G[k][l].real))
      rdm[j][k] = rdm[j][k]/N2
  return rdm
#------------------------------------------------------------------------------------------------------------------------------------
def ginibre(d):
  from numpy import random, zeros;  G = zeros((d,d), dtype = complex)
  from QRNG import QRNGGaussian
  for j in range(0,d):
    grn = QRNGGaussian(2*d)
    for k in range(0,d):
      G[j][k] = grn[k] + (1j)*grn[k+d]
  return G
test()
#####################################################################
#--------------------------------------------------------------------
#####################################################################
def rdm_ginibre(d):
  from numpy import zeros;  rdm = zeros((d,d), dtype = complex);  G = ginibre(d)
  from distances import normHS;  N2 = (normHS(d, G))**2.0
  for j in range(0,d):
    for k in range(0,d):
      rdm[j][k] = 0.0
      for l in range(0,d):
        rdm[j][k] = rdm[j][k] + (G[j][l].real)*(G[k][l].real) + (G[j][l].imag)*(G[k][l].imag) \
                              - (1j)*((G[j][l].real)*(G[k][l].imag) - (G[j][l].imag)*(G[k][l].real))
      rdm[j][k] = rdm[j][k]/N2
  return rdm
#------------------------------------------------------------------------------------------------------------------------------------
def ginibre(d):
  from QRNG import PRNGGaussian
  from numpy import zeros
  G = zeros((d,d), dtype = complex);
  for j in range(0,d):
    grn = PRNGGaussian(2*d)
    for k in range(0,d):
      G[j][k] = grn[k] + (1j)*grn[k+d]
  return G
