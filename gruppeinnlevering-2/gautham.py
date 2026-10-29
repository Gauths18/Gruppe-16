# IS-118 Gruppeoppgave 2
# Interaktiv historie om prosjektleder Erling
# Individuell løsning: Gautham

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


print("Det har gått seks uker siden prosjektet startet.")
print("Teamet utvikler en digital medborgerportal for kommunen.")
print("Uenigheter har ført teamet inn i storming-fasen.")
print("Du er Erling, prosjektleder, og må ta tre viktige beslutninger.")

print()
print("Beslutning 1: Konflikten mellom Silje og Elias")
print("Silje ønsker en innovativ og brukervennlig løsning, mens Elias")
print("prioriterer teknisk sikkerhet og kostnadskontroll.")
print("Uenigheten har utviklet seg fra en sakskonflikt til en personkonflikt.")
print("Hvordan bør Erling håndtere konflikten?")
print("A) Gjennomføre individuelle samtaler for å forstå begge parter.")
print("B) Ta opp konflikten i plenum for å skape åpenhet i teamet.")
valg1 = lesvalg("Velg A eller B: ")
if valg1 == "A":
    print("Erling gjennomfører individuelle samtaler med Silje og Elias.")
    print("Begge får mulighet til å uttrykke sine bekymringer uten å bli avbrutt.")
    print("Dette reduserer spenningen og bidrar til økt gjensidig forståelse.")
    print("Erling arrangerer deretter et felles møte for å finne en løsning begge kan akseptere.")
    poeng += 1

else:
    print("Erling samler Silje og Elias til et felles møte.")
    print("Diskusjonen blir opphetet, og begge forsvarer sine synspunkter.")
    print("Flere teammedlemmer tar side, og konflikten eskalerer.")

print()
print("Beslutning 2: Uenigheten mellom Hamdi og Hallgeir")
print("Hamdi ønsker å bruke kommunens eksisterende plattform for digitale folkemøter.")
print("Hallgeir ønsker en mer åpen løsning med rom for spontane innspill.")
print("Uenigheten er foreløpig lavmælt, men frustrasjonen vokser.")
print("Hvordan bør Erling håndtere situasjonen?")
print("A) Arrangere et avklaringsmøte før konflikten eskalerer.")
print("B) Avvente og la partene forsøke å finne en løsning selv.")
valg2 = lesvalg("Velg A eller B: ")
if valg2 == "A":
    print("Erling arrangerer et avklaringsmøte mellom Hamdi og Hallgeir.")
    print("Begge får presentere sine ønsker for de digitale folkemøtene.")
    print("De blir enige om å teste en kombinert løsning.")
    poeng += 1

else:
    print("Erling velger å avvente og håper konflikten løser seg selv.")
    print("Misnøyen mellom Hamdi og Hallgeir fortsetter å vokse.")
    print("Under neste workshop utvikler uenigheten seg til åpen kritikk.")

print()
print("Beslutning 3: Motivasjon og fremdrift")
print("Det er bare tre uker igjen til den første prototypen skal leveres.")
print("Konfliktene har påvirket kommunikasjonen og motivasjonen i teamet.")
print("Erling må balansere behovet for samarbeid med prosjektets tidsfrist.")
print("Hvordan bør Erling prioritere den siste fasen før milepælen?")
print("A) Prioritere relasjonsbygging for å gjenopprette tilliten i teamet.")
print("B) Prioritere fremdrift og leveranser for å overholde tidsfristen.")
valg3 = lesvalg("Velg A eller B: ")

if valg1 == "A" and valg2 == "A":
    print("Begge konfliktene er dempet. Samarbeidet fungerer bedre.")
elif valg1 == "B" and valg2 == "B":
    print("Begge konfliktene har eskalert. Teamet er splittet.")
else:
    print("En konflikt er håndtert, men samarbeidet er fortsatt sårbart.")

print("A) Relasjonsbygging   B) Fullt fokus på leveranse")
valg3 = lesvalg("Velg A eller B: ")

if valg3 == "A":
    print("Erling setter av tid til relasjonsbygging og samarbeid.")
    print("Teammedlemmene får bedre forståelse for hverandres perspektiver.")
    print("Tilliten styrkes, men arbeidet med prototypen tar noe lengre tid.")
    poeng += 1
else:
    print("Erling velger å prioritere arbeidet med prototypen.")
    print("Teamet arbeider effektivt for å overholde tidsfristen.")
    print("Prototypen leveres i tide, men stress og uløste konflikter svekker samarbeidet.")


print()
print("=== RESULTAT: PROSJEKTETS FREMTID ===")
print("Erling har tatt sine tre beslutninger.")
print("Valgene har fått konsekvenser for teamets samarbeid og fremdrift.")
print()

if poeng == 3:
    print("Utfall 1: Teamet beveger seg inn i norming-fasen.")
    print("Gjennom god konflikthåndtering har Erling gjenopprettet tilliten i teamet.")
    print("Silje, Elias, Hamdi og Hallgeir samarbeider nå bedre mot felles mål.")
    print("Kommunikasjonen er forbedret, og prosjektet har gode forutsetninger for å lykkes.")

elif poeng >= 1:
    print("Utfall 2: Konfliktene er delvis løst.")
    print("Erling har klart å dempe enkelte uenigheter, men utfordringer gjenstår.")
    print("Samarbeidet fungerer bedre på noen områder, mens relasjonene fortsatt er sårbare.")
    print("Prosjektet fortsetter, men teamet må arbeide videre med tillit og kommunikasjon.")

else:
    print("Utfall 3: Prosjektet mister fremdrift og samhold.")
    print("Konfliktene har eskalert, og flere teammedlemmer har mistet motivasjonen.")
    print("Manglende samarbeid og svekket kommunikasjon fører til forsinkelser.")
    print("Erling må nå iverksette tiltak for å hindre at prosjektet mislykkes.")

print()
print("=== OPPSUMMERING AV DINE VALG ===")
print(f"Din poengsum: {poeng} av 3")
print(f"Beslutning 1: {valg1}")
print(f"Beslutning 2: {valg2}")
print(f"Beslutning 3: {valg3}")
print()
print("Takk for at du spilte!")
