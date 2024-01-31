
# vytvoření kodu který vezme data z csv souboru a přehází jeho řádky 
import csv
import shutil
import random
import time
import datetime

def zaloguj(zprava, typ="INFO"):
    casove_razitko = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_zprava = f"[{casove_razitko}] {typ}: {zprava}"
    print(log_zprava) #vytiknuti log zamznamu 

while True:
    source = r"C:\Users\ucite\Desktop\Programování\python\hello\sales_data.csv"

    destination =  r"C:\Users\ucite\Desktop\Programování\python\hello\sale_new_data.csv"

    shutil.copy(source, destination)

    #   Otevření souboru CSV
    with open(r"C:\Users\ucite\Desktop\Programování\python\hello\sales_data.csv", newline='') as csvfile:
 
        # Vytvoření čtečky CSV
        csvreader = csv.reader(csvfile)

    

        header = next(csvreader)
        data = list(csvreader)
    

        # Vytisknutí původních  dat, nedulezite, pouze pro kontrolu
        print(header)

        for row in data:
            print(row)  # Vytiskne každý řádek jako seznam

 
    random.shuffle(data)
    try:
        with open(r"C:\Users\ucite\Desktop\Programování\python\hello\sales_data.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)  # Zapsání hlavičky zpět na první řádek
            writer.writerows(data)   # Zapsání zamíchaných dat
        zaloguj("Data úspěšně zamíchána a zapsána.")
    except Exception as e:
        zaloguj(f"Při zamíchání nebo zápisu dat došlo k chybě: {e}", "ERROR")


    with open(r"C:\Users\ucite\Desktop\Programování\python\hello\sales_data.csv", newline='') as csvfile:
 
        # Vytvoření čtečky CSV
        csvreader = csv.reader(csvfile)

        print(header)

        # Vytisknutí nových dat, nedulezite, pouze pro kotrolu
        for row in data:
            print(row)  # Vytiskne každý řádek jako seznam

        time.sleep(10)



