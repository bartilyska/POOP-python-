from Roslina import Roslina

class Trawa(Roslina):

    def __init__(self, polx, poly, swiat, sila=0, inicjatywa=0, oznaczenie='T', wiek=0, nazwa="Trawa", zyje=True,szansa=15):
        super().__init__(polx, poly, swiat, sila, inicjatywa, oznaczenie, wiek, nazwa, zyje)
        self._szansa_zasiania = szansa

    def wstawMlode(self, x, y, swiat):
        swiat.dodajOrganizm(Trawa(x, y, swiat))