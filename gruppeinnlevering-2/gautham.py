poeng = 0
valg1 = ""
valg2 = ""
valg3 = ""

def lesvalg(spørsmål):

    svar = input(spørsmål).strip().upper()
    while svar not in("A","B"):
        print("Ugyldig valg. Vennligst velg A eller B.")
        svar = input(spørsmål).strip().upper()
    return svar


print("Uke 6: teamet er i storming-fasen ...")
print("Du er Erling, teamleder. Tre beslutninger avgjør hvordan det ender.")
print()


print("Beslutning 1: Silje og Elias")
print("Sakskonflikten har blitt en personkonflikt.")
print("A) individuelle samtaler   B) Plenum")
valg1 = lesvalg("Velg A eller B: ")
if valg1 == "A":
    print("Stemningen roer seg ...")
    print("-> Felles arbeidsmøte om kriterier.")
    poeng += 1

else:
    print("Møtet blir opphetet ...")
    print("-> Flere i teamet tar side.")
print()
print("Beslutning 2: Hamdi og Hallgeir")
print("Uenigheten om digitale folkemøter ulmer.")
print("A) Avklaringsmøte nå   B) Avventer")
valg2 = lesvalg("Velg A eller B: ")
if valg2 == "A":
    print("Uenigheten avklares tidlig ...")
    print("-> En kombinert løsning testes.")
    poeng += 1

else:
    print("Misnøyen vokser ...")
    print("-> Åpen kritikk på workshop.")
print()
print("Beslutning 3: Motivasjon og fremdrift")
print("Tre uker igjen til prototypen.")
if valg1 == "A" and valg2 == "A":
    print("A) Relasjonsbygging   B) Fullt fokus på leveranse")
    valg3 = lesvalg("Velg A eller B: ")
    if valg3 == "A":
        print("Tilliten bygges opp igjen ...")
        print("-> Bedre samarbeidsklima.")
        poeng += 1
    else:
        print("Prototypen går i rute, men det blir mer stress ...")
        print("-> Fare for utbrenthet.")
elif valg1 == "B" and valg2 == "B":
    print("A) Relasjonsbygging   B) Fullt fokus på leveranse")
    valg3 = lesvalg("Velg A eller B: ")
    if valg3 == "A":
        print("Tilliten bygges opp igjen ...")
        print("-> Bedre samarbeidsklima.")
        poeng += 1
    else:
        print("Prototypen går i rute, men det blir mer stress ...")
        print("-> Fare for utbrenthet.")
elif valg1 == "A" and valg2 == "B":
    print("A) Relasjonsbygging   B) Fullt fokus på leveranse")
    valg3 = lesvalg("Velg A eller B: ")
    if valg3 == "A":
        print("Tilliten bygges opp igjen ...")
        print("-> Bedre samarbeidsklima.")
        poeng += 1
    else:
        print("Prototypen går i rute, men det blir mer stress ...")
        print("-> Fare for utbrenthet.")
elif valg1 == "B" and valg2 == "A":
    print("A) Relasjonsbygging   B) Fullt fokus på leveranse")
    valg3 = lesvalg("Velg A eller B: ")
    if valg3 == "A":
        print("Tilliten bygges opp igjen ...")
        print("-> Bedre samarbeidsklima.")
        poeng += 1
    else:
        print("Prototypen går i rute, men det blir mer stress ...")
        print("-> Fare for utbrenthet.")

print()
print("Resultat: summen av tillitspoeng avgjør hvilken slutt teamet får.")
if poeng == 3:
    print("Utfall 1: 3 poeng")
    print("Tillit gjenopprettet -> teamet går inn i norming-fasen.")
elif poeng >= 1:
    print("Utfall 2: 1-2 poeng")
    print("Delvis løst, men relasjonene er sårbare.")
else:
    print("Utfall 3: 0 poeng")
    print("Teamet mister samholdet -> prosjektet forsinkes.")

print()
print(f"Din poengsum: {poeng} av 3")
print("Valgene dine:", valg1, valg2, valg3)
print()
print("Takk for at du spilte!")