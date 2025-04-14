participants = 0
most_wins = -1
most_wins_driver = None
most_races = -1
most_races_driver = None
total_races = 0

try:
    with open("beolvasando_adatok/f1.txt", "r", encoding="utf-8") as f:
        header = f.readline()
        for line in f:
            data = line.strip().split(";")
            if len(data) != 4:
                continue
            
            driver = data[0]
            wins = int(data[2])
            races = int(data[3])
            
            participants += 1
            
            if wins > most_wins:
                most_wins = wins
                most_wins_driver = driver
            
            if races > most_races:
                most_races = races
                most_races_driver = driver
            
            total_races += races

    average_races = total_races / participants if participants > 0 else 0
    
    print(f"\n1. A beolvasott fájlban összesen {participants} versenyző szerepel.\n")
    print(f"2. A legtöbb futamot nyert versenyző: {most_wins_driver}\n")
    print(f"3. A legtöbb futamot teljesített versenyző: {most_races_driver}\n")
    print(f"4. Az átlagos futamszám: {average_races:.2f}\n")

except FileNotFoundError:
    print("Hiba: A 'f1.txt' fájl nem található.")