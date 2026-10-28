
# omeer.py - Gruppeinnlevering 2, IS-118
# Interaktiv historie: Erling må lede teamet gjennom storming-fasen.
# Spilleren tar tre valg. Tillitsbyggende valg gir 1 poeng.
# Summen av poengene (0-3) avgjør hvilket av tre utfall historien ender i.

# --- Variabler som lagrer valgene og poengene underveis ---
poeng = 0     # tillitspoeng, starter på 0
valg1 = ""    # valget i beslutning 1
valg2 = ""    # valget i beslutning 2
valg3 = ""    # valget i beslutning 3


# --- Introduksjon ---
poeng = 0
valg1="" 
valg2="" 
valg3="" 

def les_valg():
    svar = input("Velg A eller B: ").strip().upper()
    while svar != "A" and svar !="B":
        print("Ugyldig valg. Skriv A eller B.")
        svar = input("Velg A eller B: ").strip().upper()
        return svar

# --- Beslutning 1: konflikten mellom Silje og Elias ---
print("==== Erling og stormen ====")
print("Det har gått seks uker siden prosjektet med kommunens nye")
print("medborgerportal startet. Stemningen er spent, og første")
print("prototypen skal være klar om tre uker. Du er Erling, prosjektleder.")
print()
print("Silje og Elias er uenige om teknologi og design, og konflikten")
print("har blitt personlig. Begge har fått støttespillere i teamet.")
print("Hva gjør du?")
print("A) Tar konflikten opp i plenum på neste teammøte")
print("B)Tar individuelle samtaler med hver av dem først")
valg1 = les_valg()


if valg1 == "A":
    print("Møtet blir opphetet. Elias hever stemmen, Silje svarer skarpt,")
    print("og flere i teamet tar side. Teamet er delt i to leire.")
else:
    print("I samtalene får begge lufte frustrasjonen uten publikum.")
    print("Etterpå lager silje og Elias felles kriterier for teknologivalget.")
    poeng = poeng + 1 

    print("Samtidig merker du at frustrasjonen mellom Hamdi og Hallgeir vokser.")
print()

# --- Beslutning 2: uenigheten mellom Hamdi og Hallgeir ---

if valg1 == "A":
    print("Etter plenumsmøtet har Hallgeir tatt side med Elias.")

print("Hamdi vil bruke kommunens plattform for digitale folkemøter,")
print("mens Hallgeir vil ha et åpent system for innspill fra innbyggerne.")
print("Hva gjør du?")
print("A) Kaller dem inn til et avklaringsmøte")
print("B) Venter og håper at de løser det selv")
valg2 = les_valg()

if valg2 == "A":
    print("De blir enige om å teste en kombinert løsning i prototypen:")
    print("kommunens plattform, men med en åpen funksjon for innspill.")
    poeng = poeng + 1  
else:
    print("På en workshop kritiserer Hallgeir Hamdi åpent foran alle.")
    print("Energien i teamet faller.")

print("Fristen nærmer seg, og flere i teamet begynner å bli slitne.")
print()

# --- Beslutning 3: motivasjon og framdrift ---
print("Det er tre uker igjen til prototypen skal leveres. Hva gjør du?")
print("A) Setter av en halv dag til en felles workshop og sosialt samvær")
print("B) Strammer inn og krever full innsats mot leveransen")
valg3 = les_valg()

if valg3 == "A":
    print("Teamet går gjennom prototypen sammen og avslutter med middag.")
    print("Folk senker skuldrene, og flere tør å si ifra om problemer.")
    poeng = poeng + 1  
else:
    print("Alle jobber hardt, men uenighetene blir skjøvet under teppet.")
    print("Stresset øker, og færre sier ifra når noe ikke fungerer.")

print()

# --- Utfall: poengsummen avgjør slutten
print("=== Slutt ===")
if poeng == 3:
    print("Utfall 1: Teamet går videre til norming.")
    print("Konfliktene er håndtert, tilliten er gjenopprettet,")
    print("og prototypen leveres på tid.")
elif poeng >= 1:
    print("Utfall 2: Konfliktene er delvis løst.")
    print("Prototypen leveres, men samarbeidet er sårbart,")
    print("og Erling må følge opp de uløste konfliktene.")
else:
    print("Utfall 3: Teamet mister samholdet.")
    print("Teamet er delt, ingen tør å si ifra,")
    print("og prototypen blir forsinket.")

print()
print("Dine valg:", valg1, valg2, valg3)
print("Tillitspoeng:", poeng, "av 3")

