import re

class BankovniUcet:
    """ Trida ukazuje simulaci bankovniho uctu """

    def __init__(self, cislo_uctu : str, mena : str ):
        """
        Konstruktor prijima cislo uctu a menu, ve ktere je vedeny.

        :param cislo_uctu: Cislo uctu i kod banky ve formatu 5-10 cislic / 4 cislice
        :param mena: Mena uctu vyjadrena jako tri pismena, napr. EUR
        """
        if not re.match(r"^[0-9]{5,10}/[0-9]{4}$",cislo_uctu):
            raise Exception('Cislo uctu neodpovida formatu zapisu 000000000/0000.')

        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')

        self._cislo_uctu = cislo_uctu
        self._mena = mena
        self._zustatek = 0

    def __str__(self):
        return str(self._cislo_uctu + ":"+str(self._zustatek)+self._mena)

    def __int__(self):
        return int(self._zustatek)
    
    def __float__(self):
        return float(self._zustatek)
    
muj_ucet = BankovniUcet("12341238/0100","CZK")
print(muj_ucet)


zustatek_alice = int(BankovniUcet("123414444/0110","EUR"))
print(zustatek_alice)