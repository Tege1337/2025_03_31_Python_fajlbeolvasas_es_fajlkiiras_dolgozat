"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!
Név; Csapat; Győzelmek száma; Teljesített futamok száma


1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""

f = open("beolvasando_adatok/f1.txt", "rt")


#task 1
participants = 0
for x in f:
    participants += 1

#task 2
most_w_p = "tege"
most_wins = 0
most_r_p = "asd"
most_races = 0
futamok = 0

with open("beolvasando_adatok/f1.txt", "r") as f:
    for line in f:
        data = line.strip().split(";")

        wins = int(data[2])
        person = data[0]
        if wins > most_wins:
            most_wins = wins
            most_w_p = person

        races = int(data[3])
        person2 = data[0]
        if races > most_races:
            most_races = races
            most_r_p = person2

        for l in f:
            futamok += int(data[3])

futam_atl = futamok / participants

print(f"\nA beolvasott fájlban összesen {participants} versenyző szerepel.")
print(f"A legtöbb futamot nyert versenyző: {most_w_p}")
print(f"A legtöbb futamot teljesített versenyző: {most_r_p}")
print(f"Az átlagos futamszám: {futam_atl}\n")