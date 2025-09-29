#Izbornik na kalkulator
print("---------------------")
print("Izbornik za kalkulator")
print("---------------------")
print("1. Izračun napona struje")
print("2. Izračun otpora struje")
print("3. Izračun jakosti struje")
print("4.Zbroj serijskih otpornika")
print("5.Zbroj paralelnih otpornika")
print("---------------------")
opcija=int(input("Izaberite operaciju(1/2/3/4/5): "))
#Struktura grananja
if opcija == 1 :    # == != < > <> >= <=
    print("Izračun napona struje")
    jakost=int(input("Upiši jakost struje: "))
    otpor=int(input("Upiši otpor: "))
    napon=jakost*otpor
    print(f"Napon struje je: {napon} V")
elif opcija == 2 :
    print("Izračun otpora struje")
    napon=int(input("Upiši napon struje: "))
    jakost=int(input("Upiši jakost struje: "))
    otpor=napon/jakost
    print(f"Otpor struje je: {otpor} Ω")
elif opcija == 3 :
    print("Izračun jakosti struje")
    napon=int(input("Upiši napon struje: "))
    otpor=int(input("Upiši otpor: "))
    jakost=napon/otpor
    print(f"Jakost struje je: {jakost} A")
elif opcija == 4 :
    print("Zbroj serijskih otpornika")
    otpor1=int(input("Upiši prvi otpor: "))
    otpor2=int(input("Upiši drugi otpor: "))
    zbroj=otpor1+otpor2
    print(f"Zbroj serijskih otpornika je: {zbroj} Ω")
elif opcija == 5 :
    print("Zbroj paralelnih otpornika")
    otpor1=int(input("Upiši prvi otpor: "))
    otpor2=int(input("Upiši drugi otpor: "))
    zbroj=1/(1/otpor1+1/otpor2)
    print(f"Zbroj paralelnih otpornika je: {zbroj} Ω")
else :
    print("Pogrešan unos")
