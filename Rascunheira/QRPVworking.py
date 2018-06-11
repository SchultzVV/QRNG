from QRNG import GetRandomDec; import numpy as np
import urllib2;
import numpy as np;
import matplotlib.pyplot as plt;
import plots

def getRandomBin():
  url = 'http://150.203.48.55/RawBin.php'

  page = urllib2.urlopen(url, timeout=5)

  data = page.read()
  num = data.split('"rng"')[1].split('<td>\n')[1].split('</td>')[0]
  return num

def QRNnorm(d):
  norma = (2 ** d) - 1
  a = "1" * d
  # print a
  b = int(a, 2)
  c = float(b)
  #  print norma
  return c


def GetRandomDec(d):
  z1 = getRandomBin()
  z = z1[:d]
  n = int(z, 2)
  num = float(n)
  return num


def QRPVG_test(digits, dim):
    ax = [GetRandomDec(digits) for i in range(0, dim - 1)]
    ay = [GetRandomDec(digits) for i in range(0, dim - 1)]
    x2 = np.array(ax) + 0.
    y2 = np.array(ay) + 0.
    norm = QRNnorm(digits)
    x = x2 / norm
    y = y2 / norm
    return plots.plotScatter(x, y)


QRPVG_test(1023,10)


def QRPVG(digits, dim):
    ax = [GetRandomDec(digits) for i in range(0, dim - 1)]
    ay = [GetRandomDec(digits) for i in range(0, dim - 1)]
    x2 = np.array(ax) + 0.
    y2 = np.array(ay) + 0.
    norm = QRNnorm(digits)
    x = x2 / norm
    y = y2 / norm
    return x,y
