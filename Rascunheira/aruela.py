from urllib.request import urlopen
import json
#------------------------------------------------------------------------------------
def GetAnysizeArray(dim):
    if dim <= 1024:
        little = GetRandomArray(dim)
        return little
    else:
        large = []
        m = dim
        while m > 1024:
            large.extend(GetRandomArray(1024))
            m = m - 1024
        else:
            large.extend(GetRandomArray(m))
            return large
#------------------------------------------------------------------------------------
def QRNG_Only_one():
    a=float(GetRandomArray(1)[0])
    b=float(a/65535)
    return b
#------------------------------------------------------------------------------------

def GetRandomArrayP3(dim):
    d=str(dim)
    url1 = 'https://qrng.anu.edu.au/API/jsonI.php?length='
    url2 = '&type=uint16'
    url = url1+d+url2
    aux = urlopen(url)
    print (aux)
    HTTPResponse.read([amt])
    data = json.load(aux)
    #num = data.get("data", "none")
    #return num
#------------------------------------------------------------------------------------

GetRandomArrayP3(15)