from utils import BudgetNonSufficienteError
from utils import FormazioneNonCreataError


class Squadra:
    def __init__(self, nome, budget):
        self.nome = nome
        self.budget = budget
        self.giocatori = []
        self.formazione = None

    def componi_formazione(self, convocati):
        self.formazione = Formazione(giocatori=convocati)

    def acquista_giocatore(self, giocatore):
        if giocatore.prezzo > self.budget:
            raise BudgetNonSufficienteError
        self.giocatori.append(giocatore)
        self.budget -= giocatore.prezzo

    def cedi_giocagtore(self, giocatore):
        self.giocatori.remove(giocatore)
        self.budget += giocatore.prezzo

    def visualizza_giocatori(self):
        for giocatore in self.giocatori:
            giocatore.visualizza_giocatore()

    def visualizza_formazione(self):
        if self.formazione is None:
            raise FormazioneNonCreataError
            
        for giocatore in self.formazione.giocatori:
            giocatore.visualizza_giocatore()


class Formazione:
    def __init__(self, giocatori):
        self.giocatori = giocatori

    def forza(self):
        somma_forza = 0

        for giocatore in self.giocatori:
            somma_forza += giocatore.forza
        forza_media = somma_forza / len(self.giocatori)

        return forza_media
