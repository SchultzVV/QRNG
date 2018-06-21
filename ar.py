import numpy as np
from QRNG import GetAnysizeArray
def Contador(a):       # Programa auxiliar apenas para criar o eixo das
    #a=int(dmax-d)           # coordenadas que será usado no gráfico do teste
    x=np.zeros(a)
    x[0]=1
    for i in range(1,a):
        z=int(i+1)
        x[i]=z
    return x
#print(Contador(2))
#print(Contador(50))
#------------------------------------------------------------------------------------------------------------------------------------
#data= np.genfromtxt("QNnormalized.txt",dtype=float)
'''def QRSVG(d,int):
  rn = np.zeros(d);rsv = np.zeros(d, dtype = complex)
  rpv = Qrpv_zhsl(d,int)
  tpi = 2.0*pi
  l=0
  from QRNG import GetAnysizeRandomArray
  rn=GetAnysizeRandomArray(d)
  rn=[float(data[i])for i in range()(d)]
  for j in range(0,d):
    arg = tpi*rn[j]
    ph = cos(arg) + (1j)*sin(arg)
    rsv[j] = sqrt(rpv[j])*ph
  return rsv'''

'''def test_QRPVG():
  d = 6
  l=0
  ns = 10**2
  ni = 40
  data= np.genfromtxt("QNnormalized.txt",dtype=float)
  delta = 1.0/ni
  avg_rpv = np.zeros(d)
  ct = np.zeros((ni,d))
  for j in range(0, ns):
    l=j                                 # l=ns
    rn=np.zeros(d)
    aux=l*d+1
    aux2=(l+1)*d
    rn=[float(data[i])for i in range(aux,aux2)]
    rpv = np.zeros(d)
    rpv[0] = 1.0 - rn[0]**(1.0/(d-1.0)) # linha para gerar o p1
    norm = rpv[0]
    if d > 2:
      for j in range(1,d-1):            # Loop para gerar do segundo ao penúltimo
        rpv[j] = (1.0 - rn[j]**(1.0/(d-j-1)))*(1.0-norm)
        norm = norm + rpv[j]
    rpv[d-1] = 1.0 - norm               # Linha para gerar a última probabilidade
    avg_rpv = avg_rpv + rpv
    for k in range(0, d):
      if rpv[k] == 1.0:
        rpv[k] = 1.0 - 1/(10**10)
      for l in range(0, ni):
        if rpv[k] >= l*delta and rpv[k] < (l+1)*delta:
          ct[l][k] = ct[l][k] + 1
  avg_rpv = avg_rpv/ns
  if ( d < 7 ):
    print('avg_rpv = ', avg_rpv)
  x = np.zeros(ni);  y1 = np.zeros(ni);  y2 = np.zeros(ni);  y3 = np.zeros(ni);  y4 = np.zeros(ni);  y5 = np.zeros(ni)
  for l in range(0, ni):
    x[l] = l*delta;  y1[l] = ct[l][0]/ns;  y2[l] = ct[l][1]/ns;  y3[l] = ct[l][2]/ns;  y4[l] = ct[l][3]/ns;  y5[l] = ct[l][4]/ns
  import matplotlib.pyplot as plt;
  plt.plot(x,y1,label='p1');
  plt.plot(x,y2,label='p2');
  plt.plot(x,y3,label='p3')
  plt.plot(x,y4,label='p4')
  plt.plot(x,y5,label='p5')
  axes = plt.gca();  axes.set_xlim([0,1]);  axes.set_ylim([0,0.1])
  plt.xlabel('pj');  plt.ylabel('');  plt.legend();  plt.show()'''
#test_QRPVG()
'''def testQRSVG():
  from distances import fidelity_pp;  from numpy import zeros;
  ns = 10**2 # number of samples for the average
  nqb = 5 # maximum number of qubits regarded
  data= np.genfromtxt("QNnormalized.txt",dtype=float)
  Favg = zeros(nqb);  Fexa = zeros(nqb);  e = zeros(nqb, dtype = int)
  l=0
  for j in range(0,nqb):
    e[j] = 2**(j+1);  psi = zeros(e[j], dtype = complex);  phi = zeros(e[j], dtype = complex)
    Fexa[j] = 1.0/e[j]
    Favg[j] = 0.0
    for k in range(0,ns):
      l=k
      aux=l*d+1
      aux2=(l+1)*d
      #aux=k*(1+j)*e[k]
      #aux2=(1+j)*(k+1)*e[k]
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
        l=l+m
        aux=l*d+1
        aux2=(l+1)*d
        #aux3=aux+k*(1+j)*e[k]
        #aux4=aux2+(1+j)*(k+1)*e[k]
        rn=[float(data[i])for i in range(aux,aux2)]
        arg = tpi*rn[m]
        ph = cos(arg) + (1j)*sin(arg)
        Qrsv[m] = sqrt(rpv[m])*ph
      psi = Qrsv(e[j],k);  phi = Qrsv(e[j],k);  Favg[j] = Favg[j] + fidelity_pp(psi, phi)
    Favg[j] = Favg[j]/ns
  import matplotlib.pyplot as plt
  plt.plot(d, Favg, label = '<F>');  plt.plot(d, Fexa, label = 'F')
  plt.xlabel('d');  plt.ylabel('F');  plt.legend()
  plt.show()'''
