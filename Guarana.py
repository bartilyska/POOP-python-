from Roslina import Roslina

class Guarana(Roslina):

    def __init__(self, polx, poly, swiat, sila=0, inicjatywa=0, oznaczenie='G', wiek=0, nazwa="Guarana", zyje=True,szansa=15):
        super().__init__(polx, poly, swiat, sila, inicjatywa, oznaczenie, wiek, nazwa, zyje)
        self._szansa_zasiania = szansa

    def efektPoZjedzeniu(self,atakujacy):
        atakujacy.setSila(atakujacy.getSila()+3)

    def wstawMlode(self, x, y, swiat):
        swiat.dodajOrganizm(Guarana(x, y, swiat))