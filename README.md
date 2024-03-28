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

## List
seznam

## Slovník(set)

## Tuple 
Množina


## Funkce

## Main

## Funkcionální programování
Jednořádkové podmínky a smyčky

## Lambda funkce
Pokud chci ve funkcionálním programování využít funkci, kterou nechci definovat mimo.
```python
# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() with a lambda function to filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Print the result
print(even_numbers)
```
