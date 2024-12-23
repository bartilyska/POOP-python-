import random
from Roslina import Roslina
from Zwierze import Zwierze
from CyberOwca import CyberOwca
class BarszczSosnowskiego(Roslina):

    def __init__(self, polx, poly, swiat, sila=9999, inicjatywa=0, oznaczenie='B', wiek=0, nazwa="BarszczSosnowskiego", zyje=True):
        super().__init__(polx, poly, swiat, sila, inicjatywa, oznaczenie, wiek, nazwa, zyje)
        self._szansa_zasiania = 15

    def akcja(self):
        if self._wiek > 0: #nie atakuj od razu po dodaniu na plansze
            ruch_x = [1, -1, 0, 0]
            ruch_y = [0, 0, -1, 1]
            for i in range(4):
                nowapoz_x = self._polozenie_x + ruch_x[i]
                nowapoz_y = self._polozenie_y + ruch_y[i]
                if 0 <= nowapoz_x < self._swiat.getRozmiar_x() and 0 <= nowapoz_y < self._swiat.getRozmiar_y():
                    przeciwnik = self._swiat.coStoi(nowapoz_x, nowapoz_y)
                    if isinstance(przeciwnik, Zwierze) and not isinstance(przeciwnik,CyberOwca): # i nie cyberowca
                        self.utworzLogAtak(przeciwnik)
                        self._swiat.usunOznaczenie(nowapoz_x, nowapoz_y)
                        self._swiat.usunOrganizm(przeciwnik)

        if random.randint(0, 99) < self._szansa_zasiania:
            ruch_x = [1, -1, 0, 0]
            ruch_y = [0, 0, -1, 1]
            sprkierunki = [0, 0, 0, 0]
            while self._wiek > 0:
                los = random.randint(0, 3)
                nowapoz_x = self._polozenie_x + ruch_x[los]
                nowapoz_y = self._polozenie_y + ruch_y[los]
                if 0 <= nowapoz_x < self._swiat.getRozmiar_x() and 0 <= nowapoz_y < self._swiat.getRozmiar_y():
                    przeciwnik = self._swiat.coStoi(nowapoz_x, nowapoz_y)
                    if przeciwnik is None:
                        self.utworzLogRozsianie(nowapoz_x, nowapoz_y)
                        self.wstawMlode(nowapoz_x, nowapoz_y, self._swiat)
                        self._swiat.ustawOznaczenie(nowapoz_x, nowapoz_y, self._oznaczenie)
                        break
                    sprkierunki[los] = 1

                sprkierunki[los] = 1
                if all(sprkierunki):
                    break
        self._wiek += 1

    def efektPoZjedzeniu(self, atakujacy):
        #tu dodac ifa ze atakujacy to nie CyberOwca
        if not isinstance(atakujacy,CyberOwca):
            self._swiat.usunOznaczenie(self._polozenie_x,self._polozenie_y)
            self._swiat.usunOrganizm(self)

    def wstawMlode(self, x, y, swiat):
        swiat.dodajOrganizm(BarszczSosnowskiego(x, y, swiat))