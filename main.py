# Crée par Jonah Warshawsky
# Exercices de programmation orientee objet en Python
from random import randint


def getAbilityScore():
    d6s = [randint(1, 6) for i in range(4)]
    d6s.remove(min(d6s)) # On enleve le plus petit des 4
    return sum(d6s)


class NPC:
    def __init__(self):
        self.force = getAbilityScore()
        self.agilite = getAbilityScore()
        self.constitution = getAbilityScore()
        self.intelligence = getAbilityScore()
        self.sagesse = getAbilityScore()
        self.charisme = getAbilityScore()
        self.ac = randint(1, 12)
        self.pointsDeVie = randint(1, 20)
        self.race = str
        self.espece = str
        self.profession = str
        self.nom = str

    def afficher_caracteristiques(self):
        print(f'''
Je suis un {self.profession} {self.espece} {self.profession} nommé {self.nom}.        
        J'ai {self.pointsDeVie} points de vie, {self.force} en force, {self.agilite} en agilité, {self.constitution} en constitution, {self.intelligence} en intelligence, {self.sagesse} en sagesse, {self.charisme} en charisme et une classe d'armure {self.ac}.
''')


class Kobold(NPC):
    def __init__(self):
        super().__init__()
        self.espece = "Kobold"

    def attaquer(self, npc):
        d20 = randint(1, 20) + self.force
        if d20 >= npc.ac:
            npc.subir_dommage(self.force)

    def subir_dommage(self, dommage):
        self.pointsDeVie -= dommage


class Hero(NPC):
    def __init__(self):
        super().__init__()
        self.espece = "Humain"

    @staticmethod
    def attaquer(npc):
        d20 = randint(1, 20)
        if d20 == 20:  # attaque critique
            npc.subir_dommage(randint(1, 8))
        elif d20 != 1 and d20 >= npc.ac:  # attaque normale
            npc.subir_dommage(randint(1, 6))
        # attaque ratee - on fait rien

    def subir_dommage(self, dommage):
        self.pointsDeVie -= dommage
