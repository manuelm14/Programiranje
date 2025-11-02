def ispisi_izbornik():
    # Izbornik za kalkulator
    print("----------------------")
    print("Izbornik za kalkulator")
    print("----------------------")
    print("1. Izračun napona struje")
    print("2. Izračun otpora struje")
    print("3. Izračun jakosti struje")
    print("4. Izračun ukupnog serijskog otpora (N otpornika)")
    print("0. Izlaz")
    print("----------------------")

def izracunaj_sumu_liste(lista_vrijednosti):
    suma=0
    for vrijednost in lista_vrijednosti:
        suma+=vrijednost
    return suma

def izracunaj_napon(jakost, otpor):
    return jakost * otpor

def izracunaj_otpor(napon, jakost):
    return napon / jakost

def izracunaj_jakost(napon, otpor):
    return napon / otpor


while True:
    ispisi_izbornik()

    try:
        opcija = int(input("Izaberite operaciju (1 / 2 / 3 / 4 / 0):"))
    except Exception as greska:
        print(f"Pogrešan unos. Molimo unesite brojeve od 1 do 4. \nOdaberite 0 za izlaz.")
        continue
    #Struktura grananja
    if opcija == 1:     # == != < > <> >= <= - operatori usporedbe
        print("Izračun napona struje")
        try:
            jakost = int(input("Upiši jakost struje: "))
            otpor = int(input("Upiši otpor: "))
            napon = izracunaj_napon(jakost, otpor)
        except ValueError:
            print(f"Molimo unesite brojeve")
            continue
        except Exception as greska:
            print(f"Pogrešan unos:{greska}.\nMolimo unesite brojeve")
            continue
        
        
        print(f"Napon struje je: {napon} V")
    elif opcija == 2:
        print("Izračun otpora struje")
        try:
            napon = int(input("Upiši napon: "))
            jakost = int(input("Upiši jakost struje: "))
            otpor = izracunaj_otpor(napon, jakost)
        except ValueError:
            print(f"Molimo unesite brojeve")
            continue
        except ZeroDivisionError:
            print("Ne mogu dijeliti s nulom")
            continue
        except Exception as greška:
            print(f"Pogrešan unos:{greška}.\nMolimo unesite brojeve")
            continue

        print(f"Otpor je: {otpor} Ohm")
    elif opcija == 3:
        print("Izračun jakosti struje")
        try:
            napon = int(input("Upiši napon: "))
            otpor = int(input("Upiši otpor: "))
            jakost = izracunaj_jakost(napon, otpor)
        except ValueError:
            print(f"Molimo unesite brojeve")
            continue
        except ZeroDivisionError:
            print("Ne mogu dijeliti s nulom")
            continue
        except Exception as greska:
            print(f"Pogrešan unos:{greska}.\nMolimo unesite brojeve")
            continue
        print(f"Jakost struje je: {jakost} A")
    elif opcija==4:
        print("\n---Izračun serijskog otpora(N otpornika)---")
        lista_otpora=[]
        while True:
            print(f"   Trenutni otpornici u listi: {[f'{x:.2f} Ω' for x in lista_otpora]}")
            unos_str = input("Unesite vrijednost otpora (ili 'kraj' za izračun): ")
            
            if unos_str.lower() == 'kraj':
                break
            try:
                    vrijednost = float(unos_str)
                    if vrijednost<=0:
                            print("GREŠKA: Otpor mora biti pozitivan broj.")
                    else:lista_otpora.append(vrijednost)
                    print(f"   -> Dodan otpornik: {vrijednost} Ω")
            except ValueError:
                print("GREŠKA: Unos mora biti ispravan broj ili riječ 'kraj'.")

            if len(lista_otpora) > 0:
                ukupni_otpor = izracunaj_sumu_liste(lista_otpora)
                print(f"\nREZULTAT: Ukupan serijski otpor za {len(lista_otpora)} otpornika je: {ukupni_otpor:.4f} Ω")
            else:
                print("\nNiste unijeli nijedan otpornik. Povratak na izbornik.")
                input("\nPritisnite Enter za povratak na glavni izbornik...") 
    elif opcija==0:
            print  ("Hvala na korištenju kalkulatora.")
            break
    else:
            print("Pogrešan unos")