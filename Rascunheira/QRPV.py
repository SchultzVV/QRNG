import numpy as np
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

def GetRandomDec(d):
  z1 = getRandomBin()
  z = z1[:d]
  n = int(z, 2)
  num = float(n)
  return num

def Qrpv_zhsl(d,digits):
  rn = np.zeros(d-1)
  for j in range(0,d-1):
    rn[j] = GetRandomDec(digits)
  rpv = np.zeros(d)
  rpv[0] = 1.0 - rn[0]**(1.0/(d-1.0))
  norm = rpv[0]
  if d > 2:
    for j in range(1,d-1):
      rpv[j] = (1.0 - rn[j]**(1.0/(d-j-1)))*(1.0-norm)
      norm = norm + rpv[j]
  rpv[d-1] = 1.0 - norm
  return rpv

def QRPV_ZHSL(dim,digits):
  x = np.zeros(dim)
  x1 = np.zeros(dim)
  x2 = np.zeros(dim)
  for i in range(0,dim):
    x2[i]=GetRandomDec(digits)
    x1[i]=x2[i]**2
    x[i]=float(x2[i])
  soma=sum(x2)
  norma=soma**(0.5)
  rpv=x2/norma
  print sum(rpv)
  return rpv
#QRPV_ZHSL(3,1023)
#Qrpv_zhsl(3,1023)
#------------------------------------------------------------------------------------
def test():
  d = 3
  rpv = np.zeros(d)
  '''rpv = rpv_zhsl(d)
  for j in range(0,d):
    print('j=', j, 'rpv[j]', rpv[j])
  print('normalization',np.sum(rpv))'''
  ns = 10**4
  ni = 40
  delta = 1.0/ni
  avg_rpv = np.zeros(d)
  ct = np.zeros((ni,d))
  for j in range(1, ns):
    rpv = Qrpv_zhsl(d,35)
    avg_rpv = avg_rpv + rpv
    for k in range(0, d):
      if rpv[k] == 1.0:
        rpv[k] = 1.0 - 1/(10**10)
      for l in range(0, ni):
        if rpv[k] >= l*delta and rpv[k] < (l+1)*delta:
          ct[l][k] = ct[l][k] + 1
  avg_rpv = avg_rpv/ns
  if ( d < 5 ):
    print('avg_rpv = ', avg_rpv)
  x = np.zeros(ni);  y1 = np.zeros(ni);  y2 = np.zeros(ni);  y3 = np.zeros(ni)
  for l in range(0, ni):
    x[l] = l*delta;  y1[l] = ct[l][0]/ns;  y2[l] = ct[l][1]/ns;  y3[l] = ct[l][2]/ns
  import matplotlib.pyplot as plt;  plt.plot(x,y1,label='p0');  plt.plot(x,y2,label='p1');  plt.plot(x,y3,label='p2')
  axes = plt.gca();  axes.set_xlim([0,1]);  axes.set_ylim([0,0.1])
  plt.xlabel('pj');  plt.ylabel('');  plt.legend();  plt.show()
#------------------------------------------------------------------------------------------------------------------------------------
#test()

def square(list):
    ret = []
    for i in list:
        ret.append(i ** 2)
    return ret

def QRV(dim,digits):
  x1 = np.zeros(dim)
  x2 = np.zeros(dim)
  for i in range(0,dim):
    x2[i] = GetRandomDec(digits)
  x1=square(x2)
  x= float(x1)
  soma=sum(x)
  norma=soma**(0.5)
  rpv=x2/norma
  print sum(rpv)
  return rpv
print QRV(3,1023)