import numpy as np
from QRNG import GetAnysizeRandomArray
#------------------------------------------------------------------------------------
def Qrpv_zhsl(d):
  rn = np.zeros(d-1)
  #rn=read0to1Data(d-1,0)
  rn=GetAnysizeRandomArray(d-1)
  rpv = np.zeros(d)
  rpv[0] = 1.0 - rn[0]**(1.0/(d-1.0)) # linha para gerar o p1
  norm = rpv[0]
  if d > 2:
    for j in range(1,d-1):            # Loop para gerar do segundo ao penúltimo
      rpv[j] = (1.0 - rn[j]**(1.0/(d-j-1)))*(1.0-norm)
      norm = norm + rpv[j]
  rpv[d-1] = 1.0 - norm               # Linha para gerar a última probabilidade
  return rpv
#------------------------------------------------------------------------------------
def test():
  d = 6
  ns = 10**2
  ni = 40
  delta = 1.0/ni
  avg_rpv = np.zeros(d)
  ct = np.zeros((ni,d))
  for j in range(1, ns):
    rpv = Qrpv_zhsl(d)
    avg_rpv = avg_rpv + rpv
    for k in range(0, d):
      if rpv[k] == 1.0:
        rpv[k] = 1.0 - 1/(10**10)
      for l in range(0, ni):
        if rpv[k] >= l*delta and rpv[k] < (l+1)*delta:
          ct[l][k] = ct[l][k] + 1
  avg_rpv = avg_rpv/ns
  if ( d < 7 ):
    print('avg_rpv = ', avg_rpv)
  x = np.zeros(ni);  y1 = np.zeros(ni);  y2 = np.zeros(ni);  y3 = np.zeros(ni);  y4 = np.zeros(ni);  y5 = np.zeros(ni)
  for l in range(0, ni):
    x[l] = l*delta;  y1[l] = ct[l][0]/ns;  y2[l] = ct[l][1]/ns;  y3[l] = ct[l][2]/ns;  y4[l] = ct[l][3]/ns;  y5[l] = ct[l][4]/ns
  import matplotlib.pyplot as plt;
  plt.plot(x,y1,label='p1');
  plt.plot(x,y2,label='p2');
  plt.plot(x,y3,label='p3')
  plt.plot(x,y4,label='p4')
  plt.plot(x,y5,label='p5')
  axes = plt.gca();  axes.set_xlim([0,1]);  axes.set_ylim([0,0.1])
  plt.xlabel('pj');  plt.ylabel('');  plt.legend();  plt.show()
#------------------------------------------------------------------------------------
