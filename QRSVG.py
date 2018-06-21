from numpy import zeros;from QRPV import Qrpv_zhsl;from math import pi, sqrt, cos, sin;from QRNG import QRNG
#--------------------------------------------------
def QRSVG(d):
  rn = zeros(d);rsv = zeros(d, dtype = complex)
  rpv = Qrpv_zhsl(d)
  tpi = 2.0*pi
  from QRNG import GetAnysizeRandomArray
  rn=GetAnysizeRandomArray(d)
  for j in range(0,d):
    arg = tpi*rn[j]
    ph = cos(arg) + (1j)*sin(arg)
    rsv[j] = sqrt(rpv[j])*ph
  return rsv
#------------------------------------------------------------------------------------------------------------------------------------
def test():
  from distances import fidelity_pp;  from numpy import zeros;
  ns = 10**2 # number of samples for the average
  nqb = 5 # maximum number of qubits regarded
  Favg = zeros(nqb);  Fexa = zeros(nqb);  d = zeros(nqb, dtype = int)
  for j in range(0,nqb):
    d[j] = 2**(j+1);  psi = zeros(d[j], dtype = complex);  phi = zeros(d[j], dtype = complex)
    Fexa[j] = 1.0/d[j]
    Favg[j] = 0.0
    for k in range(0,ns):
      psi = QRSVG(d[j]);  phi = QRSVG(d[j]);  Favg[j] = Favg[j] + fidelity_pp(psi, phi)
    Favg[j] = Favg[j]/ns
  import matplotlib.pyplot as plt
  plt.plot(d, Favg, label = '<F>');  plt.plot(d, Fexa, label = 'F')
  plt.xlabel('d');  plt.ylabel('F');  plt.legend()
  plt.show()
#------------------------------------------------------------------------------------------------------------------------------------
#test()
#print (QRSVG(10))
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# A PARTIR DAQUI É UTILIZANDO O ARQUIVO txt
#------------------------------------------------------------------------------------
import numpy as np;  from math import pi, sqrt, cos, sin;from distances import fidelity_pp;
data= np.genfromtxt("QNnormalized.txt",dtype=float)
def read0to1Data(d,int):      # Versão pronta
    #data= np.genfromtxt("QNnormalized.txt",dtype=float)
    k=np.zeros(d)
    aux=int*d
    aux2=(int+1)*d
    k=[float(data[i])for i in range(aux,aux2)]
    return k

def readRandomData(int):      # Versão pronta
    #data= np.genfromtxt("QNnormalized.txt",dtype=float)
    aux=int
    aux2=(int+1)
    k=float(data[int])
    return k

def StoragedQrpv_zhsl(d,int):
   rn = np.zeros(d-1)
   print(int)
   #data= np.genfromtxt("QNnormalized.txt",dtype=float)
   rn=read0to1Data(d,int)              # aqui tem que cuidar que desperdiça números do arquivo
   rpv = np.zeros(d)
   rpv[0] = 1.0 - rn[0]**(1.0/(d-1.0)) # linha para gerar o p1
   norm = rpv[0]
   if d > 2:
     for j in range(1,d-1):            # Loop para gerar do segundo ao penúltimo
       rpv[j] = (1.0 - rn[j]**(1.0/(d-j-1)))*(1.0-norm)
       norm = norm + rpv[j]
   rpv[d-1] = 1.0 - norm               # Linha para gerar a última probabilidade
   return rpv
#------------------------------------------------------------------------------------
def StoragedQRSVG(d,int):
  rn = np.zeros(d);  rpv = np.zeros(d);  rsv = np.zeros(d, dtype = complex);  tpi = 2.0*pi
  rpv = StoragedQrpv_zhsl(d,int)
  print(int)
  l=int+1
  print(l)
  for j in range(0,d):
      rn[j] = readRandomData(l)
      arg = tpi*rn[j];  ph = cos(arg) + (1j)*sin(arg)
      rsv[j] = sqrt(rpv[j])*ph
      l=l+j+1
  print(l)
  return rsv,l
#print(StoragedQRSVG(50,3))
#------------------------------------------------------------------------------------
def test():
  from distances import fidelity_pp;  from numpy import zeros;  from math import sqrt
  ns = 10**2 # number of samples for the average
  l=0
  nqb = 5 # maximum number of qubits regarded
  Favg = zeros(nqb);  Fexa = zeros(nqb);  d = zeros(nqb, dtype = int)
  for j in range(0,nqb):
    d[j] = 2**(j+1);  psi = zeros(d[j], dtype = complex);  phi = zeros(d[j], dtype = complex)
    Fexa[j] = 1.0/d[j]
    Favg[j] = 0.0
    for k in range(0,ns):
      psi,l = StoragedQRSVG(d[j],l);  phi,l = StoragedQRSVG(d[j],l);  Favg[j] = Favg[j] + fidelity_pp(psi, phi)
    Favg[j] = Favg[j]/ns
  import matplotlib.pyplot as plt
  plt.plot(d, Favg, label = '<F>');  plt.plot(d, Fexa, label = 'F')
  plt.xlabel('d');  plt.ylabel('F');  plt.legend()
  plt.show()

test()

