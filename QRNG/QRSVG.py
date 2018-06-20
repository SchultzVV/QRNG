from numpy import zeros;from QRPV import Qrpv_zhsl;from math import pi, sqrt, cos, sin;from QRNG import QRNG
#------------------------------------------------------------------------------------------------------------------------------------
def test():
  from distances import fidelity_pp;  from numpy import zeros;
  ns = 10**2 # number of samples for the average
  nqb = 5 # maximum number of qubits regarded
  Favg = zeros(nqb);  Fexa = zeros(nqb);  d = zeros(nqb, dtype = int)
  for j in range(0,nqb):
    d[j] = 2**(j+1);  psi = zeros(d[j], dtype = complex);  phi = zeros(d[j], dtype = complex)
    Fexa[j] = 1.0/d[j]
    Favg[j] = 0.0
    for k in range(0,ns):
      psi = QRSVG(d[j]);  phi = QRSVG(d[j]);  Favg[j] = Favg[j] + fidelity_pp(psi, phi)
    Favg[j] = Favg[j]/ns
  import matplotlib.pyplot as plt
  plt.plot(d, Favg, label = '<F>');  plt.plot(d, Fexa, label = 'F')
  plt.xlabel('d');  plt.ylabel('F');  plt.legend()
  plt.show()
#------------------------------------------------------------------------------------------------------------------------------------
def QRSVG(d):
  rn = zeros(d);rsv = zeros(d, dtype = complex)
  rpv = Qrpv_zhsl(d)
  tpi = 2.0*pi
  from QRNG import GetAnysizeArrayNormalized
  rn=GetAnysizeArrayNormalized(d)
  for j in range(0,d):
    arg = tpi*rn[j]
    ph = cos(arg) + (1j)*sin(arg)
    rsv[j] = sqrt(rpv[j])*ph
  return rsv
#--------------------------------------------------
test()

