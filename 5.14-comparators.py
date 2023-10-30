import re
class Zbozi:
    """ Trida zbozi pro ukazu prikladu relacnich operatoru"""

    def __init__(self, nazev: str, vaha: float):
        """
        Pri vytvoreni se nastavuje nazev zbozi a jeho vaha
        :param nazev: Nazev musi byt znaky v rozsahu 1 az 200 znaku
        :param vaha: Vaha musi byt kladne a nenulove cislo
        """
        if not re.match(r"^[\D ]{1,200}$", nazev):
            raise Exception('Nazev musi byt v rozsahu 1 az 200 znaku')
        if vaha <= 0:
            raise Exception('Vaha nesmi byt zapojna')

        self._nazev = nazev
        self._vaha = vaha

    def __lt__(self, other):
        """
        Metoda zjistuje jestli je zbozi mensi nez druhe zbozi. Porovnava se pouze vaha.
        :param other: Trida pro porovnani, musi to byt instance Zbozi
        :return: True pokud je self mensi nez other
        """
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._vaha < other._vaha

    def __gt__(self, other):
        """
        Metoda zjistuje jestli je zbozi vetsi nez druhe zbozi. Porovnava se pouze vaha.
        :param other: Trida pro porovnani, musi to byt instance Zbozi
        :return: True pokud je self vetsi nez other
        """
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._vaha > other._vaha

    def __eq__(self, other):
        """
        Metoda zjistuje jestli je zbozi stejne jako druhe zbozi. Porovnava se pouze vaha.
        :param other: Trida pro porovnani, musi to byt instance Zbozi
        :return: True pokud je self stejne jako other
        """
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._vaha == other._vaha

    def __le__(self, other):
        """
        Metoda zjistuje jestli je zbozi mensi nebo rovne jako druhe zbozi. Porovnava se pouze vaha.
        :param other: Trida pro porovnani, musi to byt instance Zbozi
        :return: True pokud je self mensi nebo stejne jako other
        """
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._vaha <= other._vaha

    def __ge__(self, other):
        """
        Metoda zjistuje jestli je zbozi vetsi nebo rovne jako druhe zbozi. Porovnava se pouze vaha.
        :param other: Trida pro porovnani, musi to byt instance Zbozi
        :return: True pokud je self vetsi nebo rovne jako other
        """
        if (not isinstance(other, Zbozi)):
            raise Exception('Porovnavat lze jen zbozi mezi sebou')

        return self._vaha >= other._vaha

    def __hash__(self):
        return hash(self._nazev)*hash(self._vaha);

    def __eq__(self,other):
        if not isinstance(other,Zbozi): return False

        return (hash(self) == hash(other))

    def __str__(self):
        return str(self._nazev + " : "+self._vaha) 



    
kilo_brambor = Zbozi("Bramobra", 1)
krabice_mleka = Zbozi("Mleko", 1.029)
if(kilo_brambor < krabice_mleka):
    print("Svet je jeste v poradku")

voda = Zbozi("Voda",1)
cola = Zbozi("Cola",1.5)
voda2 = Zbozi("Voda",1)

print("Voda: 1")
print("Cola: 1.5")

print("cola == voda "+str(cola == voda))
print("cola > voda "+str(cola > voda))
print("cola < voda "+str(cola < voda))
print("cola <= voda "+str(cola <= voda))
print("cola >= voda "+str(cola >= voda))

zbozi1 = Zbozi("Mrkev", 1)
print(hash(voda))
print(hash(voda2))
x = set()
x.add(voda)
x.add(voda2)
x.add(cola)

print(x)
print(voda == voda2)