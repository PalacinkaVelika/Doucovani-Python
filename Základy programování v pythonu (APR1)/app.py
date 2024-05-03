'''
print("hello world")

muj_list = [1,9,77,45]
prazdny = []
prazdny.append("aa")
prazdny.append(1)
prazdny.append(0.31)
prazdny.append("asdfmklksda")

def add(a,b): return a+b


vek = add(1,2)
clovek = {
    "jmeno" : "Josef", 
    "vek" : vek,
    "syn" : {
        "jmeno": "pepe"
    }
}

print(clovek["vek"])
'''

# toto je komentář
'''
Toto
je
multi
line
komentář
'''

'''
name = input("Zadejte svoje jméno: ")
print(f"Jestli nekecas tak jsi: {name}")


a = 3
b = 5
c = 9
if True:
    print(a+b) 


# for(int i = 0; i < 10; i+=2)

for i in range(0,11,1):
    print(float(i))

    
list = [10,51,902,23,44]
kolikaty = 0
for prvek in list:
 print(prvek)
 kolikaty += 1 
 print(kolikaty)
    

list = [10,51,902,23,44]
 
for prvek, kolikaty in enumerate(list):
 print(prvek) #10, 51, 902, ...
 print(kolikaty) # 0, 1, 2, 3, ...
 
'''
'''
a = 7
while a > 0:
    print(a)
    a -= 1


a = 7
while True:
    print(a)
    a -= 1
    if a < 0:
        break
'''
'''
def rectangle_info(width, height):
    plocha = width * height
    perimetr = 2 * (width + height)
    return plocha, perimetr

a, b = rectangle_info(4, 6)
perimetr = rectangle_info(4, 6)[1]
print(perimetr)
'''
'''
def greet(name):
    if name == "":
        print("prosím zadej platné jméno")
        return
    if name == "Josef":
        print("dobrý jméno")
    return "Hello, " + name

print(greet("John"))
print(greet(""))
'''
'''
radek_kalkulacky = "2+2/3"
radek_kalkulacky += "-"
radek_kalkulacky += "5"
print(radek_kalkulacky)
vysledek = eval(radek_kalkulacky)
print(vysledek)
vysledek = 2+2/3-5
print(vysledek)
'''
'''
def add(x: int, y: int) -> str:
    return x+y

result = add(2, 5)
print(result)
'''
'''
a = "3"
b = "5"
print(int(a+b))
'''
'''
def krasna_fce():
 print("funguju")
def main():
 print("Hello from main function!")
if __name__ == "__main__":
    main()
    krasna_fce()
'''
'''
a = False

if a == True:
    x = "lets go"
else:
    x = "no go"

x = "lets go" if a else "no go" 
'''
'''
# setup
def func(par):
 return par + 25
arr = [1,5,6,4,2]
# fUnKcIoNáLnÍ programko
x = [func(a) for a in arr]
print(x) # [26, 30, 31, 29, 27]
# realisticky normální programování verze
x = []
for a in arr:
 x.append(func(a)) # vše v tomto bloku se stane pro každý prvek listu "arr"
print(x) # [26, 30, 31, 29, 27]
'''
'''
vysledek = (lambda x, y: x + y)(1,2) #3
print(vysledek)

arr = [1,5,6,4,2]
x = [(lambda a: a + 25)(a) for a in arr]
print(x)
'''
'''
arr = [1,"5",6.4156,4,2]
x = list(map(lambda a: int(a), arr))
print(x) # [1, 5, 6, 4, 2]
'''


# "pravidla" tříd
# privátní / veřejný -> private public
# getter a setter


class Pes:
    def __init__(self, jmeno, barva, majitel):
        self._jmeno = jmeno
        self._barva = barva
        self._majitel = majitel
        
    # public metoda
    def spocitej_vzdalenost_ode_me(self):
       # cislo = vypocet()
       cislo = 1
       return cislo
    # private metoda
    def vypocet():
        pass
    
    def stekej(self, cokoliv):
        print(f"haf {cokoliv}")
        
    def rekni_sve_jmeno(self):
        print(f"jmenuju se {self._jmeno}")
        
    ''' 
    # python to neumi ale je to cool vedet     
    
    def rekni_sve_jmeno(self, parameter, parameterr, parametereef):
        print("něco jiného")


    def rekni_sve_jmeno(self, parameter, parameterr, parametereef, out):
        print("něco jiného")
        return "ahoj"
        
    rekni_sve_jmeno(1,2,3) # nevraci nic
    rekni_sve_jmeno(1,2,3,necim) # vraci ahoj
    '''  
    # špatně udělaný setter
    def set_barva(self, nova_barva):
        self._barva = nova_barva
    
    # špatně udělaný getter
    def get_barva(self):
        return "co ti je do toho jakou mám barvu"
    
    # správně udělaný getter a setter
    @property
    def barva(self):
        return self._barva

    @barva.setter
    def barva(self, value):
        self._barva = value
        
        
    @staticmethod
    def jak_dela_pes():               
        return "haf haf"  

# instance třídy (varianta)
alik = Pes("alik", "cernej", "Josef")
alik.get_barva()
alik.stekej("pepepepe")
alik.rekni_sve_jmeno()

# alik.rekni_sve_jmeno(1,1,1)

# statická třída nemá instanci - používá se hlavně pro utility
class StatickaTrida:
    @staticmethod
    def deset_cisel_pi():
        return 3.1419841384
    
StatickaTrida.deset_cisel_pi()



class Vojak:
    #kontruktor
    def __init__(self, jmeno, zivoty=100, utok=10):
        self.zivoty = zivoty
        self.utok = utok
        self.jmeno = jmeno
    # metoda
    def zautoc(self, vojak_na_nez_utocim):
        vojak_na_nez_utocim.prijmi_dmg(self.utok)
        print(f"({self.jmeno}) (životy:{self.zivoty}): já jsem zautocil na {vojak_na_nez_utocim.jmeno}")
    
    def prijmi_dmg(self, dmg):
        self.zivoty = self.zivoty - dmg
        print(f"({self.jmeno}) (životy:{self.zivoty}): au! schytal jsem dmg!")
        
    #sečtením dvou vojaku
    def __add__(self, other):
        return Vojak(self.jmeno + other.jmeno, self.zivoty+other.zivoty, self.utok+other.utok)
    
    # přetypování na string
    def __str__(self):
        return f"Mé jméno jest nádherná {self.jmeno}"

        
        
rusak = Vojak("rus")
cech = Vojak("cech", 200, 20)

novy_supervojak = rusak + cech
print(novy_supervojak.jmeno)
print(novy_supervojak.zivoty)
print(novy_supervojak.utok)
print(str(rusak))

rusak.zautoc(cech)
cech.zautoc(rusak)
cech.zautoc(rusak)
rusak.zautoc(cech)
rusak.zautoc(cech)