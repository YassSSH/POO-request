class Item:
    def __init__(self, name : str, prix: float, quantite=0):
        assert prix >= 0, "error"
        assert quantite >= 0 , "error"

        print("OEOEOEE INIT")

        self.name = name
        self.prix = prix
        self.quantite = quantite
    
    def calcul(self):
        return self.prix * self.quantite

item1 = Item("POPO", 800, 6)
print(f"{item1.name} vaut {item1.calcul()}")
