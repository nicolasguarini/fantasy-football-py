class Giocatore:
    def __init__(self, nome, cognome, prezzo, ruolo, forza):
        self.nome = nome
        self.cognome = cognome
        self.prezzo = prezzo
        self.ruolo = ruolo
        self.forza = forza
    
    def visualizza_giocatore(self):
        print("---\nNome: %s Cognome: %s \nRuolo: %s Prezzo: %d \nForza %d\n--\n" % (self.nome, self.cognome, self.ruolo, self.prezzo, self.forza))
        

class Ruoli:
    attaccante = 'attaccante'
    difensore = 'difensore'
    centrocampista = 'centrocampista'
    portiere = 'portiere'
