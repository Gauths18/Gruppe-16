# Interaktiv historie om prosjektleder Erling (IS-118, gruppeinnlevering 2)
# Spilleren tar tre valg. Hvert valg som bygger tillit gir 1 poeng.
# Poengene avgjør hvilken av tre slutter spilleren får.

import time

poeng = 0
valg1 = ""
valg2 = ""
valg3 = ""


# Spør om A eller B, og spør på nytt hvis svaret er ugyldig
def lesvalg(spørsmål):
    svar = input(spørsmål).strip().upper()
    while svar not in ("A", "B"):
        print("Ugyldig valg. Vennligst velg A eller B.")
        svar = input(spørsmål).strip().upper()
    return svar


# Venter til spilleren trykker Enter, slik at historien kommer litt om gangen
def pause():
    input("\n(Trykk Enter for å fortsette ...)")


# Skriver tekst bokstav for bokstav, som om noen skriver den i sanntid
def skriv(tekst):
    for bokstav in tekst:
        print(bokstav, end="", flush=True)
        time.sleep(0.03)
    print()


# Introduksjon
print("Mandag morgen. Kaffen er kald, og du har 47 uleste e-poster.")
print("Du er Erling, prosjektleder for kommunens nye digitale medborgerportal.")
print("Det har gått seks uker, og teamet er i storming-fasen.")
print("Silje og Elias er uenige om design og teknologi, og det har blitt personlig mellom dem.")
print("Hamdi og Hallgeir er uenige om hvordan innbyggerne skal delta i digitale folkemøter, og det begynner å eskalere.")
print("Den første prototypen skal være klar om tre uker. Ingen press.")
pause()


# Beslutningspunkt 1: konflikten mellom Silje og Elias
print()
print("Teammøtet blir høylytt. Silje og Elias krangler, og noen har begynt å velge side.")
print("Hvordan håndterer du konflikten mellom Silje og Elias?")
print("A) Ta det opp i et åpent plenumsmøte")
print("B) Snakke med dem hver for seg")
valg1 = lesvalg("Velg A eller B: ")

if valg1 == "A":
    print("Møtet blir opphetet, og flere i teamet tar side.")
    print("Noen begynner å sitte på hver sin side av bordet i lunsjen.")
else:
    print("Stemningen roer seg, og Silje og Elias blir enige om å samarbeide om teknologivalget.")
    print("Elias tilbyr til og med Silje en kaffe. Fremgang!")
    poeng += 1

print("Samtidig merker du at frustrasjonen mellom Hamdi og Hallgeir øker.")
pause()


# Beslutningspunkt 2: uenigheten mellom Hamdi og Hallgeir
print()
print("En e-posttråd om digitale folkemøter har nå 23 svar. Tonen blir stadig kortere.")
print("Hamdi vil bruke kommunens egen plattform. Hallgeir vil ha et åpent system.")
print("Plutselig svarer Hallgeir: «Greit. 1v1. Vinneren bestemmer.»")
print("Hvordan håndterer du uenigheten mellom Hamdi og Hallgeir?")
print("A) Kalle inn til et avklaringsmøte")
print("B) La dem finne ut av det selv i ringen")
valg2 = lesvalg("Velg A eller B: ")

if valg2 == "A":
    print("Du avlyser 1v1-en og booker et møterom i stedet.")
    print("Uenigheten blir avklart, og de blir enige om å teste en felles løsning.")
    poeng += 1
else:
    print("DING DING DING! Hamdi og Hallgeir løser det i ringen.")
    print("I det ene hjørnet: Hamdi, med kommunens plattform på skjorta.")
    print("I det andre hjørnet: Hallgeir, med «ÅPENT SYSTEM» skrevet på pannebåndet.")
    print("Etter tre runder vinner Hallgeir på poeng. Hamdi sier ingenting resten av uka.")
    print("Uenigheten er ikke løst, og misnøyen vokser i det stille.")

print("Fristen nærmer seg, og flere i teamet begynner å bli slitne.")
pause()


# Beslutningspunkt 3: motivasjonen i teamet
print()
print("Det er to uker igjen. Kaffemaskinen har gått tom tre ganger denne uka. Uff.")
print("Hvordan skal du bevare motivasjonen i teamet?")
print("A) Sette av tid til relasjonsbygging")
print("B) Kreve fullt fokus på leveransen")
valg3 = lesvalg("Velg A eller B: ")

if valg3 == "A":
    print("Dere tar en lunsj sammen. Teamet får hentet seg inn, og tilliten bygges opp igjen.")
    poeng += 1
else:
    print("Arbeidet går raskere, men teamet blir stresset og slitent.")
    print("Noen har begynt å sukke høyt hver gang kalenderen varsler om et nytt møte.")

pause()


# Avslutning: utfallet avgjøres av poengsummen
print()
skriv("Prototypefristen er her ...")

if poeng == 3:
    skriv("Teamet gjenoppretter tilliten og går videre til norming-fasen.")
    print("Prototypen leveres i tide, og bystyret er fornøyd.")
    print("Din tittel: KONFLIKTKNUSEREN")
elif poeng >= 1:
    print("Konflikten løses delvis, men relasjonene er fortsatt sårbare.")
    print("Prototypen blir ferdig, men det er fortsatt spenninger i teamet.")
    print("Din tittel: BRANNSLUKKEREN")
else:
    print("Prosjektet mister samhold og blir forsinket.")
    print("Teamet er delt i to leirer, og bystyret ringer for å spørre hva som skjer.")
    print("De har også hørt rykter om en boksekamp. «Hvem vant, forresten?»")
    print("Din tittel: STORMKASTET")

print()
print(f"Din poengsum: {poeng} av 3")
print("Valgene dine:", valg1, valg2, valg3)