import random
from Roslina import Roslina

class Mlecz(Roslina):

    def __init__(self, polx, poly, swiat, sila=0, inicjatywa=0, oznaczenie='M', wiek=0, nazwa="Mlecz", zyje=True,szansa=10):
        super().__init__(polx, poly, swiat, sila, inicjatywa, oznaczenie, wiek, nazwa, zyje)
        self._szansa_zasiania = szansa

    def akcja(self):
        for i in range(3):
            rand = random.Random()
            losuj = rand.randint(0, 99)
            if losuj < self._szansa_zasiania:
              ruch_x = [1, -1, 0, 0]
              ruch_y = [0, 0, -1, 1]
              sprkierunki = [0, 0, 0, 0]
              while self._wiek > 0:
                 los = rand.randint(0, 3)
                 nowapoz_x = self._polozenie_x + ruch_x[los]
                 nowapoz_y = self._polozenie_y + ruch_y[los]
                 if 0 <= nowapoz_x < self._swiat.getRozmiar_x() and 0 <= nowapoz_y < self._swiat.getRozmiar_y():
                        przeciwnik = self._swiat.coStoi(nowapoz_x, nowapoz_y)
                        if przeciwnik is None:  # Nic nie stoi tam
                            self.utworzLogRozsianie(nowapoz_x, nowapoz_y)
                            self.wstawMlode(nowapoz_x, nowapoz_y, self._swiat)
                            self._swiat.ustawOznaczenie(nowapoz_x, nowapoz_y, self._oznaczenie)
                            break
                        sprkierunki[los] = 1
                 sprkierunki[los] = 1
                 if all(sprkierunki):
                      # Nie ma miejsca, by się rozsiać
                     break
        self._wiek += 1

    def wstawMlode(self, x, y, swiat):
        swiat.dodajOrganizm(Mlecz(x, y, swiat))