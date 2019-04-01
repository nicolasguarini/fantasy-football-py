import os
from utils import (GiocatoreNonTrovatoError,
                   GiocatoriNonSufficientiError,
                   BudgetNonSufficienteError,
                   FormazioneNonCreataError)

from mercato import mercato
from squadra import Squadra
from partita import Partita
from anagrafica_giocatori import giocatori


def clear():
    os.system("clear")


def riempi_squadre(squadre):
    nome_nuova_squadra = "milan"
    budget_nuova_squadra = 350
    nuova_squadra = Squadra(nome_nuova_squadra, budget_nuova_squadra)
    nuova_squadra.giocatori = giocatori[:11]
    squadre.append(nuova_squadra)

    nome_nuova_squadra = "juventus"
    budget_nuova_squadra = 643
    nuova_squadra = Squadra(nome_nuova_squadra, budget_nuova_squadra)
    nuova_squadra.giocatori = giocatori[11:22]
    squadre.append(nuova_squadra)


def menu():
    squadre = []
    riempi_squadre(squadre)

    while True:
        clear()
        print("1 - Nuova squadra\n")
        print("2 - Gestione squadre\n")
        print("3 - Nuova partita\n")
        print("0 - Esci\n")
        scelta = int(input("Inserisci una scelta: "))

        if scelta == 1:
            nuova_squadra(squadre)
        elif scelta == 2:
            gestione_squadre(squadre)
        elif scelta == 3:
            nuova_partita(squadre)
            pass
        elif scelta == 0:
            return


def nuova_squadra(squadre):
    clear()
    nome_nuova_squadra = input("Inserisci il nome della squadra da creare: ")
    budget_nuova_squadra = 1500
    nuova_squadra = Squadra(nome_nuova_squadra, budget_nuova_squadra)
    squadre.append(nuova_squadra)


def gestione_squadre(squadre):
    clear()
    while True:
        clear()

        for contatore_squadre in range(0, len(squadre)):
            print('%d - %s \n' % (contatore_squadre+1, squadre[contatore_squadre].nome))
        print("0 - Indietro\n")

        indice_squadra = int(input("Inserisci la squadra da gestire: "))

        if indice_squadra == 0:
            return
        else:
            indice_squadra -= 1

        gestione_squadra(squadre, indice_squadra)


def nuova_partita(squadre):
    clear()
    cont = 0
    squadre_che_giocano = []

    while cont < 2:
        clear()
        for contatore_squadre in range(0, len(squadre)):
            print('%d - %s \n' % (contatore_squadre+1, squadre[contatore_squadre].nome))
        print("0 - Indietro\n")
        indice_squadra = int(input("Inserisci la squadra %s: " % (cont + 1)))

        if indice_squadra == 0:
            return
        else:
            indice_squadra -= 1

        if squadre[indice_squadra].formazione is None:
            print("La squadra selezionata non ha una formazione valida per giocare una partita!!")
            input("Premere un tasto per continuare...")
            continue

        squadre_che_giocano.append(squadre[indice_squadra])
        cont += 1

    partita = Partita(squadre_che_giocano[0], squadre_che_giocano[1])
    clear()
    partita.gioca()
    input("Premere un tasto per continuare...")


def gestione_squadra(squadre, indice_squadra):
    while True:
        clear()
        print("--- " + squadre[indice_squadra].nome + " ---\n")
        print("Budget disponibile: " + str(squadre[indice_squadra].budget) +"\n")
        print("1 - Acquista Giocatori\n")
        print("2 - Vendi Giocatori\n")
        print("3 - Visualizza Mercato\n")
        print("4 - Visualizza Giocatori della squadra\n")
        print("5 - Componi formazione\n")
        print("6 - Visualizza formazione\n")
        print("0 - Indietro\n")
        scelta = int(input("Inserisci l'opzione desiderata: "))
        
        if scelta == 1:
            try:
                acquista(squadre, indice_squadra)
            except GiocatoreNonTrovatoError:
                print("Giocatore non trovato")
                input("Premere un tasto per continuare...")

        elif scelta == 2:
            try:
                vendi(squadre, indice_squadra)
            except GiocatoreNonTrovatoError:
                print("Giocatore non trovato")
                input("Premere un tasto per continuare...")
        
        elif scelta == 3:
            visualzza_mercato()
            input("Premere un tasto per continuare...")

        elif scelta == 4:
            clear()
            squadre[indice_squadra].visualizza_giocatori()
            input("Premere un tasto per continuare...")

        elif scelta == 5:
            try:
                componi_formazione(squadre[indice_squadra])
            except GiocatoriNonSufficientiError:
                print("Non hai abbastanza giocatori!!!")
                input("Premere un tasto per continuare...")

        elif scelta == 6:
            clear()
            try:
                squadre[indice_squadra].visualizza_formazione()
            except FormazioneNonCreataError:
                print("Devi prima creare una formazione!!")
            input("Premere un tasto per continuare")

        elif scelta == 0:
            return


