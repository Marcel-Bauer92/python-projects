"""
# def = definieren einer Funktion
def addieren(a, b) :
    # a und b sind Parameter für Zahlen
    #return gibt das Ergebnis zurück
    return a + b

#print zeigt es im Terminal an
print(addieren(3, 5))
"""

#Taschenrechner - Grundrechenarten

def addieren(a, b):
    return a + b

def subtrahieren(a, b):
    return a - b

def multiplizieren(a, b):
    return a * b

def dividieren(a, b):
    if b == 0:
        return "Fehler: Division durch 0 nicht möglich"
    return a / b 

"""
# Testausgaben
print(addieren(10, 5))
print(subtrahieren(10, 5))
print(multiplizieren(10, 5))
print(dividieren(10, 5))
print(dividieren(10, 0))
"""

"""
#Menü für den Nutzer

print("=== Taschenrechner ===")
print("1 - Addieren")
print("2 - Subtrahieren")
print("3 - Multiplizieren")
print("4 - Dividieren")

auswahl = input("Wähle eine Rechenart (1-4): ")

zahl1 = float(input("Erste Zahl: "))
zahl2 = float(input("Zweite Zahl: "))

if auswahl == "1":
    print("Ergebenis:", addieren(zahl1, zahl2))

elif auswahl == "2":
    print("Ergebenis:", subtrahieren(zahl1, zahl2))

elif auswahl == "3":
    print("Ergebnis:", multiplizieren(zahl1, zahl2))

elif auswahl == "4":
    print("Ergebenis:", dividieren(zahl1, zahl2))

else:
    print("Ungültige Auswahl!")    
"""

# Schleife damit der Rechner mehrmals benutzt werden kann

while True:
    print("\n=== Taschenrechner ===")
    print("1 - Addieren")
    print("2 - Subtrahieren")
    print("3 - Multiplizieren")
    print("4 - Dividieren")
    print("5 - Prozentrechnen")
    print("6 - Beenden")
#while True ist eine Endlosschleife – der Code darin wiederholt sich für immer
    auswahl = input("Wähle eine Rechenart (1-5): ")
    if auswahl not in ["1", "2", "3", "4", "5", "6"]:
        print("Bitte nur 1-5 eingeben!")
        continue 
 #not in prüft ob ein Wert nicht in einer Liste vorkommt
 #Wenn die Auswahl ungültig ist, springt continue direkt zurück zum Anfang der Schleife – ohne die Zahleneingabe abzufragen    
    if auswahl == "6":
        print("Tschüss!")
        break
#break bricht die Schleife ab – in diesem Fall wenn der Nutzer 6 drückt
    try:
        zahl1 = float(input("Erste Zahl: "))
        zahl2 = float(input("Zweite Zahl: "))
    except ValueError:
        print("Bitte nur Zahlen eingeben!")
        continue    
#float() wandelt die Eingabe (die Python erstmal als Text behandelt) in eine Dezimalzahl um – ohne das könntest du nicht rechnen
#input() hält das Programm an und wartet auf eine Eingabe vom Nutzer
    if auswahl == "1":
        print("Ergebnis:", addieren(zahl1, zahl2))
    elif auswahl == "2":
        print("Ergebnis:", subtrahieren(zahl1, zahl2))
    elif auswahl == "3":
        print("Ergebnis:", multiplizieren(zahl1, zahl2))
    elif auswahl == "4":
        print("Ergebnis:", dividieren(zahl1, zahl2))
    elif auswahl == "5":
        print("Ergebnis:", (zahl1 / 100) * zahl2)
    else:
        print("Ungültige Auswahl!")
#elif bedeutet "sonst wenn" – eine Kette von Bedingungen
#else greift wenn keine der Bedingungen zutrifft         