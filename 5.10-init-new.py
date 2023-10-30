import re;
class Zbozi:
    def __new__(cls, nazev, cena):
        regex = '^(\s*)$'
        pattern = re.compile(regex);


        try:
            if cena < 0:
                return None
        except Exception:
            return None

        if pattern.search(nazev) != None:
            return None

        instance = super().__new__(cls)
        
        return instance

    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

a = Zbozi("Rohlik", 5)
b = Zbozi("Hackers item", -10)
c = Zbozi("",10)
d = Zbozi("Mliko","Jedna")

print(a)
print(b)
print(c)
print(d)