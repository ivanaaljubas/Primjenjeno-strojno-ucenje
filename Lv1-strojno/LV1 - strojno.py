"""1. zadatak
def total_euro(hours_worked, hourly_rate):
    total = hours_worked * hourly_rate
    return total

def main():
    hours_worked = float(input("Radni sati: "))
    hourly_rate = float(input("eura/h: "))

    total = total_euro(hours_worked, hourly_rate)

    print("Ukupno:", total, "eura")

if __name__ == "__main__":
    main()
"""
""" 2. zadatak
def grade_category(grade):
    if grade >= 0.9:
        return "A"
    elif grade >= 0.8:
        return "B"
    elif grade >= 0.7:
        return "C"
    elif grade >= 0.6:
        return "D"
    elif grade < 0.6 and grade >= 0.0:
        return "F"
    else:
        return "Ocjena je izvan intervala [0.0, 1.0]"

def main():
    try:
        grade = float(input("Unesite ocjenu (između 0.0 i 1.0): "))
        if grade < 0.0 or grade > 1.0:
            print("Ocjena je izvan intervala [0.0, 1.0].")
        else:
            category = grade_category(grade)
            print("Kategorija ocjene:", category)
    except ValueError:
        print("Greška: Unos treba biti broj između 0.0 i 1.0.")

if __name__ == "__main__":
    main()
    """
"""3. zadatak
def main():
    numbers = []
    while True:
        try:
            user_input = input("Unesite broj (ili 'Done' za završetak): ")
            if user_input.lower() == 'done':
                break
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Pogrešan unos. Molimo unesite broj ili 'Done' za završetak.")

    if numbers:
        print("Brojeva uneseno:", len(numbers))
        print("Srednja vrijednost:", sum(numbers) / len(numbers))
        print("Minimalna vrijednost:", min(numbers))
        print("Maksimalna vrijednost:", max(numbers))

        sorted_numbers = sorted(numbers)
        print("Sortirana lista brojeva:", sorted_numbers)
    else:
        print("Niste unijeli nijedan broj.")

if __name__ == "__main__":
    main()
"""
""" 4. zadatak
def izracunaj_prosjek_pouzdanosti(ime_datoteke):
    try:
        datoteka = open(ime_datoteke)
        broj_linija = 0
        suma_pouzdanosti = 0

        for linija in datoteka:
            if linija.startswith("X-DSPAM-Confidence:"):
                broj_linija += 1
                indeks_pouzdanosti = linija.find(":") + 1
                pouzdanost = float(linija[indeks_pouzdanosti:].strip())
                suma_pouzdanosti += pouzdanost

        if broj_linija == 0:
            print("Nema linija X-DSPAM-Confidence u datoteci.")
        else:
            prosjek_pouzdanosti = suma_pouzdanosti / broj_linija
            print("Prosječna X-DSPAM-Confidence:", prosjek_pouzdanosti)

        datoteka.close()

    except FileNotFoundError:
        print("Datoteka nije pronađena.")


ime_datoteke = input("Ime datoteke: ")
izracunaj_prosjek_pouzdanosti(ime_datoteke)
"""
""" 5.zadatak
def broj_rijeci_jedinstvenih(datoteka):
    try:
        with open(datoteka, 'r') as f:
            tekst = f.read()
            rijeci = tekst.split()

            rjecnik = {}
            for rijec in rijeci:
                rjecnik[rijec] = rjecnik.get(rijec, 0) + 1

            jedinstvene_rijeci = [rijec for rijec, broj in rjecnik.items() if broj == 1]
            
            print("Broj riječi koje se pojavljuju samo jednom:", len(jedinstvene_rijeci))
            print("Riječi koje se pojavljuju samo jednom:")
            for rijec in jedinstvene_rijeci:
                print(rijec)

    except FileNotFoundError:
        print("Datoteka nije pronađena.")


datoteka = "song.txt"
broj_rijeci_jedinstvenih(datoteka)
"""
""" 6.zadatak
def izracunaj_prosjek_rijeci(datoteka):
    try:
        with open(datoteka, 'r', encoding='utf-8') as f:
            sms_poruke = f.readlines()

            broj_ham_poruka = 0
            broj_rijeci_ham = 0
            broj_spam_poruka = 0
            broj_rijeci_spam = 0
            broj_spam_usklicnik = 0

            for poruka in sms_poruke:
                tip, tekst = poruka.strip().split("\t", 1)
                rijeci = tekst.split()
                broj_rijeci = len(rijeci)

                if tip == "ham":
                    broj_ham_poruka += 1
                    broj_rijeci_ham += broj_rijeci
                elif tip == "spam":
                    broj_spam_poruka += 1
                    broj_rijeci_spam += broj_rijeci
                    if tekst.endswith("!"):
                        broj_spam_usklicnik += 1

            if broj_ham_poruka > 0:
                prosjek_rijeci_ham = broj_rijeci_ham / broj_ham_poruka
                print("Prosječan broj riječi u ham porukama:", prosjek_rijeci_ham)
            else:
                print("Nema ham poruka u datoteci.")

            if broj_spam_poruka > 0:
                prosjek_rijeci_spam = broj_rijeci_spam / broj_spam_poruka
                print("Prosječan broj riječi u spam porukama:", prosjek_rijeci_spam)
                print("Broj spam poruka koje završavaju uskličnikom:", broj_spam_usklicnik)
            else:
                print("Nema spam poruka u datoteci.")

    except FileNotFoundError:
        print("Datoteka nije pronađena.")


datoteka = "SMSSpamCollection.txt"
izracunaj_prosjek_rijeci(datoteka)

"""