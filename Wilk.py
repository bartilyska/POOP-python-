from Zwierze import Zwierze
class Wilk(Zwierze):

    def __init__(self, polx, poly, swiat, sila=9, inicjatywa=5, oznaczenie='W', wiek=0, nazwa="Wilk", zyje=True):
        super().__init__(polx, poly, swiat, sila, inicjatywa, oznaczenie, wiek, nazwa, zyje)

    def wstawMlode(self, x, y, swiat):
        swiat.dodajOrganizm(Wilk(x, y, swiat))
