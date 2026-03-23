import secrets
import string

def generiere_passwort(laenge, zahl_erlaubt, sonder_erlaubt):
    # Basis: Immer Groß- und Kleingeschriebene Buchstaben
    pool = string.ascii_letters
    
    if zahl_erlaubt:
        pool += string.digits
        
    if sonder_erlaubt:
        pool += string.punctuation

    # Das Passwort sicher generieren
    passwort = ''.join(secrets.choice(pool) for i in range(laenge))
    return passwort

def main():
    print("--- Willkommen beim Python Passwort-Generator ---")
    
    try:
        # Benutzereingaben abfragen
        laenge = int(input("Wie lang soll das Passwort sein? (z.B. 16): "))
        
        zahlen = input("Sollen Zahlen enthalten sein? (j/n): ").lower() == 'j'
        sonder = input("Sollen Sonderzeichen enthalten sein? (j/n): ").lower() == 'j'
        
        # Passwort erstellen
        ergebnis = generiere_passwort(laenge, zahlen, sonder)
        
        print("\n" + "="*30)
        print(f"DEIN PASSWORT: {ergebnis}")
        print("="*30)
        
        # Optional: In Datei speichern
        speichern = input("\nIn 'passwort.txt' speichern? (j/n): ").lower()
        if speichern == 'j':
            with open("passwort.txt", "a") as file:
                file.write(f"Passwort: {ergebnis}\n")
            print("Erfolgreich gespeichert!")

    except ValueError:
        print("Fehler: Bitte gib für die Länge eine gültige Zahl ein!")

    # Verhindert, dass sich das Fenster sofort schließt
    input("\nDrücke Enter zum Beenden...")

if __name__ == "__main__":
    main()
