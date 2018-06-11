
import urllib2;
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

def getRandom(self,type):
    if type == self.BINARY:
        url = 'http://150.203.48.55/RawBin.php'
    elif type == self.HEX:
        url = 'http://150.203.48.55/RawHex.php'
    elif type == self.CHAR:
        url = 'http://150.203.48.55/RawChar.php'

        page = urllib2.urlopen(url, timeout=5)

        data = page.read()
        num = data.split('"rng"')[1].split('<td>\n')[1].split('</td>')[0]


def Getrandom():
    url = 'http://150.203.48.55/RawBin.php'
    page = urllib2.urlopen(url, timeout=5)

    data = page.read()
    num = data.split('"rng"')[1].split('<td>\n')[1].split('</td>')[0]
    return num
#print (Getrandom(1))
#print (GetRandomDec(1))

def Getrandom1000(d):
    A=[]
    for i in range (0,d):
        A[i]=int(GetRandomDec(3))
    return A
print(Getrandom1000(100))
