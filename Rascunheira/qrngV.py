import urllib2
#from urllib.request import urlopen
import numpy
import matplotlib.pyplot as plt
from plots import plotScatter

'''
def getRandomChar():
        url = 'http://150.203.48.55/RawChar.php'

        page = urllib2.urlopen(url, timeout=5)

        data = page.read()
        num = data.split('"rng"')[1].split('<td>\n')[1].split('</td>')[0]
        return num
'''
def getRandomBin():
        url = 'http://150.203.48.55/RawBin.php'

        page = urllib2.urlopen(url, timeout=5)
        

        data = page.read()
        num = data.split('"rng"')[1].split('<td>\n')[1].split('</td>')[0]
        return num
'''
def getRandomHex():
        url = 'http://150.203.48.55/RawHex.php'

        page = urllib2.urlopen(url, timeout=5)

        data = page.read()
        num = data.split('"rng"')[1].split('<td>\n')[1].split('</td>')[0]
        return num
'''

def GetRandomDec():
        N = 10
        dim = N*16
        x = numpy.zeros(dim)
        y = numpy.zeros(dim)
        d = 64
        norm = float(18446744073709551615)
        for k in range(0,N):
          z1 = getRandomBin()
          for j in range(0,16):
            z = z1[j:j+d-1]
            n = int(z, 2)
            x[j] = float(n)/norm
        for k in range(0,N):
          z2 = getRandomBin()
          for j in range(0,16):
            V = z2[j:j+d-1]
            n2 = int(V, 2)
            y[j] = float(n2)/norm


#a=getRandomBin()
#print a
#b=getRandomChar()
#c=getRandomHex()
#c = 0
GetRandomDec()
#print rn
#print b
#print c