tekst = str(input("Sisesta tekst: "))
hind = float(input("Sisestage 1 kauba hind: "))
kogus = int(input("Sisesta kogus: "))
riik = input("Sisestage riigi kood: ").upper()
def kaibemaks(riigikood):
    if riigikood == "AL":
        return 4
    elif riigikood == "CA":
        return 8.25
    elif riigikood == "TX":
        return 6.25
    elif riigikood == "NV":
        return 6
    elif riigikood == "UT":
        return 6.85
    else:
        return 0
koguhind = hind * kogus
lopuhind = round(koguhind + ((koguhind / 100) * kaibemaks(riik)),2)
print("See on teie tekst: " + tekst)
print("Ühe kauba hind on: " + str(hind) )
print("Teie kogus on: " + str(kogus) )
print("Kogu kauba hind on : " + str(koguhind))
print("Teie riigi kood on" + str(riik))
print(riik, "maks on", kaibemaks(riik), "%")
print("Teie lõpuhind on: " + str(lopuhind))