#------------------------------------------------------------------------------------
# ---- ESSES DE CIMA ESTÃO ROLANO, OS DE BAIXO É RASCUNHO
#------------------------------------------------------------------------------------
'''import numpy as np;  from math import pi, sqrt, cos, sin;  from random import random;
data= np.genfromtxt("QNnormalized.txt",dtype=float)
def read0to1Data(d,int):      # Versão pronta
    #data= np.genfromtxt("QNnormalized.txt",dtype=float)
    k=np.zeros(d)
    aux=int*d
    aux2=(int+1)*d
    k=[float(data[i])for i in range(aux,aux2)]
    return k
#------------------------------------------------------------------------------------
def readRandomData(int):      # Versão pronta
    #data= np.genfromtxt("QNnormalized.txt",dtype=float)
    aux=int
    aux2=(int+1)
    k=float(data[int])
    return k
#------------------------------------------------------------------------------------
def StoragedQrpv_zhsl(d,int):
   rn = np.zeros(d-1)
   #data= np.genfromtxt("QNnormalized.txt",dtype=float)
   rn=read0to1Data(d,int)              # aqui tem que cuidar que desperdiça números do arquivo
   rpv = np.zeros(d)
   rpv[0] = 1.0 - rn[0]**(1.0/(d-1.0)) # linha para gerar o p1
   norm = rpv[0]
   if d > 2:
     for j in range(1,d-1):            # Loop para gerar do segundo ao penúltimo
       rpv[j] = (1.0 - rn[j]**(1.0/(d-j-1)))*(1.0-norm)
       norm = norm + rpv[j]
   rpv[d-1] = 1.0 - norm               # Linha para gerar a última probabilidade
   return rpv
#------------------------------------------------------------------------------------
def StoragedQRSVG(d,int):
  rn = np.zeros(d);  rpv = np.zeros(d);  rsv = np.zeros(d, dtype = complex);  tpi = 2.0*pi
  rpv = StoragedQrpv_zhsl(d,int)
  l=int+1
  print(l)
  for j in range(0,d):
      rn[j] = readRandomData(l)
      arg = tpi*rn[j];  ph = cos(arg) + (1j)*sin(arg)
      rsv[j] = sqrt(rpv[j])*ph
      l=l+j+1
  return rsv
print(StoragedQRSVG(5,2))
#------------------------------------------------------------------------------------
# ----  OS DE BAIXO É RASCUNHO
#------------------------------------------------------------------------------------
def QRSVG(d,int):
  rn = zeros(d);rsv = zeros(d, dtype = complex)
  rpv = Qrpv_zhsl(d)
  tpi = 2.0*pi
  data= np.genfromtxt("QNnormalized.txt",dtype=float)
  from QRNG import GetAnysizeRandomArray
  rn=GetAnysizeRandomArray(d)
  for j in range(0,d):
    arg = tpi*rn[j]
    ph = cos(arg) + (1j)*sin(arg)
    rsv[j] = sqrt(rpv[j])*ph
  return rsv
#------------------------------------------------------------------------------------
def test():
  from distances import fidelity_pp;  from numpy import zeros;
  ns = 10**2 # number of samples for the average
  nqb = 5 # maximum number of qubits regarded
  data= np.genfromtxt("QNnormalized.txt",dtype=float)
  Favg = zeros(nqb);  Fexa = zeros(nqb);  e = zeros(nqb, dtype = int)
  for j in range(0,nqb):
    e[j] = 2**(j+1);  psi = zeros(e[j], dtype = complex);  phi = zeros(e[j], dtype = complex)
    Fexa[j] = 1.0/e[j]
    Favg[j] = 0.0
    for k in range(1,ns):
      aux=k*(1+j)*e[k]
      aux2=(1+j)*(k+1)*e[k]
      rn=[float(data[i])for i in range(aux,aux2)]
      rpv = np.zeros(e[k])
      rpv[0] = 1.0 - rn[0]**(1.0/(d-1.0)) # linha para gerar o p1
      norm = rpv[0]
      if d > 2:
        for l in range(1,d-1):            # Loop para gerar do segundo ao penúltimo
          rpv[l] = (1.0 - rn[l]**(1.0/(e[k]-l-1)))*(1.0-norm)
          norm = norm + rpv[l]
      rpv[e[k]-1] = 1.0 - norm
      for m in range(0,e[k]):
        aux3=aux+k*(1+j)*e[k]
        aux4=aux2+(1+j)*(k+1)*e[k]
        rn=[float(data[i])for i in range(aux3,aux4)]
        arg = tpi*rn[m]
        ph = cos(arg) + (1j)*sin(arg)
        Qrsv[m] = sqrt(rpv[m])*ph
      psi = Qrsv(e[j],k);  phi = Qrsv(e[j],k);  Favg[j] = Favg[j] + fidelity_pp(psi, phi)
    Favg[j] = Favg[j]/ns
  import matplotlib.pyplot as plt
  plt.plot(d, Favg, label = '<F>');  plt.plot(d, Fexa, label = 'F')
  plt.xlabel('d');  plt.ylabel('F');  plt.legend()
  plt.show()
#------------------------------------------------------------------------------------
def QRSVG(d,int):
  rn = zeros(d);rsv = zeros(d, dtype = complex)
  rpv = Qrpv_zhsl(d,int)
  tpi = 2.0*pi
  from QRNG import GetAnysizeRandomArray
  rn=GetAnysizeRandomArray(d)
  rn=[float(data[i])for i in range()(d)]
  for j in range(0,d):
    arg = tpi*rn[j]
    ph = cos(arg) + (1j)*sin(arg)
    rsv[j] = sqrt(rpv[j])*ph
  return rsv
'''
