while True:
    print("--------------------")
    print("Pozdrav, molim vas izaberite sljedeću opciju:")
    print("--------------------")
    print("1.Pretvorba iz volti(V)  u milivolte(mV)")
    print("2.Pretvorba iz ohmi(Ω) u kiloohme(kΩ)")
    print("3.Pretvorba iz ampera(A) u miliampere(mA)")
    print("0.Izlaz iz pretvarača mjernih jednica")
    print("--------------------")
    try:
        opcija=int(input("Izaberite opciju(1/2/3/0):"))
    except Exception as greska:
        print(f"Pogrešan unos.{greska}")
        continue
    if opcija==0:
        print(f"Izašli ste iz pretvarača mjernih jedinica, doviđenja!")
        break
    elif opcija==1:
        print("Pretvroba iz volti(V) u milivolte(mV)")
        napon=float(input("Upišite napon:"))
        naponm=(napon)*1000
        print(f"Napon struje {napon} V je jednako {naponm} mV")
    elif opcija==2:
        print("Pretvorba iz ohmi(Ω) u kiloohme(kΩ)")
        otpor=float(input("Upišite otpor:"))
        otpork=(otpor)/1000
        print(f"Otpor struje {otpor} Ω je jednako {otpork} kΩ")
    elif opcija==3:
        print("Pretvorba iz ampera(A) u miliampere(mA)")
        jakost=float(input("Upišite jakost struje:"))
        jakostm=(jakost)*1000
        print(f"Jakost struje {jakost} A je jednako {jakostm} mA")
    else:
        print("Pogrešan unos.")