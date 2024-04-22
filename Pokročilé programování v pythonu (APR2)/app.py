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