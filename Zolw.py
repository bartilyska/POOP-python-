import random
from Zwierze import Zwierze

class Zolw(Zwierze):

    def __init__(self, polx, poly, swiat, sila=2, inicjatywa=1, oznaczenie='Z', wiek=0, nazwa="Zolw", zyje=True):
        super().__init__(polx, poly, swiat, sila, inicjatywa, oznaczenie, wiek, nazwa, zyje)
    def czyOdbilAtak(self, atakujacy):
        return atakujacy.getSila() < 5

    def akcja(self):
        ruch_x = [1, -1, 0, 0]
        ruch_y = [0, 0, -1, 1]
        wykonano = False
        rand = random.Random()
        while not wykonano and self._wiek > 0:
            losuj = rand.randint(0, 3)
            czyruch = rand.randint(0, 3)
            nowapoz_x = self._polozenie_x + ruch_x[losuj]
            nowapoz_y = self._polozenie_y + ruch_y[losuj]
            if czyruch < 3:
                #print(f"{self._nazwa} ({self._polozenie_x + 1}, {self._polozenie_y + 1}) nie ruszyl sie")
                break
            elif 0 <= nowapoz_x < self._swiat.getRozmiar_x() and 0 <= nowapoz_y < self._swiat.getRozmiar_y():
                przeciwnik = self._swiat.coStoi(nowapoz_x, nowapoz_y)

                if przeciwnik is None:  # Nic nie stoi tam
                    #print(f"{self._nazwa} rusza z ({self._polozenie_x + 1}, {self._polozenie_y + 1})")
                    self._swiat.usunOznaczenie(self._polozenie_x, self._polozenie_y)
                    self._polozenie_x = nowapoz_x
                    self._polozenie_y = nowapoz_y
                    #print(f"i idzie na ({nowapoz_x + 1}, {nowapoz_y + 1})")
                    self._swiat.ustawOznaczenie(self._polozenie_x, self._polozenie_y, self._nazwa)
                else:
                    if przeciwnik.getNazwa() == self._nazwa:  # Rozmnazanie
                        if przeciwnik.getWiek() != 0:
                            self.rozmnazanie()
                    else:  # Walka
                        self.kolizja(przeciwnik)
                wykonano = True
        self._wiek += 1

    def wstawMlode(self, x, y, swiat):
        swiat.dodajOrganizm(Zolw(x, y, swiat))