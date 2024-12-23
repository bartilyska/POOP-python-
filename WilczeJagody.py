from Roslina import Roslina

class WilczeJagody(Roslina):

    def __init__(self, polx, poly, swiat, sila=9999, inicjatywa=0, oznaczenie='J', wiek=0, nazwa="WilczeJagody", zyje=True,szansa=15):
        super().__init__(polx, poly, swiat, sila, inicjatywa, oznaczenie, wiek, nazwa, zyje)
        self._szansa_zasiania = szansa
    def efektPoZjedzeniu(self, atakujacy):
        self._swiat.usunOznaczenie(self._polozenie_x,self._polozenie_y)
        self._swiat.usunOrganizm(self)

    def wstawMlode(self, x, y, swiat):
        swiat.dodajOrganizm(WilczeJagody(x, y, swiat))