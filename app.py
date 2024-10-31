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

def bestaat_lijst(lijst, data):
    if lijst not in data:
        return False
    return True

lijst = {}

# Maakt een lijst met items en voegt dit dit toe
def lijst_maken():
    naam = []
    naam_key = input("Wat is de naam van de lijst? Typ series als je een lijst met series wil toevoegen etc.")
    aantal = int(input("Hoeveel items wil je toevoegen?"))
    for i in range(aantal):
        optie = input(f"Welke item wil je toevoegen aan de lijst?")
        naam.append(optie)
    lijst[naam_key] = naam
    opslaan(lijst)

# Voeg 1 of meerdere items toe
def item_toevoegen(data):
    lijst = input("Aan welke lijst wil je een item toevoegen?")
    if bestaat_lijst(lijst, data) == False:
        return
    aantal = int(input("Hoeveel items wil je toevoegen?"))
    for i in range(aantal):
        toevoegen_item = input("Welk item wil je toevoegen?")
        data[lijst].append(toevoegen_item)
    print(data[lijst])
    opslaan(data)

# Delete een lijst of item
def item_verwijderen(data):
    lijst_of_item = input("Wil je een item uit een lijst of een hele lijst verwijderen?")
    if lijst_of_item == "item":
        lijst = input("Van welke lijst wil je een item verwijderen?")
        if bestaat_lijst(lijst, data) == False:
            return
        item_lijst = input("Welk item wil je verwijderen?")
        data[lijst].remove(item_lijst)
    else:
        lijst = input("Welke lijst wil je verwijderen?")
        if bestaat_lijst(lijst, data) == False:
            return
        del data[lijst] 
    verwijderen_data(data)

def error(actie):
    try:
        actie()
    except(KeyError,FileNotFoundError, json.JSONDecodeError, TypeError):
        return print("Deze lijst bestaat niet of er zijn nog geen lijsten toegevoegd!")

def random_item():
    item = input("Uit welke lijst wil je een item krijgen?")
    keuze = random.choice(list(data_ophalen[item]))
    print(keuze)
    return keuze

toevoegen_of_random = int(input("Wil je een lijst toevoegen, item toevoegen, random item uit lijst of een lijst/item verwijderen? Typ 0 voor lijst toevoegen, 1 voor item toevoegen etc."))
data_ophalen = ophalen()
functies = [lambda: error(lijst_maken),lambda: error(item_toevoegen(data_ophalen)),lambda: error(random_item),lambda: error(item_verwijderen(data_ophalen))]

functies[toevoegen_of_random]()