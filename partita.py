import time
import random


class Partita:
    def __init__(self, squadra_1, squadra_2):
        self.squadra_1 = squadra_1
        self.squadra_2 = squadra_2
        self.punteggio = [0, 0]

    def gioca(self):
        forza_squadra_1 = self.squadra_1.formazione.forza()
        forza_squadra_2 = self.squadra_2.formazione.forza()

        totale_forze = forza_squadra_1 + forza_squadra_2
        percentuale_vittoria_squadra_1 = forza_squadra_1 * 100 / totale_forze

        tempo_di_gioco = 0

        while tempo_di_gioco < 30:
            numero_estratto = estrai_numero_casuale()

            if numero_estratto <= 100:
                if numero_estratto <= percentuale_vittoria_squadra_1:
                    self.punteggio[0] += 1
                    notifica_goal(self.squadra_1, self.punteggio)
                else:
                    self.punteggio[1] += 1
                    notifica_goal(self.squadra_2, self.punteggio)

            time.sleep(1)
            tempo_di_gioco += 1

        self.notifica_risultato()

    def notifica_risultato(self):
        if self.punteggio[0] > self.punteggio[1]:
            notifica_vittoria(vincitrice=self.squadra_1, punteggio=self.punteggio)
                              
        elif self.punteggio[0] == self.punteggio[1]:
            notifica_pareggio(self.punteggio)

        else:
            notifica_vittoria(vincitrice=self.squadra_2, punteggio=self.punteggio)
                              

def estrai_numero_casuale():
    return random.randint(1, 300)


def notifica_vittoria(vincitrice, punteggio):
    print("---\nLa squadra %s vince la partita!!\n--\nPunteggio: %d - %d\n" % (vincitrice.nome, punteggio[0], punteggio[1]))


def notifica_pareggio(punteggio):
    print("---\nPareggio!!\n----\nPunteggio: %d - %d\n" % (punteggio[0], punteggio[1]))


def notifica_goal(squadra_che_ha_segnato, punteggio):
    print("---\nLa squadra %s ha fatto gol!!!\nPunteggio: %d - %d\n" % (squadra_che_ha_segnato.nome, punteggio[0], punteggio[1]))
