# Doucovani-Python
 
## Úvodní povídání
### Collab vs. PC
Většinou při psaní v pythonu se rozhoduješ mezi psaní na cloudu přes "Google Colab", který tvoří automaticky jupyter notebooky, nebo psaním na vlastním stroji skrz pycharm nebo visual studio code(jupyter notebooky jdou psát i na vlastním stroji).
## VENV

### Jednoduchý a nenáročný jazyk
Python a JavaScript jsou oba super flexible na psaní kódu - můžeš v nich udělat téměř cokoli, aniž bys musel přemýšlet o typech proměnných. Python je o něco víc "přehledný" - například když porovnáváš různé věci jako řetězce nebo čísla, obvykle to funguje stejně, což ulehčuje psaní kódu a snižuje možnost chyb.
### Středníky
Python nepoužívá středníky k zakončení příkazu. Místo středníků se začne psát na další řádek.
```python
a = 1
b = 2
c = a + b
```
### Mezery a řádkování
Python místo závorek pracuje se spacingem. Pokud píšeš například uvnitř bloku smyčky, tak musí být všechny řádky oddělené od kraje o stejný počet míst(nejlépe o TAB). Každý nový blok se znovu odděluje.
```python
while true:
 a = true
 if a is not false:
  print("hello world")
  break
```

## Proměnné
V Pythonu není potřeba explicitně určovat typ proměnné, protože Python je dynamicky typovaný jazyk(typ proměnné je určen automaticky na základě hodnoty, kterou do ní přiřazuješ, a může se měnit během běhu programu).
```python
x = 5
y = "Hello"
z = 3.14
instance_tridy = EpickoUzasnaTrida()
```
## List(Seznam)
V Pythonu je seznam datová struktura, která umožňuje ukládat více prvků v jednom objektu. Prvky seznamu mohou být různých typů a seznam může být měnitelný.
```python
my_list = [1, 2, 3, 4, 5, 6, 7]
my_funky_list = [1, "Hello", True, [1, 2, 3], {"name": "John", "age": 30}]
```
## Slovník(set)
Slovník v Pythonu je datová struktura, která ukládá páry klíč-hodnota. Každý klíč musí být unikátní a neměnitelný. Obsah nemusí být stejný pro všechny prvky, ale měl by pro sanžší iteraci
```python
slovnik = {"name": "John", "age": 30}
slovnik_veliky = {
 "Velitel":{"name": "John", "age": 3,},
 "Generál":{"name": "Johnny", "age": 28},
 {"Ministr všeho": "Udělal jsem tady klíč slovníkem"}:{"name": "John John", "age": 40},
 [0,1] : {"name": "Johnnnnnn~", "age": 22}
}
```
## Tuple 
Tuple je datová struktura podobná seznamu, ale na rozdíl od seznamu je neměnitelná, což znamená, že po vytvoření nelze její prvky změnit.
```python
my_tuple = (1, 2, 3, 4, 5, 6, 7)
my_funky_tuple = (1, "Hello", True, [1, 2, 3], {"name": "John", "age": 30})
```
## Input a print
```python
name = input("Zadej své jméno: ")
print("Ahoj,", name)
```
## Podmínky
Podmínky v pythonu pracují s klíčovými slovy "if", "elif" a "else". Obsah podmínky může, ale nemusí být ohraničen závorkou(většinou se píše bez). Za podmínkou se pro začátek bloku musí napsat ":" a obsah odsadit tak, aby ne byl na stejnm odsazení jako podmínka.
```python
x = 10

if x > 5:
    print("x je větší než 5")
elif x == 5:
    print("x je rovno 5")
else:
    print("x je menší než 5")

if (x > 5):
    print("x je větší než 5")
elif (x == 5):
    print("x je rovno 5")
else:
    print("x je menší než 5")
```
```python
x = True

if x is True:
    print("x je real")
else:
    print("x je faleš")

if x is not True:
    print("x je real")
else:
    print("x je faleš")

if x == True:
    print("x je real")
else:
    print("x je faleš")

if x != True:
    print("x je real")
else:
    print("x je faleš")
```
#### pass/...
V bloku musí být napsaný nějaký příkaz, jinak compiler vyhazuje chybu. Pokud se chceš vyhnout červeným řádkům při tvoření nového kodu, můžeš využít "pass" nebo "...", který umožnuje prázdný blok. Toto platí pro všechny "bloky", nejen pro podmínky.
```python
if x is True:
    pass
else:
    ...
```
## Smyčky
### for
Python nemá klasický for loop jako takový, pracuje pouze s for each loopem. U klasíckého loopu iteruji ve funkci range, abych docílil chtěné funkcionality
```python
# for(int i = 1; i<10, i+=2)
for i in range(1,10,2):
 print(i)
```
Klasický for each.
```python
list = [10,51,902,23,44]
for prvek in list:
 print(prvek)
```
Enumerate zároven umožnuje pracovat s tím, kolikátá je to iterace.
```python
list = [10,51,902,23,44]
for prvek, iterace in enumerate(list):
 print(prvek)
```
### while
```python
while true:
 print("haha nekonečný smyčka")
```
```python
for char in "Python":
    print(char)
```
## Funkce

```python
def krasna_fce():
 print("funguju")

krasna_fce()
```
## Main
V Pythonu není přímo definovaná funkce main jako v některých jiných programovacích jazycích, ale obvykle se kód spouští od horní úrovně souboru.
```python
def krasna_fce():
 print("funguju")
def main():
 print("Hello from main function!")
 krasna_fce()

if __name__ == "__main__":
    main()
```
## Funkcionální programování
Jednořádkové podmínky a smyčky

## Lambda funkce
Pokud chci ve funkcionálním programování využít funkci, kterou nechci definovat mimo.
```python
# Lambda funkce
add = lambda x, y: x + y

# Mapování
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))

# Filtrování
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
```
