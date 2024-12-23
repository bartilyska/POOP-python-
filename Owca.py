from Zwierze import Zwierze
class Owca(Zwierze):

    def __init__(self, polx, poly, swiat, sila=4, inicjatywa=4, oznaczenie='O', wiek=0, nazwa="Owca", zyje=True):
        super().__init__(polx, poly, swiat, sila, inicjatywa, oznaczenie, wiek, nazwa, zyje)

    def wstawMlode(self, x, y, swiat):
        swiat.dodajOrganizm(Owca(x, y, swiat))