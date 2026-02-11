"""
Olvasd be a labdarugok.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány játékos szerepel a fájlban?
2. Melyik játékos szerezte a legkevesebb gólt?
3. Melyik játékos szerzett a legtöbb gólt?
4. Ki játszott a legtöbb mérkőzést?
5. Átlagosan hány gólt szerzett egy játékos?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerzett a legtöbb gólt? (feltételezve, hogy egy játékos csak egy csapatban játszott)


A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""


print("A beolvasott fájlban összesen ____ játékos szerepel.")
print("A legkevesebb gólt szerző játékos: ____")
print("A legtöbb gólt szerző játékos: ____")
print("A legtöbb mérkőzést játszó játékos: ____")
print("Az átlagos gólszám: ____")
print("***A legtöbb gólt szerző csapat: ____")

forras = "beolvasando_adatok/labdarugok.txt"
cel = "statisztika.txt"

nevek = []
csapatok = []
meccsek = []
golok = []

f = open(forras, "r", encoding="utf-8")

f.readline() 

for sor in f:
    sor = sor.strip()
    if sor:
        adat = sor.split(";")
        nevek.append(adat[0])
        csapatok.append(adat[1])
        meccsek.append(int(adat[2]))
        golok.append(int(adat[3]))
f.close()


