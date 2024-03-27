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

## Input a print

## Podmínky

## Smyčky
### for
#### pass/...
### foreach

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
