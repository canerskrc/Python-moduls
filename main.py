"""import math
ustal=math.pow(5,2)
fak=math.factorial(4)
cosinus=math.cos(120)
karekok=math.sqrt(81)
print(ustal)
print(fak)
print(cosinus)
print(karekok)"""

# bir modülün hangi özellikleri olduğunu görme
import time

"""import random
print(dir(random))"""
# 0 ile 1 aralığında random sayı üretmek
"""import random
a=random.random()
print(a)"""
# belirlediğimiz aralıkta integer veri tipinde sayı üretilmesi
"""import random
sayi=random.randint(1,10)
print(sayi)"""

# random.choice listeden rastgele öge seçilmesi

"""import random
cicekler=["gül","papatya","begonya","menekşe","karanfil"]
print(random.choice(cicekler))
print(random.choice(cicekler))
print(random.choice(cicekler))
print(random.choice(cicekler))
print(random.choice(cicekler))"""


#https://pip.pypa.io/en/latest/installing.html

# get-pip.py dosyasını bilgisayarımıza indirelim


#install yeni bir paket yükler
#uninstall varolan paketi siler
#freze yüklü olan tüm paketleri listesini çıktıya verir
#list yüklü olan tüm paketlerin normal listesini çıktıya verir
#show yüklü olan pektlerin hakkında bize bilgi verir

"""import time
print(time.time())"""
# gmtime()

"""import  time
print(time.gmtime(time.time()))"""

#localtime zaman bilgisini sıralı şekilde verir.

"""import time
print(time.localtime())"""

#ctime fonksiyonu içinde bulunulan zamanı verir

"""import time
print(time.ctime())"""

# strftime() kendimize ait zaman cümlesi oluşturur

"""import time

print(time.strftime("%S/%M/%H"))"""

#sleep() belirlenen süre boyunca programı durdurur

"""import time
print("başlangıç: %s "% time.ctime())
time.sleep(5)
print("bitiş: %s" % time.ctime())"""
###########################################################
"""from tkinter import *
import time
pencere = Tk()
pencere.title("Dijital Saat")
zaman1=''
sekil= Label(pencere, font=('times', 20, 'bold',), bg='white')
sekil.grid()

def saat():
      global zaman1
      zaman2= time.strftime('%H:%M:%S')
      if zaman2 != zaman1:
            zaman1 = zaman2
            sekil.config(text=zaman2)
            sekil.after(50, saat)
saat()
pencere.mainloop( )"""


"""from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("dijital saat")
def saat():
      string=strftime('%H:%M:%S %p')
      label.config(text=string)
      label.after(1000, saat)

label= Label(root, font=("ds-digital", 80, ), background="black", foreground="pink")
label.pack(anchor='center')
saat()
mainloop()"""
############################################################################
"""from os import system

i = 0
while i <=1:
      system("cls")
      print(time.strftime("%H/%M/%S"))
      time.sleep(1)"""

###########################################################################






