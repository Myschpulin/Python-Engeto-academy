TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
ODDDELOVAC = ("=") * 52
# UZIVATELE + hesla
UZIVATELE = { 'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
# promene pro analyzu textu
pocet_velka_pismena = 0
pocet_velkych_slov = 0
pocet_mala_pismena = 0
pocet_cisel = 0
soucet_cisel = 0
vyskyt = {}

# Uvod do analyzatoru
print(ODDDELOVAC, "Vitejte v textovem analyzatoru, prihlaste se prosim!", ODDDELOVAC, sep=("\n"))
# Vyzadani a zadani uzivatelskeho jmena
while True:
    zadani_UZIVATELE = input("Zadejte uzivatelske jmeno: ")
    zadani_hesla = input("Zadejte vase heslo: ")

    if UZIVATELE.get(zadani_UZIVATELE) != zadani_hesla:
        print(f"Spatne prihlasovaci udaje".upper())
    else:
        print("Uspesne prihlaseni".upper())
        break

# Hlaseni poctu textu
print(ODDDELOVAC,"Mame pro vas prichystanou analyzu 3 textu!", ODDDELOVAC, sep=("\n"))

# Vyber a kontrola cisla textu
while True:
        vyber_textu = input("Zvolte cislici od 1 do 3: ")
        if vyber_textu.isnumeric() and int(vyber_textu) in [1, 2, 3]:
            print(f"Vyborne, zvolil jste text cislo {vyber_textu}!")
            break
        elif vyber_textu.isnumeric() and int(vyber_textu) not in [1, 2, 3]:
             print("Zvolte prosim cislici 1 - 3 !")
        else:
            print("Zkuste to prosim znovu, nezadal jste cislici.")

# Analyza textu
for slovo in TEXTS[int(vyber_textu) - 1].split():
    slovo = slovo.strip(".:,")

    if len(slovo) not in vyskyt:
        vyskyt[len(slovo)] = 1
    else:
        vyskyt[len(slovo)] += 1

    if slovo[0].islower():
            pocet_mala_pismena = pocet_mala_pismena + 1
    elif slovo[0].isupper():
            pocet_velka_pismena = pocet_velka_pismena + 1
    elif slovo.istitle():
            pocet_velkych_slov = pocet_velkych_slov + 1
    elif slovo.isdigit():
            pocet_cisel = pocet_cisel + 1
            soucet_cisel += int(slovo)

 # Vystup 1. analyzy textu
print(
        ODDDELOVAC,
      f"Zvoleny text obsahuje {len(TEXTS[int(vyber_textu) - 1].split())} slov",
      f" Zvoleny text obsahuje {pocet_mala_pismena} slov, zacinajicich malym pismenem!",
      f" Zvoleny text obsahuje {pocet_velka_pismena} slov, zacinajicich velkym pismen!",
      f" Zvoleny text obsahuje {pocet_velkych_slov} slov, psanych velkym pismem!",
      f" Zvoleny text obsahuje {pocet_cisel} pocet cisel!",
      ODDDELOVAC,
      sep=("\n")
      )

# Vystup cetnosti slov
for (slovicko) in sorted(vyskyt):
    print(f"{slovicko} {vyskyt[slovicko] * '*'} {vyskyt[slovicko]}")

# Soucet cisel v textu + konecny vystup
print(ODDDELOVAC,f"Sectenim cisel v tomto textu, dostaneme hodnotu {soucet_cisel}!", ODDDELOVAC, sep=("\n"))
