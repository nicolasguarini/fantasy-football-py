from giocatore import Ruoli
from anagrafica_giocatori import giocatori


class Mercato:
    def __init__(self): 
        self.giocatori = giocatori

    def attaccanti(self):
        attaccanti = []

        for giocatore in self.giocatori:
            if giocatore.ruolo == Ruoli.attaccante:
                attaccanti.append(giocatore)

        return attaccanti

    def centrocampisti(self):
        centrocampisti = []

        for giocatore in self.giocatori:
            if giocatore.ruolo == Ruoli.centrocampista:
                centrocampisti.append(giocatore)

        return centrocampisti

    def difensori(self):
        difensori = []

        for giocatore in self.giocatori:
            if giocatore.ruolo == Ruoli.difensore:
                difensori.append(giocatore)

        return difensori

    def portieri(self):
        portieri = []

        for giocatore in self.giocatori:
            if giocatore.ruolo == Ruoli.portiere:
                portieri.append(giocatore)

        return portieri

    def inserisci_giocatore(self, giocatore):
        self.giocatori.append(giocatore)

    def rimuovi_giocatore(self, giocatore):
        self.giocatori.remove(giocatore)

    def visualizza_svincolati(self):
        for svincolato in self.giocatori:
            svincolato.visualizza_giocatore()


mercato = Mercato()

