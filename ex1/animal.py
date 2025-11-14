class Animal:
    def parler(self):
        raise NotImplementedError("Cette méthode doit être redéfinie")

class Chien(Animal):
    def parler(self):
        return "Ouaf !"

class Chat(Animal):
    def parler(self):
        return "Miaou !"

class Vache(Animal):
    def parler(self):
        return "Meuh !"

class Robot:
    def parler(self):
        return "Bip bop."

def faire_parler(animal):
    print(animal.parler())

if __name__ == "__main__":
    animaux = [Chien(), Chat(), Chien(), Vache(), Robot()]
    for a in animaux:
        faire_parler(a)
