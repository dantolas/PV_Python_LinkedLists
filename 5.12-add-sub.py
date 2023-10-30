import re

class PenezniHotovost:
    """
    Trida reprezentuje penezni hotovost v urcite mene
    """

    def __init__(self, castka: float, mena: str):
        """
        Pri vytvoreni tridy se musi specifikovat castka a mena, nebo se pouzije defaultnich 0 EUR

        :param castka: Jakekoli realne cislo, muze byt i zaporne
        :param mena: Mena vyjadrena jako tripismeny kod
        :return: Objekt penezni hotovosti
        """
        if not re.match(r"^[A-Z]{3}$", mena):
            raise Exception('Mena neodpovida formatu zapisu tri velkych pismen.')

        self._mena = mena
        self._castka = castka

    def __str__(self):
        """
        Vrati castku a menu jako string
        :return: <castka> <mena>
        """
        return str(self._castka)+" "+self._mena

    def __add__(self, other):
        """
        Pretizeni operatoru + ktere vytvori novy objekt jako vysledek operace scitnai
        :param other: Lze scitat cisla typy int, float nebo jiny objekt penezni hotovosti ve stejne mene
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace scitani
        """
        if(isinstance(other, float) or isinstance(other, int)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other
            return vysledek

        if(isinstance(other, PenezniHotovost) and other._mena == self._mena):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka + other._castka
            return vysledek

        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")
    
    def __sub__(self, other):
        """
        Pretizeni operatoru - ktere vytvori novy objekt jako vysledek operace odcitani
        :param other: Lze odcitat cisla typy int, float nebo jiny objekt penezni hotovosti ve stejne mene
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace scitani
        """
        if(isinstance(other, float) or isinstance(other, int)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka - other
            return vysledek

        if(isinstance(other, PenezniHotovost) and other._mena == self._mena):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka - other._castka
            return vysledek

        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")

    def __mul__(self, other):
        """
        Pretizeni operatoru - ktere vytvori novy objekt jako vysledek operace nasobeni
        :param other: Lze nasobit cisla typy int, float nebo jiny objekt penezni hotovosti ve stejne mene
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace nasobeni
        """
        if(isinstance(other, float) or isinstance(other, int)):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka * other
            return vysledek

        if(isinstance(other, PenezniHotovost) and other._mena == self._mena):
            vysledek = PenezniHotovost(0, self._mena)
            vysledek._castka = self._castka * other._castka
            return vysledek

        raise Exception("Penezni hotovost lze scitat pouze s int,float a hotovosti ve stejne mene")

    def __pow__(self, power, modulo=None):
        """
        Pretizeni operatoru - ktere vytvori novy objekt jako vysledek operace umocnovani
        :param other: Lze umocnit cisla pouze prirozenym cislem int 
        :return: Vraci novy objekt, ktery ma nastavenou menu podle pubodni instance a castku jako vysledek operace umocnovani
        """
        if isinstance(power, int):

            if (power == 0):
                return PenezniHotovost(1,self._mena)

            if(power > 0 ):
                
                zustatek = self._castka
                for i in range(power):
                    zustatek = zustatek*zustatek

                return PenezniHotovost(zustatek,self._mena) 
            
            zustatek = self._castka
            for i in range(power):
                    zustatek = zustatek*zustatek
            
            return PenezniHotovost(1 / zustatek, self._mena)



        raise Exception("Penezni hotovost lze umocnovat pouze celymi cisly Z")
    
    def __truediv__(self, other,):
        """
        Pretizeni operatoru - ktere vytvori novy objekt jako vysledek operace deleni s realnym vysledkem
        :param other: Lze delit pouze realnymi cisly, nebo jinou instanci PenezniHotovost
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace 
        """
        if isinstance(other, int) or isinstance(other,float):

            return PenezniHotovost(self._castka / other,self._mena)
        
        if isinstance(other,PenezniHotovost) and other._mena == self._mena:

            return PenezniHotovost(self._castka / other._castka, self._castka)

        raise Exception("Penezni hotovost lze delit pouze realnymi cisly a jinimy instancemi PenezniHotovost se stejnou menou")

    def __floordiv__(self, other,):
        """
        Pretizeni operatoru - ktere vytvori novy objekt jako vysledek operace deleni s celociselnym vysledkem
        :param other: Lze delit pouze realnymi cisly, nebo jinou instanci PenezniHotovost
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace 
        """
        if isinstance(other, int) or isinstance(other,float):

            return PenezniHotovost(self._castka // other,self._mena)
        
        if isinstance(other,PenezniHotovost) and other._mena == self._mena:

            return PenezniHotovost(self._castka // other._castka, self._castka)

        raise Exception("Penezni hotovost lze delit pouze realnymi cisly a jinimy instancemi PenezniHotovost se stejnou menou")

    def __mod__(self, other,):
        """
        Pretizeni operatoru - ktere vytvori novy objekt jako vysledek operace modulo
        :param other: Lze modulovat pouze realnymi cisly, nebo jinou instanci PenezniHotovost
        :return: Vraci novy objekt, ktery ma nastavenou menu podle puvodnich objektu a zustatek jako vysledek operace modulo 
        """
        if isinstance(other, int) or isinstance(other,float):

            return PenezniHotovost(self._castka % other,self._mena)
        
        if isinstance(other,PenezniHotovost) and other._mena == self._mena:

            return PenezniHotovost(self._castka % other._castka, self._castka)

        raise Exception("Penezni hotovost lze delit pouze realnymi cisly a jinimy instancemi PenezniHotovost se stejnou menou")


    
sto_korun = PenezniHotovost(100, "CZK")
dve_sta_korun = sto_korun + 100

stoKorun = dve_sta_korun - sto_korun

tisicKorun = stoKorun * 10

desetKorun = 10

print(sto_korun)
print(dve_sta_korun)
print(stoKorun)
print(tisicKorun)
print(desetKorun**2)
print(desetKorun**0)
print(desetKorun**-2)

print(stoKorun / 12)
print(stoKorun // 12)
print(stoKorun % 12)