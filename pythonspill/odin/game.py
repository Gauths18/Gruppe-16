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


print("A) individuelle samtaler   B) Plenum")
valg1 = lesvalg("Velg A eller B: ")
if valg1 == "A":
    print("Temperaturen dempes ...")
    poeng += 2
    print()
    print("Du setter opp to samtaler på tirsdag. Elias forklarer at han er")
    print("redd for at prosjektet sprenger budsjettet og får hull i")
    print("sikkerheten. Silje forteller at hun føler at ingen lytter til")
    print("brukerne. Begge har gode poenger, og begge er lettet over å")
    print("slippe å forsvare seg foran de andre.")
    print()
    print("Torsdag samler du dem. Sammen blir dere enige om kriterier for")
    print("teknologivalget: sikkerhet, kostnad, brukervennlighet og")
    print("fleksibilitet. Konflikten er ikke borte, men den handler nå om")
    print("sak og ikke om person.")
else:
    print("Åpen konflikt ...")

    print()
    print("Du tar opp saken i plenum på fredagsmøtet. Først går samtalen")
    print("rolig, men etter noen minutter hever Elias stemmen, og Silje")
    print("svarer skarpt. Marcia og Hamdi blander seg inn, og snart er")
    print("hele teamet delt i to leire.")
    print()
    print("Noa prøver å dempe stemningen, men uten hell. Møtet avsluttes")
    print("tidlig, og ingen er enige om noe. Du har mistet litt av rollen")
    print("som nøytral leder, og begge sider ser nå på deg for å se hvem")
    print("du holder med.")



print(f"Din poengsum: {poeng} av 4")
print("Valgene dine:", valg1, valg2, valg3)
print()
print("Takk for at du spilte!")