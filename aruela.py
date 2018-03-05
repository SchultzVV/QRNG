import urllib.request; import json

def anu():
   url = 'https://qrng.anu.edu.au/API/jsonI.php?length=10&type=uint16'
   page = urllib.request.urlopen(url, timeout=5)
   aux = page.read()
   print (aux)
   data = json.loads(aux.decode('utf-8'))
#   data = json.load(aux)

   num = data.get("data", "none")
   print (num)
   return num

anu()