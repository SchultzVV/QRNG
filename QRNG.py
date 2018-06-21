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
def GetAnysizeRandomArray(d): # Faz um array entre 0 e 1 do servidor ANU
    D=GetAnysizeArray(d)
    F=[D[i]/int(65535)for i in range(0,d)]
    return F
#print("GetAnysizeRandomArray(12)")
#print(GetAnysizeRandomArray(12))
#print("Sum(GetAnysizeRandomArray(12))=",sum(GetAnysizeRandomArray(12)))
#------------------------------------------------------------------------------------
def QRNGGaussian(d):
    import math
    D=GetAnysizeRandomArray(d)
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
def correlacaoPRNGtest(d):
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
    return result     # Teste que mostra a distribuição gaussiana para PRN # Teste de Correlação Simples
#------------------------------------------------------------------------------------
def correlacaoQRNGtest(d):
    D=GetAnysizeArray(d)
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
    return result     # Teste que mostra a distribuição gaussiana para TRN # Teste de Correlação Simples
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
def CorTestQandPRNG(d,dmax):# plot do Teste de Correlação Simples
    result1=[correlacaoQRNGtest(i) for i in range(d,dmax)]
    #result2=[correlacaoQRNGtest(i) for i in range(d,dmax)]
    result2=[correlacaoPRNGtest(i) for i in range(d,dmax)]
    x=Contador(d,dmax)
    plotScatter2(x,result1,result2)
#CorTestQandPRNG(1,150)
#------------------------------------------------------------------------------------
def TestPRNG(d,dmax):       # Programa que plota os testes do gerador Mersene Twister
    result1=[simplePRNGtest(i) for i in range(d,dmax)]
    #result2=[simplePRNGtest(i) for i in range(d,dmax)]
    x=Contador(d,dmax)
    plotScatter(x,result1)
#------------------------------------------------------------------------------------
def PRNGtest2(d):
    import random as rd
    x = [rd.random() for i in range(0,d)]
    y = [rd.random() for i in range(0,d)]
    return plotScatter(x,y)          # Teste de distribuição de pontos aleatórios
#PRNGtest2(1800000)
#------------------------------------------------------------------------------------
def QRNGtest2(d):
    x = GetAnysizeArray(d)
    y = GetAnysizeArray(d)
    return plotScatter(x,y)          # Teste de distribuição de pontos aleatórios
#QRNGtest2(1500)
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#  A PARTIR DAQUI É UTILIZANDO O ARQUIVO txt
#------------------------------------------------------------------------------------
#data= np.genfromtxt("QNnormalized.txt",dtype=float)
def QRNbetweenZeroAndOne(d):
    data= np.genfromtxt("QN.txt",dtype=int)
    aux=[65535 for i in range(0,d)]
    F=[data[i]/aux[i]for i in range(0,d)]
    return F # Versão 1.0 do read0to1Data
#------------------------------------------------------------------------------------
def QRNGtest2(d):# Teste de distribuição de pontos aleatórios
    import matplotlib.pyplot    as plt
    x = [data[i] for i in range(0,d)]
    a=d
    y = [data[i] for i in range(a,a+d)]
    plt.scatter(x,y,c='black', s=1, marker='*')
    plt.title('Distribuição de pontos Aleatórios')
    #plt.xlabel('x')
    #plt.ylabel('y')
    plt.legend()
    plt.show()(x,y)
#QRNGtest2(1800000)
#------------------------------------------------------------------------------------
def read0to1Data(d,int):      # Versão pronta
    #data= np.genfromtxt("QNnormalized.txt",dtype=float)
    k=np.zeros(d)
    aux=int*d
    aux2=(int+1)*d
    k=[float(data[i])for i in range(aux,aux2)]
    return k
#print(read0to1Data(10,0))
#-----------------------------------------------------------------------------------
def SaveQRNnormalized():
    D=np.genfromtxt("QN8.dat",dtype=int)
    a=len(D)
    aux=[int(65535) for i in range(0,a)]
    F=[D[i]/aux[i]for i in range(0,a)]
    with open("QN8normalized.txt", 'w') as f:
        for a in F:
            f.write(str(a) + '\n')
#SaveQRNnormalized()
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# WANTED TO CREATE THE RUG AND RDMG
#------------------------------------------------------------------------------------

def strgQRNGGaussian(d,int):
    import math
    D=read0to1Data(d,int)
    x=np.zeros(d,dtype = complex)
    for i in range(0,d,2):
        x[i]=np.sqrt(-2*math.log(D[i+1]))*math.cos(2*math.pi*D[i])
        x[i+1]=np.sqrt(-2*math.log(D[i+1]))*math.sin(2*math.pi*D[i])
    return x
#print(strgQRNGGaussian(6,1))
#------------------------------------------------------------------------------------
def StrgQginibre(d):
  from QRNG import QRNGGaussian
  from numpy import zeros
  G = zeros((d,d), dtype = complex);
  for j in range(0,d):
    int=j
    grn = strgQRNGGaussian(2*d,int)
    for k in range(0,d):
      G[j][k] = grn[k] + (1j)*grn[k+d]
  return G
#print(StrgQginibre(5))
