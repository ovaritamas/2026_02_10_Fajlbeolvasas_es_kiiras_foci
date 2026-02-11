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

letszam = len(nevek)
atlag_gol = sum(golok) / letszam

idx_min_gol = golok.index(min(golok))
idx_max_gol = golok.index(max(golok))
idx_max_meccs = meccsek.index(max(meccsek))

egyedi_csapatok = []
for cs in csapatok:
    if cs not in egyedi_csapatok:
        egyedi_csapatok.append(cs)

legjobb_csapat_nev = ""
legtobb_csapat_gol = -1

for csapat in egyedi_csapatok:
    csapat_osszes_gol = 0
    for i in range(letszam):
        if csapatok[i] == csapat:
            csapat_osszes_gol += golok[i]
    
    if csapat_osszes_gol > legtobb_csapat_gol:
        legtobb_csapat_gol = csapat_osszes_gol
        legjobb_csapat_nev = csapat

eredmeny_szoveg = f"""A beolvasott fájlban összesen {letszam} játékos szerepel.
A legkevesebb gólt szerző játékos: {nevek[idx_min_gol]}
A legtöbb gólt szerző játékos: {nevek[idx_max_gol]}
A legtöbb mérkőzést játszó játékos: {nevek[idx_max_meccs]}
Az átlagos gólszám: {atlag_gol:.2f}
***A legtöbb gólt szerző csapat: {legjobb_csapat_nev}"""

print(eredmeny_szoveg)

f_ki = open(cel, "w", encoding="utf-8")
f_ki.write(eredmeny_szoveg)
f_ki.close()

print("\nA statisztika.txt fájl sikeresen létrejött!")
