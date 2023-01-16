# Crée par Jonah Warshawsky
# Exercices de programmation en Python
import random


def getAbilityScore():
    d6s = [random.randint(1, 6) for i in range(4)]
    d6s.remove(min(d6s))
    return sum(d6s)


class NPC:
    def __init__(self):
        self.force = getAbilityScore()
        self.agilite = getAbilityScore()
        self.constitution = getAbilityScore()
        self.intelligence = getAbilityScore()
        self.sagesse = getAbilityScore()
        self.charisme = getAbilityScore()
        self.ac = random.randint(1, 12)
        self.pointsDeVie = random.randint(1, 20)
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
        d20 = random.randint(1, 20) + self.force
        if d20 >= npc.ac:
            npc.subir_dommage(self.force)

    def subir_dommage(self, dommage):
        self.pointsDeVie -= dommage


class Hero(NPC):
    def __init__(self):
        super().__init__()
        self.espece = "Humain"

    def attaquer(self, npc):
        d20 = random.randint(1, 20) + self.force
        if d20 >= npc.ac:
            npc.subir_dommage(random.randint(1, 6) + self.force)

    def subir_dommage(self, dommage):
        self.pointsDeVie -= dommage