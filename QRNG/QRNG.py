import urllib.request;import numpy as np;import json;from plots import plotScatter;from plots import plotScatter2;from plots import plotHistogram
#------------------------------------------------------------------------------------
def GetRandomArray(dim):
    d=str(dim)
    url1 = 'https://qrng.anu.edu.au/API/jsonI.php?length='
    url2 = '&type=uint16'
    url = url1+d+url2
    page = urllib.request.urlopen(url, timeout=100000)
    aux = page.read()
    data = json.loads(aux.decode('utf-8'))
    num = data.get("data", "none")
    return num   # Programa que comunica com o site e recebe os dados
#print("GetRandomArray(12)")
#print(GetRandomArray(12))
#------------------------------------------------------------------------------------
def GetAnysizeArray(dim):
   if dim <= 1024:
       little = GetRandomArray(dim)
       return little
   else:
       large = []
       m = dim
       while m > 1024:
           large.extend(GetRandomArray(1024))
           m = m - 1024
       else:
           large.extend(GetRandomArray(m))
           return large  # Gera um array de qualquer tamanho com os dados do site
#print("GetAnysizeArray(12)")
#print(GetAnysizeArray(12))
#------------------------------------------------------------------------------------
def QRNG():
    a=float(GetRandomArray(1)[0])
    b=float(a/65535)
    return b                # Programa que gera 1 valor normalizado
#------------------------------------------------------------------------------------
def QRNGGaussian(d):
    import math
    D=GetAnysizeArray(d)
    aux=np.zeros(d)
    for i in range(0,d):    # Looping para limitar o vetor entre [0,1)
        aux[i]=65535        # O teste requer valores neste intervalo...
    D=D/aux
    x=np.zeros(d,dtype = complex)
    for i in range(0,d,2):
        x[i]=np.sqrt(-2*math.log(D[i+1]))*math.cos(2*math.pi*D[i])
        x[i+1]=np.sqrt(-2*math.log(D[i+1]))*math.sin(2*math.pi*D[i])
    return x
#------------------------------------------------------------------------------------
def PRNGGaussian(d):
    import math; import random as rd
    D=[rd.random() for i in range (0,d)]
    x=np.zeros(d,dtype = complex)
    for i in range(0,d,2):
        x[i]=np.sqrt(-2*math.log(D[i+1]))*math.cos(2*math.pi*D[i])
        x[i+1]=np.sqrt(-2*math.log(D[i+1]))*math.sin(2*math.pi*D[i])
    return x
#------------------------------------------------------------------------------------
def Qginibre(d):
  from QRNG import QRNGGaussian
  from numpy import zeros
  G = zeros((d,d), dtype = complex);
  for j in range(0,d):
    grn = QRNGGaussian(2*d)
    for k in range(0,d):
      G[j][k] = grn[k] + (1j)*grn[k+d]
  return G
#------------------------------------------------------------------------------------
def GetAnysizeArrayNormalized(d): # Faz a soma de todos as componentes = 1
    D=GetAnysizeArray(d)
    aux=[sum(D)for i in range(0,d)]
    F=[D[i]/aux[i]for i in range(0,d)]
    return F
#print("GetAnysizeArrayNormalized(12)")
#print(GetAnysizeArrayNormalized(12))
#print("Sum(GetAnysizeArrayNormalized(12))=",sum(GetAnysizeArrayNormalized(12)))
#------------------------------------------------------------------------------------
def GetAnysizeRandomArray(d): # Faz a soma de todos as componentes = 1
    D=GetAnysizeArray(d)
    F=[D[i]/int(65535)for i in range(0,d)]
    return F
