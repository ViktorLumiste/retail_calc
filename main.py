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
def soodustus(hind):
    if hind >= 50000:
        return 15
    elif hind >= 10000:
        return 10
    elif hind >= 7000:
        return 7
    elif hind >= 5000:
        return 5
    elif hind >= 1000:
        return 3
    else:
        return 0
koguhind = hind * kogus
lopuhind = round(koguhind + ((koguhind / 100) * kaibemaks(riik)),2)
soodushind = round(koguhind - (koguhind / 100 * soodustus(hind)), 2)
lopuhind = round(soodushind + ((soodushind / 100) * kaibemaks(riik)), 2)
print("Teie kogus on: " + str(kogus))
print("Teie 1 kauba hind on: " + str(hind) + " €")
print("Teie käibemaksu määr on: " + str(kaibemaks(riik)) + "%")
print("Teie soodustus protsent on " + str(soodustus(hind)) + "%")
print("Teie koguhind on: " + str(koguhind))
print("Teie soodusega hind on: " + str(soodushind))
print("Teie koguhind koos soodustusega ja maksutega on: " + str(lopuhind))