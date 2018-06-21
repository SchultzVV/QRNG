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
# A PARTIR DAQUI É UTILIZANDO O ARQUIVO txt   ainda não ta perfeito
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

def readRandomData(a):      # Versão pronta
    #data= np.genfromtxt("QNnormalized.txt",dtype=float)
    k=float(data[a])
    return k

def StoragedQrpv_zhsl(d,a):
   rn = np.zeros(d-1)
   #print('qrpv_int=',a)
   #data= np.genfromtxt("QNnormalized.txt",dtype=float)
   rn=read0to1Data(d,a)              # aqui tem que cuidar que desperdiça números do arquivo
   rpv = np.zeros(d)
   rpv[0] = 1.0 - rn[0]**(1.0/(d-1.0)) # linha para gerar o p1
   norm = rpv[0]
   if d > 2:
     for j in range(1,d-1):            # Loop para gerar do segundo ao penúltimo
       rpv[j] = (1.0 - rn[j]**(1.0/(d-j-1)))*(1.0-norm)
       norm = norm + rpv[j]
   rpv[d-1] = 1.0 - norm               # Linha para gerar a última probabilidade
   a=a+2
   return rpv,a
#------------------------------------------------------------------------------------
def StoragedQRSVG(d,a):
  rn = np.zeros(d);  rpv = np.zeros(d);  rsv = np.zeros(d, dtype = complex);  tpi = 2.0*pi
  rpv,a = StoragedQrpv_zhsl(d,a)
  #print('QRSV_int=',a)
  l=a+1
  #print('l=',l)
  for j in range(0,d):
      rn[j] =float(data[l])
      arg = tpi*rn[j];  ph = cos(arg) + (1j)*sin(arg)
      rsv[j] = sqrt(rpv[j])*ph
      l=l+j+1
      #print('l=',l)
  a=l+d
  return rsv,a
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
      psi,l = StoragedQRSVG(d[j],l)
      print(l)
      phi,l = StoragedQRSVG(d[j],l)
      print(l)
      Favg[j] = Favg[j] + fidelity_pp(psi, phi)
    Favg[j] = Favg[j]/ns
  import matplotlib.pyplot as plt
  plt.title('Fidelidade exata e entre dois Vetores de Estado')
  plt.plot(d, Favg, label = 'Fidelidade média');  plt.plot(d, Fexa, label = 'Fidelidade exata')
  plt.xlabel('Dimensão');  plt.ylabel('Fidelidade');  plt.legend()
  plt.show() # esse tá funcionando
test()
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# ---- PROGRAMINHAS SÓ PARA TESTAR E SE LIGAR
#------------------------------------------------------------------------------------
#_____________--------------____teste StoragedQRSVG___---------___________________---
def teste_do_teste(dim,loop):
    a=0
    for i in range (0,loop):
        a=a+i
        g,a=StoragedQRSVG(dim,a)
        print(g)
        print(a)
        #b
#teste_do_teste(50,5)
#------------------------------------------------------------------------------------
# ---- ESSES DE CIMA ESTÃO ROLANO, OS DE BAIXO É RASCUNHO
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
'''import numpy as np;  from math import pi, sqrt, cos, sin;from distances import fidelity_pp;
#data= np.genfromtxt("QNnormalized.txt",dtype=float)
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
   print('qrpv_int=',int)
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
   int=int+2
   return rpv,int
#------------------------------------------------------------------------------------
def StoragedQRSVG(d,int):
  rn = np.zeros(d);  rpv = np.zeros(d);  rsv = np.zeros(d, dtype = complex);  tpi = 2.0*pi
  rpv,int = StoragedQrpv_zhsl(d,int)
  print('QRSV_int=',int)
  l=int+1
  print('l=',l)
  for j in range(0,d):
      rn[j] = readRandomData(l)
      arg = tpi*rn[j];  ph = cos(arg) + (1j)*sin(arg)
      rsv[j] = sqrt(rpv[j])*ph
      l=l+j+1
      print('l=',l)
  int=l+d+1
  return rsv,int
#print(StoragedQRSVG(50,3))
#_____________--------------____teste StoragedQRSVG___---------___________________---
def teste_do_teste(dim,loop):
    int=0
    for i in range (0,loop):
        int=int+i
        a,int=StoragedQRSVG(dim,int)
        print(a)
        print(int)
        #b
#teste_do_teste(50,5)
#------------------------------------------------------------------------------------
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
  plt.title('Fidelidade exata e de dois Vetores de Estado')
  plt.plot(d, Favg, label = 'Fidelidade média');  plt.plot(d, Fexa, label = 'Fidelidade exata')
  plt.xlabel('Dimensão');  plt.ylabel('Fidelidade');  plt.legend()
  plt.show() # esse tá funcionando
#test()
#------------------------------------------------------------------------------------
def test():
  from distances import fidelity_pp;  from numpy import zeros;  from math import sqrt
  ns = 10**2 # number of samples for the average
  nqb = 5 # maximum number of qubits regarded
  d = zeros(nqb,dtype=int)
  int=0
  Favg = zeros(nqb);  Fexa = zeros(nqb);
  for j in range(0,nqb):
    d[j] = 2**(j+1);  psi = zeros(d[j], dtype = complex);  phi = zeros(d[j], dtype = complex)
    Fexa[j] = 1.0/d[j]
    Favg[j] = 0.0
    for k in range(0,ns):
      int=int+k
      psi,int = StoragedQRSVG(d[j],int);  phi,int = StoragedQRSVG(d[j],int);  Favg[j] = Favg[j] + fidelity_pp(psi, phi)
    Favg[j] = Favg[j]/ns
  import matplotlib.pyplot as plt
  plt.plot(d, Favg, label = 'Fidelidade média');  plt.plot(d, Fexa, label = 'F')
  plt.xlabel('d');  plt.ylabel('F');  plt.legend()
  plt.show()

#test()'''