#print("GetAnysizeRandomArray(12)")
#print(GetAnysizeRandomArray(12))
#print("Sum(GetAnysizeRandomArray(12))=",sum(GetAnysizeRandomArray(12)))
#------------------------------------------------------------------------------------
def simplePRNGtest(d):
    import random          #OPÇÃO NUMERO 2
    D=[random.random() for i in range(0,d)]    #OPÇÃO NUMERO 2
    aux=np.zeros(d)
    squareD=np.zeros(d)
    a=np.sum(D)
    b= len(D)
    c= a/b
    e=c*c
    b2=[D[i]*D[i+1]for i in range(0,d-1)]
    b2sum=np.sum(b2)
    D2=b2sum/b
    result=D2-e
    return result     # Teste que mostra a distribuição gaussiana para PRN
#------------------------------------------------------------------------------------
def simpleQRNGtest(d):
    D=GetAnysizeArray(d)   #OPÇÃO NUMERO 1
    aux=np.zeros(d)
    squareD=np.zeros(d)
    for i in range(0,d):    # Looping para limitar o vetor entre [0,1)
        aux[i]=65535        # O teste requer valores neste intervalo...
    D=D/aux                 # No looping faz um array de dimensão d tal que
    a=np.sum(D)             # todas sa componentes são o valor 65535 pois
    b= len(D)               # é o valor máximo. Assim fazemos uma divisão
                            # entre as componentes dos dois vetores D e aux
    c= a/b
    e=c*c                   # Essa é o E²(x) da equação do teste
    b2=[D[i]*D[i+1]for i in range(0,d-1)]
    b2sum=np.sum(b2)
    D2=b2sum/b              # Essa é a primeira parte da equalção
    result=D2-e             # Esse é o resultado que o programa retorna
    return result     # Teste que mostra a distribuição gaussiana para TRN
#------------------------------------------------------------------------------------
def Contador(d,dmax):       # Programa auxiliar apenas para criar o eixo das
    a=int(dmax-d)           # coordenadas que será usado no gráfico do teste
    x=np.zeros(a)
    x[0]=1
    for i in range(1,a):
        z=int(i+1)
        x[i]=z
    return x
#------------------------------------------------------------------------------------
def CorTestQandPRNG(d,dmax):       # Programa que plota os testes do gerador ANU e MT
    result1=[simpleQRNGtest(i) for i in range(d,dmax)]
    #result2=[simpleQRNGtest(i) for i in range(d,dmax)]
    result2=[simplePRNGtest(i) for i in range(d,dmax)]
    x=Contador(d,dmax)
    plotScatter2(x,result1,result2)
#------------------------------------------------------------------------------------
def TestPRNG(d,dmax):       # Programa que plota os testes do gerador Mersene Twister
    result1=[simplePRNGtest(i) for i in range(d,dmax)]
    #result2=[simplePRNGtest(i) for i in range(d,dmax)]
    x=Contador(d,dmax)
    plotScatter(x,result1)
#------------------------------------------------------------------------------------
def QRNGtest2(d):
    x = GetAnysizeArray(d)
    y = GetAnysizeArray(d)
    return plotScatter(x,y)
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# A PARTIR DAQUI É UTILIZANDO O ARQUIVO txt
#------------------------------------------------------------------------------------
def QRNbetweenZeroAndOne(d):
    data= np.genfromtxt("QN.txt",dtype=int)
    aux=[65535 for i in range(0,d)]
    F=[data[i]/aux[i]for i in range(0,d)]
    return F
#------------------------------------------------------------------------------------
def read0to1Data(d,int):
    data= np.genfromtxt("QNnormalized.txt",dtype=float)
    k=np.zeros(d)
    aux=int*d
    aux2=(int+1)*d
    k=[float(data[i])for i in range(aux,aux2)]
    return k
#print(read0to1Data(10,0))
#-----------------------------------------------------------------------------------
def GetQRNnormalized():
    D=np.genfromtxt("QN.txt",dtype=int)
    a=len(D)
    aux=[int(65535) for i in range(0,a)]
    F=[D[i]/aux[i]for i in range(0,a)]
    with open("QNnormalized.txt", 'w') as f:
        for a in F:
            f.write(str(a) + '\n')