data= np.genfromtxt("QNnormalized.txt",dtype=float)
def StoragedQrpv_zhsl(d,int):
   rn = np.zeros(d-1)
   #data= np.genfromtxt("QNnormalized.txt",dtype=float)
   k=np.zeros(d)
   aux=int*d
   aux2=(int+1)*d
   rn=[float(data[i])for i in range(aux,aux2)]
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
  import numpy as np;  from math import pi, sqrt, cos, sin;  from random import random;  from QRNG import read0to1Data
  rn = np.zeros(d);  rpv = np.zeros(d);  rsv = np.zeros(d, dtype = complex);  tpi = 2.0*pi
  rpv = StoragedQrpv_zhsl(d,int)
  l=int+1
  for j in range(0,d):
      a=float(read0to1Data(1,l))
      rn[j] = a
      arg = tpi*rn[j]
      ph = cos(arg) + (1j)*sin(arg)
      rsv[j] = sqrt(rpv[j])*ph
      l=l+j+1
  return rsv
 print(StoragedQRSVG(5,2))
#------------------------------------------------------------------------------------
def QRSVG_test():
  from distances import fidelity_pp;  from numpy import zeros;  from math import sqrt
  ns = 10**3 # number of samples for the average
  nqb = 5 # maximum number of qubits regarded
  Favg = zeros(nqb);  Fexa = zeros(nqb);  d = zeros(nqb, dtype = int)
  for j in range(0,nqb):
    d[j] = 2**(j+1);  psi = zeros(d[j], dtype = complex);  phi = zeros(d[j], dtype = complex)
    Fexa[j] = 1.0/d[j]
    Favg[j] = 0.0
    for k in range(0,ns):
        l=k
        psi = StoragedQRSVG(d[j],l)
        l=l+1
        phi = StoragedQRSVG(d[j],l)
        Favg[j] = Favg[j] + fidelity_pp(psi, phi)
    Favg[j] = Favg[j]/ns
  import matplotlib.pyplot as plt
  plt.plot(d, Favg, label = '<F>');  plt.plot(d, Fexa, label = 'F')
  plt.xlabel('d');  plt.ylabel('F');  plt.legend()
  plt.show()
#QRSVG_test()
'''def testQRSVG():
  from distances import fidelity_pp;  from numpy import zeros;
  ns = 10**2 # number of samples for the average
  nqb = 5 # maximum number of qubits regarded
  data= np.genfromtxt("QNnormalized.txt",dtype=float)
  Favg = zeros(nqb);  Fexa = zeros(nqb);  e = zeros(nqb, dtype = int)
  l=0
  for j in range(0,nqb):
    e[j] = 2**(j+1);  psi = zeros(e[j], dtype = complex);  phi = zeros(e[j], dtype = complex)
    Fexa[j] = 1.0/e[j]
    Favg[j] = 0.0
    for k in range(0,ns):
      l=k
      aux=l*d+1
      aux2=(l+1)*d
      #aux=k*(1+j)*e[k]
      #aux2=(1+j)*(k+1)*e[k]
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
        l=l+m
        aux=l*d+1
        aux2=(l+1)*d
        #aux3=aux+k*(1+j)*e[k]
        #aux4=aux2+(1+j)*(k+1)*e[k]
        rn=[float(data[i])for i in range(aux,aux2)]
        arg = tpi*rn[m]
        ph = cos(arg) + (1j)*sin(arg)
        Qrsv[m] = sqrt(rpv[m])*ph
      psi = Qrsv(e[j],k);  phi = Qrsv(e[j],k);  Favg[j] = Favg[j] + fidelity_pp(psi, phi)
    Favg[j] = Favg[j]/ns
  import matplotlib.pyplot as plt
  plt.plot(d, Favg, label = '<F>');  plt.plot(d, Fexa, label = 'F')
  plt.xlabel('d');  plt.ylabel('F');  plt.legend()
  plt.show()'''
#------------------------------------------------------------------------------------
