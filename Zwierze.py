import random
from Organizm import Organizm

class Zwierze(Organizm):
    def __init__(self, polx, poly,swiat, sila, inicjatywa, ozn, wiek, nazwa, zyje):
        super().__init__(polx, poly,swiat, sila, inicjatywa, ozn, wiek, nazwa, zyje)

    def akcja(self):
        rand = random.Random()
        ruch_x = [1, -1, 0, 0]
        ruch_y = [0, 0, -1, 1]
        wykonano = False
        while not wykonano and self._wiek > 0:
            losuj = rand.randint(0, 3)
            nowapoz_x = self._polozenie_x + ruch_x[losuj]
            nowapoz_y = self._polozenie_y + ruch_y[losuj]
            if 0 <= nowapoz_x < self._swiat.getRozmiar_x() and 0 <= nowapoz_y < self._swiat.getRozmiar_y():
                przeciwnik = self._swiat.coStoi(nowapoz_x, nowapoz_y)
                if przeciwnik is None:
                    self._swiat.usunOznaczenie(self._polozenie_x, self._polozenie_y)
                    self._polozenie_x = nowapoz_x
                    self._polozenie_y = nowapoz_y
                    self._swiat.ustawOznaczenie(self._polozenie_x, self._polozenie_y, self._oznaczenie)
                else:
                    if przeciwnik.getNazwa() == self._nazwa:
                        if przeciwnik.getWiek() != 0:
                            self.rozmnazanie()
                    else:
                        self.kolizja(przeciwnik)
                wykonano = True
        self._wiek += 1

    def kolizja(self, broniacy):
        if broniacy.czyOdbilAtak(self):
            self.utworzLogOdbicie(broniacy)
        elif broniacy.czyMozeUciec():
            broniacy.ucieczka(self)
        elif self._sila >= broniacy.getSila():
            self.utworzLogWalkaWygrana(broniacy)
            broniacy.efektPoZjedzeniu(self)
            self._swiat.usunOznaczenie(self._polozenie_x, self._polozenie_y)
            self._polozenie_x = broniacy.getPolozenie_x()
            self._polozenie_y = broniacy.getPolozenie_y()
            self._swiat.ustawOznaczenie(self._polozenie_x, self._polozenie_y, self._oznaczenie)
            self._swiat.usunOrganizm(broniacy)
        else:
            self.utworzLogWalkaPrzegrana(broniacy)
            broniacy.efektPoZjedzeniu(self)
            self._swiat.usunOznaczenie(self._polozenie_x, self._polozenie_y)
            self._swiat.usunOrganizm(self)

    def rozmnazanie(self):
        kierunekx = [1, -1, 0, 0, 1, -1, -1, 1]
        kieruneky = [0, 0, 1, -1, -1, 1, -1, 1]
        czy_rozmnozono = False
        for i in range(8):
            dziecko_x = self._polozenie_x + kierunekx[i]
            dziecko_y = self._polozenie_y + kieruneky[i]
            if (0 <= dziecko_x < self._swiat.getRozmiar_x() and
                    0 <= dziecko_y < self._swiat.getRozmiar_y() and
                    self._swiat.coStoi(dziecko_x, dziecko_y) is None):
                self.wstawMlode(dziecko_x, dziecko_y, self._swiat)
                self._swiat.ustawOznaczenie(dziecko_x, dziecko_y, self._oznaczenie)
                czy_rozmnozono = True
                self.utworzLogRozmnozenie()
                break

    def utworzLogOdbicie(self, broniacy):
        log = (f"{broniacy.getNazwa()} ({broniacy.getPolozenie_x() + 1}, {broniacy.getPolozenie_y() + 1}) "
               f"odbija atak {self._nazwa} ({self._polozenie_x + 1}, {self._polozenie_y + 1})")
        self._swiat.dodajLog(log)

    def utworzLogWalkaWygrana(self, broniacy):
        log = (f"{self._nazwa} ({self._polozenie_x + 1}, {self._polozenie_y + 1}) atakuje {broniacy.getNazwa()} "
               f"({broniacy.getPolozenie_x() + 1}, {broniacy.getPolozenie_y() + 1}) i wygrywa")
        self._swiat.dodajLog(log)

    def utworzLogWalkaPrzegrana(self, broniacy):
        log = (f"{self._nazwa} ({self._polozenie_x + 1}, {self._polozenie_y + 1}) atakuje {broniacy.getNazwa()} "
               f"({broniacy.getPolozenie_x() + 1}, {broniacy.getPolozenie_y() + 1}) i od niego ginie")
        self._swiat.dodajLog(log)

    def utworzLogRozmnozenie(self):
        log = f"{self._nazwa} ({self._polozenie_x + 1}, {self._polozenie_y + 1}) rozmnozyl sie "
        self._swiat.dodajLog(log)

    def utworzLogUcieczka(self, atakujacy):
        log = (f"{self._nazwa} uciekla na ({self._polozenie_x + 1}, {self._polozenie_y + 1}) przed "
               f"{atakujacy.getNazwa()} z ({atakujacy.getPolozenie_x() + 1}, {atakujacy.getPolozenie_y() + 1})")
        self._swiat.dodajLog(log)

