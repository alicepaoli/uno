#definzioni classi del progetto
# importazione di librerie esterne
from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime
import random

class Partita:
    def _init_(self, data:datetime, ora:datetime, numero_partita):
        self.data = data
        self.ora = ora
        self.numero_partita = numero_partita

    def inizializza_partita(self):
        print(f"Partita {self.numero_partita} inizializzata il {self.data} alle {self.ora}.")



class Giocatore:
    def _init_(self, nome, cognome, sesso, eta):
        self.punteggio= 0
        self.nome = nome
        self.cognome = cognome
        self.sesso = sesso
        self.eta = eta
        self.mossa_numero = 0

    def passa_turno(self):
        print(f"Il giocatore {self.nome}{self.cognome} passa il turno")

    def pesca_carta(self, mazzo):
        carta=mazzo.pesca_carta()
        print(f"Il giocatore {self.nome} {self.cognome} pesca la carta {carta}")

    def gioca_carta(self, carta):
        print(f"Il giocatore {self.nome}{self.cognome} gioca la carta {carta}")

class Mossa:
    def init(self, numero_mossa):
        self.numero_mossa = numero_mossa


class Mazzo:
    def crea_mazzo(self):
        # Implementazione per estrarre una carta dal mazzo
        pass
    ...

def mischia_mazzo(self):
    random.shuffle(self.carte)



