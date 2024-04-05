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