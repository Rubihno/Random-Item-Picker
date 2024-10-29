import random, json

def opslaan(data):
    try:
        with open("opslag.json", "r") as f:
            bestaande_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        bestaande_data = {}

    bestaande_data.update(data)

    with open("opslag.json", "w") as f:
        json.dump(bestaande_data, f, indent=4)

def ophalen():
    with open("opslag.json", "r") as f:
        return json.load(f)

lijst = {}    
data_opslaan = opslaan(lijst)
data_ophalen = ophalen()

def lijst_maken():
    naam = []
    naam_key = input("Wat wil je toevoegen aan de lijst? Typ series als je series wil toevoegen etc.")
    aantal = int(input("Hoeveel items wil je toevoegen?"))
    for i in range(aantal):
        optie = input(f"Welke item wil je toevoegen aan de lijst?")
        naam.append(optie)
    lijst[naam_key] = naam
    opslaan(lijst)

def item_toevoegen(data):
    toevoegen_lijst = input("Aan welke lijst wil je een item toevoegen?")
    aantal = int(input("Hoeveel items wil je toevoegen?"))
    for i in range(aantal):
        toevoegen_item = input("Welk item wil je toevoegen?")
        data[toevoegen_lijst].append(toevoegen_item)
    print(data[toevoegen_lijst])

def item_verwijderen(data):
    volledig_of_item = input("Wil je een lijst of een item uit een lijst verwijderen?")
    if volledig_of_item == "item":
        verwijderen_lijst = input("Aan welke lijst wil je een item toevoegen?")
        item_lijst = input("Welk item wil je verwijderen?")
        data[verwijderen_lijst].remove(item_lijst)
    else:
        lijst = input("Welke lijst?")
        del data[lijst]
        
    opslaan(data)
item_verwijderen(data_ophalen)
print(data_ophalen)
def random_item():
    item = input("Uit welke lijst wil je een item krijgen?")
    keuze = random.choice(list(data_ophalen[item]))
    print(keuze)
    return keuze

toevoegen_of_random = int(input("Wil je een lijst toevoegen of wil je een random item uit een beschikbare lijst? 0 voor toevoegen, 1 voor random item"))

if toevoegen_of_random == 0: 
    lijst_maken()
elif toevoegen_of_random == 1:
    try: 
        random_item()
    except (json.JSONDecodeError, FileNotFoundError):
        print("Deze lijst bestaat niet of er zijn nog geen lijsten toegevoegd!")
else:
    print("Deze optie bestaat niet! U kunt alleen een lijst toevoegen en uit een bestaande lijst een item krijgen.")
