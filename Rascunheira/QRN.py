import urllib2; import numpy as np; import matplotlib.pyplot as plt; import plots
def getRandomBin():
    url = 'http://150.203.48.55/RawBin.php'

    page = urllib2.urlopen(url, timeout=5)

    data = page.read()
    num = data.split('"rng"')[1].split('<td>\n')[1].split('</td>')[0]
    return num
#-------------------------------------------------------------------------
def GetRandomDec(d):
    z1 = getRandomBin()
    z = z1[:d]
    n = int(z, 2)
    return n
#-------------------------------------------------------------------------
def QRNnorm(d):
    norma=(2**d)-1
    a = "1" * d
    b=int(a,2)
    c=float(b)
    return norma
import urllib2;import numpy as np;import json;from plots import plotScatter
#------------------------------------------------------------------------------------
def GetRandomArray(dim):
    d=str(dim)
    url1 = 'https://qrng.anu.edu.au/API/jsonI.php?length='
    url2 = '&type=uint16'
    url = url1+d+url2
    response = urllib2.urlopen(url)
    data = json.load(response)
    num = data.get("data", "none")
    return num









'''
#def test():
#    import matplotlib.pyplot as plt
#    for i in range(0,10):
#        x = np.zeros(10)
#        y = np.zeros(10)
#        x[i]= GetRandomDec(20)
#        y[i] = GetRandomDec(20)
#    plt.plotscatter(x,y, label='scatter', color='blue', s=5, marker='*')
#    plt.xlabel('x')
#    plt.ylabel('y')
#    plt.legend()float_version = float(int_version)
#    plt.show()
#test()

def Jqrng():
    N = 10
    dim = N * 16
    x = np.zeros(dim)
    y = np.zeros(dim)
    d = 64
    norm = float(18446744073709551615)
    for k in range(0, N):
        z1 = getRandomBin()
        for j in range(0, 16):
            z = z1[j:j + d - 1]
            n = int(z, 2)
            x[j] = float(n) / norm
    for k in range(0, N):
        z1 = getRandomBin()
        for j in range(0, 16):
            z = z1[j:j + d - 1]
            n = int(z, 2)
            y[j] = float(n) / norm
    plots.plotScatter(x, y)
'''