def componi_formazione(squadra):
    clear()
    minimo_giocatori = 11

    if len(squadra.giocatori) < minimo_giocatori:
        raise GiocatoriNonSufficientiError
    
    giocatori_temp = squadra.giocatori.copy()
    convocati = []

    if len(giocatori_temp) == minimo_giocatori:
        convocati = giocatori_temp.copy()
        squadra.componi_formazione(convocati)
        print("Formazione composta automaticamente")
        input("Premere un tasto per continuare...")
        return

    cont = 0
    while cont < minimo_giocatori:
        clear()
        print("--\nGiocatore %d\n--\n" % (cont + 1))
        for giocatore in giocatori_temp:
            giocatore.visualizza_giocatore()
        
        cognome_giocatore_da_vendere = input("Inserisci il cognome del giocatore: ")
        nome_giocatore_da_vendere = input("Inserisci il nome del giocatore: ")
        
        for giocatore in giocatori_temp: 
            if cognome_giocatore_da_vendere == giocatore.cognome:
                if nome_giocatore_da_vendere == giocatore.nome:
                    giocatori_temp.remove(giocatore)
                    convocati.append(giocatore)
                    cont += 1
                    break
    squadra.componi_formazione(convocati)


def acquista(squadre, indice_squadra):
    clear()
    trovato = False
    mercato.visualizza_svincolati()

    cognome_giocatore_da_acquistare = input("Inserisci il cognome del giocatore: ")
    nome_giocatore_da_acquistare = input("Inserisci il nome del giocatore: ")

    for svincolato in mercato.giocatori: 
        if cognome_giocatore_da_acquistare == svincolato.cognome:
            if nome_giocatore_da_acquistare == svincolato.nome:
                try:
                    squadre[indice_squadra].acquista_giocatore(svincolato)
                except BudgetNonSufficienteError:
                    print("Budget non sufficiente")
                    input("Premere un tasto per continuare...")
                    return
                mercato.giocatori.remove(svincolato)
                trovato = True
                break

    if not trovato:
        raise GiocatoreNonTrovatoError


def vendi(squadre, indice_squadra):
    clear()
    trovato = False
    if len(squadre[indice_squadra].giocatori) == 0:
        print("Acquista prima dei giocatori!!!")
        input("Premere un tasto per continuare...")
        return
    
    for giocatore in squadre[indice_squadra].giocatori:
        giocatore.visualizza_giocatore()
    
    cognome_giocatore_da_vendere = input("Inserisci il cognome del giocatore: ")
    nome_giocatore_da_vendere = input("Inserisci il nome del giocatore: ")

    for giocatore in squadre[indice_squadra].giocatori: 
        if cognome_giocatore_da_vendere == giocatore.cognome:
            if nome_giocatore_da_vendere == giocatore.nome:
                trovato = True
                squadre[indice_squadra].cedi_giocagtore(giocatore)
                mercato.giocatori.append(giocatore)
                break
    
    if not trovato:
        raise GiocatoreNonTrovatoError


def visualzza_mercato():
    clear()
    print("1 - Visualizza Attaccanti\n")
    print("2 - Visualizza Difensori\n")
    print("3 - Visualizza Centrocampisti\n")
    print("4 - Visualizza Portieri\n")
    print("5 - Visualizza Tutti\n")
    scelta = int(input("Inserire l'opzione desiderata: "))

    if scelta == 1:
        attaccanti = mercato.attaccanti()
        for attaccante in attaccanti:
            attaccante.visualizza_giocatore()
    elif scelta == 2:
        difensori = mercato.difensori()
        for difensore in difensori:
            difensore.visualizza_giocatore()
    elif scelta == 3:
        centrocampisti = mercato.centrocampisti()
        for centrocampista in centrocampisti:
            centrocampista.visualizza_giocatore()
    elif scelta == 4:
        portieri = mercato.portieri()
        for portiere in portieri:
            portiere.visualizza_giocatore()
    elif scelta == 5:
        mercato.visualizza_svincolati()


if __name__ == "__main__":
    menu()
