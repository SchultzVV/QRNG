import urllib2; import numpy as np; import matplotlib.pyplot as plt; import plots
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
print QRNnorm(1023)

def GetRandomDec(d):
    z1 = getRandomBin()
    z = z1[:d]
    n = int(z,2)
    num=float(n)
    return num
print GetRandomDec(1023)

def testRandomDec(d):
    ab = np.zeros(d)
    ord = np.zeros(d)
    for i in range(0, d):
        ab[i] = GetRandomDec(800)
        ord[i] = GetRandomDec(800)
    x = ab / QRNnorm(800)
    y = ord / QRNnorm(800)
    print x
    print y
    plots.plotScatter(x, y)



testRandomDec(200)