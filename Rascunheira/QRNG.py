from plots import plotScatter;import urllib2;import numpy as np;import plots;import json;

def getRandomBin():
    url = 'http://150.203.48.55/RawBin.php'

    page = urllib2.urlopen(url, timeout=5)

    data = page.read()
    num = data.split('"rng"')[1].split('<td>\n')[1].split('</td>')[0]
    return num

def QRNnorm(d):
    norma=(2**d)-1
    a = "1" * d
   # print a
    b=int(a,2)
    c=float(b)
  #  print norma
    return c

def GetRandomDec(d):
    z1 = getRandomBin()
    z = z1[:d]
    n = int(z,2)
    num=float(n)
    return num

def testRandomDec(d):
    ab = np.zeros(d)
    ord = np.zeros(d)
    digits=1023
    for i in range(0, d):
        ab[i] = GetRandomDec(digits)
        ord[i] = GetRandomDec(digits)
    x = ab / QRNnorm(digits)
    y = ord / QRNnorm(digits)
    #print x
    #print y
    plots.plotScatter(x, y)

def RandomDecGraph(ptos,digits):
    ab = np.zeros(ptos)
    ord = np.zeros(ptos)
    for i in range(0, ptos):
        ab[i] = GetRandomDec(digits)
        ord[i] = GetRandomDec(digits)
    x =str( ab / QRNnorm(digits))
    y =str( ord / QRNnorm(digits))
    file=open('Xdata.txt','w')
    file.write(x)
    file.close()
    file2 = open('Ydata.txt', 'w')
    file2.write(y)
    file2.close()
    print x
    print y
    plots.plotScatter(x, y)
    return x
    return y

def QRV(ptos, digits):
    ab = np.zeros(ptos)
    for i in range(0, ptos):
        ab[i] = GetRandomDec(digits)
    x = str(ab / QRNnorm(digits))
    file = open('Xdata.txt', 'w')
    file.write(x)
    file.close()
    return x

def Enjambre(dim,digits):
    for i in range (0,dim):
        ax = [GetRandomDec(digits) for i in range(0, dim - 1)]
        ay = [GetRandomDec(digits) for i in range(0, dim - 1)]
    x1=str(ax)
    y1 = str(ay)
    x = np.array(x1) + 0.
    y = np.array(y1) + 0.
    filex2 = open('XdataArray.txt','w')
    filey2 = open('YdataArray.txt','w')
    filex2.write (x)
    filey2.write (y)
    filex2.close()
    filey2.close()
    print x
    print y

# ------------------------------------------------------------------------------------
def GetData(lenght):
    d1 = str(lenght)
    url1 = 'https://qrng.anu.edu.au/API/jsonI.php?length='
    url2 = '&type=uint16'
    url = url1 + d1 + url2
    response = urllib2.urlopen(url)
    data = json.load(response)
    num = data.get("data", "none")

    return num


# ------------------------------------------------------------------------------------
def QRNG_test():
    x1 = GetData(1000)
    y1 = GetData(1000)
    x1.extend(GetData(1000))
    y1.extend(GetData(1000))
    norm = np.zeros(2000)
    for i in range(0, 2000):
        norm[i] = 65535
    x = np.divide(x1, norm)
    y = np.divide(y1, norm)
    return plotScatter(x, y)
# ------------------------------------------------------------------------------------
def E(d):
    D=GetAnysizeArray(d)   #OPÇÃO NUMERO 1
    #import random          #OPÇÃO NUMERO 2
    #D=[random.random() for i in range(0,d)]    #OPÇÃO NUMERO 2
    #print ('O vetor de números aleatórios inicial é:',D)
    aux=np.zeros(d)
    squareD=np.zeros(d)
    for i in range(0,d):    # Looping para normalizar o vetor
        aux[i]=65535
    D=D/aux
    #print ('Aqui está o vetor [o,1]:',D)
    a=np.sum(D)
    print('A soma é:',a)
    b= len(D)
    print ('o N é :', b)
    c= a/b
    e=c*c
    print(' o E(x) ao quadrado é :',e)
    b2=[D[i]*D[i+1]for i in range(0,d-1)]
    b2sum=np.sum(b2)
    D2=b2sum/b
    print ('a parte do primeiro somatório é:',D2)
    result=D2-e
    print('o resultado do teste é :',result)
    print('Quanto mais próximo de zero menos corelacionado')
    return result
