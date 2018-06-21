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
'''def test():
  l=0
  ns = 10**3 # number of samples for the average
  nqb = 5 # maximum number of qubits regarded
  Favg = np.zeros(nqb);  Fexa = np.zeros(nqb);  d = np.zeros(nqb, dtype = int)
  for j in range(0,nqb):
    d[j] = 2**(j+1);  psi = np.zeros(d[j], dtype = complex);  phi = np.zeros(d[j], dtype = complex)
    Fexa[j] = 1.0/d[j]
    Favg[j] = 0.0
    for k in range(0,ns):
        psi = StoragedQRSVG(d[j],l)
        l=+1
        phi = StoragedQRSVG(d[j],l)
        l=+1
        Favg[j] = Favg[j] + fidelity_pp(psi, phi)
    Favg[j] = Favg[j]/ns
  import matplotlib.pyplot as plt
  plt.plot(d, Favg, label = '<F>');  plt.plot(d, Fexa, label = 'F')
  plt.xlabel('d');  plt.ylabel('F');  plt.legend()
  plt.show()'''
def test():
  from distances import fidelity_pp;  from numpy import zeros;  from math import sqrt
  ns = 10**1 # number of samples for the average
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
