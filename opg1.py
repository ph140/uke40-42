# O P P G A V E  1

# tall = int(input('Tall: \n'))


def primtallsum(sum):
    primliste = [2]
    x = 2
    primsum = 2
    while primsum < sum:
        for i in range(2, x):
            if x % i == 0:
                break
            elif x == i+1 or x == 2:
                primliste.append(x)
                primsum = primsum + x

        x += 1

    # E N U M E R A T E
    for i, j in enumerate(primliste):
        if i in primliste:
            print(j)
            pass

    # listelengde = len(primliste)
    # return listelengde
    return primliste


# print(primtallsum(10000))


# O P P G A V E  2

lag = "Molde Brann Vålerenga Haugesund Mjøndalen"

tippelagliste = ["Bodø/glimt", "Molde", "Odd", "Rosenberg",
                 "Kristiansund", "Vålerenga", "Brann", "Haugesund",
                 "Stabæk", "Viking", "Strømsgodset", "Sarpsborg 08",
                 "Sandefjord", "Start", "Mjøndalen", "Aalesund"]


def listehandtering(lag, tippelaglisteliste):
    # Splitter opp lagene etter mellomrom
    lag = lag.split(" ")

    for i in tippelagliste:
        # Gå gjennom alle lagene i tippeligaen og legger til de
        # om de ikke er i den andre lag-listen
        if i not in lag:
            lag.append(i)

    # Reverserer og returnerer den oppdaterte listen.
    lag.sort(reverse=True)
    return lag


def opprykk(tippelag, oboslag):
    # Fjerner tippelaget og legger til oboslaget i tippeligalisten
    tippelagliste.remove(tippelag)
    tippelagliste.append(oboslag)

    # Reverserer og returnerer tippeligalisten
    tippelagliste.sort(reverse=True)
    return tippelagliste


# listehandtering(lag, tippelagliste)
# print(opprykk("Stabæk", "Ranheim"))


# O P P G A V E  3

valorer = {"kronestykke": 1, "femkrone": 5, "tikrone": 10, "tjuekrone": 20,
           "femtilapp": 50, "hundrelapp": 100, "tohundrelapp": 200,
           "femhundrelapp": 500, "tusenlapp": 1000}

kassabeholdning = {"kronestykke": 5, "femkrone": 5, "tikrone": 5,
                   "tjuekrone": 5, "femtilapp": 5, "hundrelapp": 5,
                   "tohundrelapp": 5, "femhundrelapp": 5, "tusenlapp": 5}


def vekslepenger(betalt, pris):
    veksel = betalt - pris

    if veksel < 0:
        print('Kunden betalte for lite')
    elif not veksel:
        print('Kunden har betalt akkurat nok')
    else:
        for navn, verdi in reversed(valorer.items()):
            antall = veksel // verdi
            veksel -= verdi * antall
            if antall:
                print(antall, navn)


def innskudd():
    # Tar inn input med f.eks '2 hundrelapp'
    verdi = input('Skriv hva du vil sette inn i banken: \n')

    antall = int(verdi.split(' ')[0])
    navn = verdi.split(' ')[1]

    kassabeholdning[navn] += antall
    return kassabeholdning


def ernok(navn):
    if kassabeholdning[navn] > 0:
        return True


def uttak(belop):
    if belop < 0:
        return False
    else:
        for navn in reversed(valorer):
            while ernok(navn) and belop >= valorer[navn]:
                kassabeholdning[navn] -= 1
                belop -= valorer[navn]

    return kassabeholdning


def pengebehandling(metode):
    metode()


# vekslepenger(108, 80)
# print(innskudd())
# print(uttak(100))
pengebehandling(innskudd)
