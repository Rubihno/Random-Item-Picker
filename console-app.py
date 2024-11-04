import random, json

def opslaan(data):
    """
        Saves the data to the json file. 

        Arguments:
            data (list): the list that needs to be saved to the json file
    """
    try:
        with open("console-opslag.json", "r") as f:
            bestaande_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        bestaande_data = {}

    bestaande_data.update(data)

    with open("console-opslag.json", "w") as f:
        json.dump(bestaande_data, f, indent=4)

def verwijderen_data(data):
    """
        Wordt gebruikt om data te verwijderen

        Arguments:
            data (dict): huidige data van de json file
    """
    try:
        with open("console-opslag.json", "w") as f:
            json.dump(data, f, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File niet gevonden!")

# Laad de huidige data
def ophalen():
    with open("console-opslag.json", "r") as f:
        return json.load(f)

def bestaat_lijst(lijst, data):
    """
        Kijkt of een lijst bestaat

        Arguments:
            data (dict): huidige data van de json file
            lijst (string): naam van de lijst
    """
    if lijst not in data:
        raise KeyError
    return True

def error(actie):
    """
        Voert een functie uit en geeft een error message als iets niet werkt

        Arguments:
            actie (functie): huidige data van de json file
    """
    try:
        actie(data_ophalen)
    except(KeyError,FileNotFoundError, json.JSONDecodeError):
        return print("Deze lijst bestaat niet of er zijn nog geen lijsten toegevoegd!")

lijst = {}

def lijst_maken(data):
    """
        Maakt een lijst met items en voegt dit toe

        Arguments:
            data (dict): huidige data van de json file
    """
    naam = []
    naam_key = input("Wat is de naam van de lijst? Typ series als je een lijst met series wil toevoegen etc.")
    if naam_key not in data:
        aantal = int(input("Hoeveel items wil je toevoegen?"))
        for i in range(aantal):
            optie = input(f"Welke item wil je toevoegen aan de lijst?")
            naam.append(optie)
        lijst[naam_key] = naam
        opslaan(lijst)

def item_toevoegen(data):
    """
        Voegt 1 of meerdere items toe

        Arguments:
            data (dict): huidige data van de json file
    """
    lijst = input("Aan welke lijst wil je een item toevoegen?")
    if bestaat_lijst(lijst, data) == KeyError:
        return
    aantal = int(input("Hoeveel items wil je toevoegen?"))
    for i in range(aantal):
        toevoegen_item = input("Welk item wil je toevoegen?")
        data[lijst].append(toevoegen_item)
    print(data[lijst])
    opslaan(data)

def item_verwijderen(data):
    """
        Delete een lijst of item

        Arguments:
            data (dict): huidige data van de json file
    """
    lijst_of_item = input("Wil je een item uit een lijst of een hele lijst verwijderen?")
    if lijst_of_item == "item":
        lijst = input("Van welke lijst wil je een item verwijderen?")
        if bestaat_lijst(lijst, data) == KeyError:
            return
        item_lijst = input("Welk item wil je verwijderen?")
        data[lijst].remove(item_lijst)
    else:
        lijst = input("Welke lijst wil je verwijderen?")
        if bestaat_lijst(lijst, data) == KeyError:
            return
        del data[lijst] 
    verwijderen_data(data)

def random_item(data):
    """
        Kiest een item uit een lijst

        Arguments:
            data (list): huidige data van de json file

        Return: 
            keuze (string): item uit een lijst
    """
    lijst = input("Uit welke lijst wil je een item krijgen?")
    if bestaat_lijst(lijst, data) == KeyError:
        return
    keuze = random.choice(list(data_ophalen[lijst]))
    print(keuze)
    return keuze

toevoegen_of_random = int(input("Wil je een lijst toevoegen, item toevoegen, random item uit lijst of een lijst/item verwijderen? Typ 0 voor lijst toevoegen, 1 voor item toevoegen etc."))
data_ophalen = ophalen()

# lambda zorgt ervoor dat een functie alleen wordt uitgevoerd als deze aangeroepen wordt, zo wordt niet constant de eerste functie uit de list uitgevoerd
functies = [lambda: error(lijst_maken),lambda: error(item_toevoegen),lambda: error(random_item),lambda: error(item_verwijderen)]

functies[toevoegen_of_random]()