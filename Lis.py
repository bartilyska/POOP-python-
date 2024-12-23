import random
from Zwierze import Zwierze

class Lis(Zwierze):
    def __init__(self, polx, poly, swiat, sila=3, inicjatywa=7, oznaczenie='L', wiek=0, nazwa="Lis", zyje=True):
        super().__init__(polx, poly, swiat, sila, inicjatywa, oznaczenie, wiek, nazwa, zyje)

    def akcja(self):
        rand = random.Random()
        ruch_x = [1, -1, 0, 0]
        ruch_y = [0, 0, -1, 1]
        wykonano = False
        sprkierunki = [0, 0, 0, 0]
        while not wykonano and self._wiek > 0:
            losuj = rand.randint(0, 3)
            nowapoz_x = self._polozenie_x + ruch_x[losuj]
            nowapoz_y = self._polozenie_y + ruch_y[losuj]

            if 0 <= nowapoz_x < self._swiat.getRozmiar_x() and 0 <= nowapoz_y < self._swiat.getRozmiar_y():
                przeciwnik = self._swiat.coStoi(nowapoz_x, nowapoz_y)

                if przeciwnik is None:  # Nic nie stoi tam
                    self._swiat.usunOznaczenie(self._polozenie_x, self._polozenie_y)
                    self._polozenie_x = nowapoz_x
                    self._polozenie_y = nowapoz_y
                    self._swiat.ustawOznaczenie(self._polozenie_x, self._polozenie_y, self._nazwa)
                else:
                    if przeciwnik.getNazwa() == self._nazwa:  # Rozmnazanie
                        if przeciwnik.getWiek() != 0:
                            self.rozmnazanie()
                    elif self._sila >= przeciwnik.getSila():  # Walka
                        self.kolizja(przeciwnik)
                    else:
                        sprkierunki[losuj] = 1
                        if all(sprkierunki):
                            break
                        continue

                wykonano = True

            sprkierunki[losuj] = 1

        self._wiek += 1
    def wstawMlode(self, x, y, swiat):
        swiat.dodajOrganizm(Lis(x, y, swiat))