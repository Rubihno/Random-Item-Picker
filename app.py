import random, json


def opslaan(data):
    """
        Saves the data to the json file. 

        Arguments:
            data (dict): the list that needs to be saved to the json file
    """
    try:
        with open("opslag.json", "r") as f:
            bestaande_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        bestaande_data = {}

    bestaande_data.update(data)

    with open("opslag.json", "w") as f:
        json.dump(bestaande_data, f, indent=4)

# Wordt gebruikt om data te verwijderen
def verwijderen_data(data):
    try:
        with open("opslag.json", "w") as f:
            json.dump(data, f, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found")

# Laad de huidige data
def ophalen():
    with open("opslag.json", "r") as f:
        return json.load(f)

lijst = {}

# Maakt een lijst met items en voegt dit dit toe
def lijst_maken():
    naam = []
    naam_key = input("Wat wil je toevoegen aan de lijst? Typ series als je series wil toevoegen etc.")
    aantal = int(input("Hoeveel items wil je toevoegen?"))
    for i in range(aantal):
        optie = input(f"Welke item wil je toevoegen aan de lijst?")
        naam.append(optie)
    lijst[naam_key] = naam
    opslaan(lijst)

# Voeg 1 of meerdere items toe
def item_toevoegen(data):
    toevoegen_lijst = input("Aan welke lijst wil je een item toevoegen?")
    aantal = int(input("Hoeveel items wil je toevoegen?"))
    for i in range(aantal):
        toevoegen_item = input("Welk item wil je toevoegen?")
        data[toevoegen_lijst].append(toevoegen_item)
    print(data[toevoegen_lijst])
    opslaan(data)

# Delete een lijst of item
def item_verwijderen(data):
    volledig_of_item = input("Wil je een item uit een lijst of een hele lijst verwijderen?")
    if volledig_of_item == "item":
        verwijderen_lijst = input("Van welke lijst wil je een item verwijderen?")
        item_lijst = input("Welk item wil je verwijderen?")
        data[verwijderen_lijst].remove(item_lijst)
    else:
        lijst = input("Welke lijst wil je verwijderen?")
        del data[lijst] 
    verwijderen_data(data)

def error(actie):
    try:
        actie
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        print("Deze lijst bestaat niet of er zijn nog geen lijsten toegevoegd!")

def random_item():
    item = input("Uit welke lijst wil je een item krijgen?")
    keuze = random.choice(list(data_ophalen[item]))
    print(keuze)
    return keuze

toevoegen_of_random = int(input("Wil je een lijst toevoegen, item toevoegen, random item uit lijst of een lijst/item verwijderen? Typ 0 voor lijst toevoegen, 1 voor item toevoegen etc."))
data_ophalen = ophalen()

if toevoegen_of_random == 0: 
    error(lijst_maken())
elif toevoegen_of_random == 1:
    error(item_toevoegen(data_ophalen))
elif toevoegen_of_random == 2:
    error(random_item())
elif toevoegen_of_random == 3:
    error(item_verwijderen(data_ophalen))
else:
    print("Deze optie bestaat niet! Typ 0 voor lijst toevoegen, 1 voor item toevoegen etc.")
