import json
import urllib2;import numpy as np;import plots
#------------------------------------------------------------------------------------
def getRandomBin():
    url = 'http://150.203.48.55/RawBin.php'

    page = urllib2.urlopen(url, timeout=5)

    data = page.read()
    num = data.split('"rng"')[1].split('<td>\n')[1].split('</td>')[0]
    return num
#------------------------------------------------------------------------------------
def QRNnorm2(d):
    norma = (2 ** d) - 1
    return norma
#------------------------------------------------------------------------------------
def QRNnorm(d):
    a = "1" * d
    b=int(a,2)
    c=float(b)
    return c
#------------------------------------------------------------------------------------
def GetRandomDec(d):
    z1 = getRandomBin()
    z = z1[:d]
    n = int(z,2)
    num=float(n)
    return num
#------------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------------
def QRV(ptos, digits):
    ab = np.zeros(ptos)
    for i in range(0, ptos):
        ab[i] = GetRandomDec(digits)
    x = str(ab / QRNnorm(digits))
    file = open('Xdata.txt', 'w')
    file.write(x)
    file.close()
    return x
#------------------------------------------------------------------------------------
#RandomDecGraph(10,100)
def Enjambre(dim,digits):
    for i in range (0,dim):
        ax = [GetRandomDec(digits) for i in range(0, dim - 1)]
        ay = [GetRandomDec(digits) for i in range(0, dim - 1)]
        x2 = np.array(ax) + 0.
        y2 = np.array(ay) + 0.
        norm = QRNnorm(digits)
        x = x2 / norm
        y = y2 / norm
        return plots.plotScatter(x, y)
'''
def getRandom(lenght):
    d1=str(lenght)
    url1 = 'https://qrng.anu.edu.au/API/jsonI.php?length='
    url2 = '&type=uint16'
    url = url1+d1+url2
    page = urllib2.urlopen(url, timeout=5)

    data = page.read()
    if data:
        with open(data, 'r') as f:
            datastore = json.load(f)
    return datastore
    print datastore
print getRandom(5)
'''
