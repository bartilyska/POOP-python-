import random
from Organizm import Organizm

class Roslina(Organizm):

    def __init__(self, polx, poly,swiat, sila, inicjatywa, ozn, wiek, nazwa, zyje):
        super().__init__(polx, poly,swiat, sila, inicjatywa, ozn, wiek, nazwa, zyje)

    def akcja(self):
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

    def kolizja(self,org):
        pass

    def utworzLogRozsianie(self, nowapoz_x, nowapoz_y):
        log = (f"{self._nazwa} rozsiewa sie z ({self._polozenie_x + 1}, {self._polozenie_y + 1})"
               f" na ({nowapoz_x + 1}, {nowapoz_y + 1})")
        self._swiat.dodajLog(log)

    def utworzLogAtak(self, przeciwnik):
        log = (f"{self._nazwa} ({self._polozenie_x + 1}, {self._polozenie_y + 1}) zabija"
               f" {przeciwnik.getNazwa()} ({przeciwnik.getPolozenie_x() + 1}, {przeciwnik.getPolozenie_y() + 1})")
        self._swiat.dodajLog(log)
