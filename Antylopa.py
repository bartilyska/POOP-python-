import random
from Zwierze import Zwierze
class Antylopa(Zwierze):

    def __init__(self, polx, poly, swiat, sila=4, inicjatywa=4, oznaczenie='A', wiek=0, nazwa="Antylopa", zyje=True):
        super().__init__(polx, poly, swiat, sila, inicjatywa, oznaczenie, wiek, nazwa, zyje)

    def czyMozeUciec(self):
        rand = random.Random()
        ucieczka = rand.randint(0, 1)
        if ucieczka == 0:
            return False
        ruch_x = [1, -1, 0, 0]
        ruch_y = [0, 0, 1, -1]

        for i in range(4):
            nowapoz_x = self._polozenie_x + ruch_x[i]
            nowapoz_y = self._polozenie_y + ruch_y[i]
            if 0 <= nowapoz_x < self._swiat.getRozmiar_x() and 0 <= nowapoz_y < self._swiat.getRozmiar_y():
                if self._swiat.coStoi(nowapoz_x, nowapoz_y) is None:  # Nic nie stoi tam
                    return True
        return False

    def ucieczka(self, atakujacy):
        ruch_x = [1, -1, 0, 0]
        ruch_y = [0, 0, 1, -1]  # antylopa ucieka
        for i in range(4):
            nowapoz_x = self._polozenie_x + ruch_x[i]
            nowapoz_y = self._polozenie_y + ruch_y[i]
            if 0 <= nowapoz_x < self._swiat.getRozmiar_x() and 0 <= nowapoz_y < self._swiat.getRozmiar_y():
                if self._swiat.coStoi(nowapoz_x, nowapoz_y) is None:
                    self._swiat.usunOznaczenie(atakujacy.getPolozenie_x(), atakujacy.getPolozenie_y())
                    self._swiat.ustawOznaczenie(self._polozenie_x, self._polozenie_y,
                                               atakujacy.getOznaczenie())  # ruch atakującego i antylopy
                    atakujacy.setPolozenie_x(self._polozenie_x)
                    atakujacy.setPolozenie_y(self._polozenie_y)
                    self._polozenie_x = nowapoz_x
                    self._polozenie_y = nowapoz_y
                    self._swiat.ustawOznaczenie(nowapoz_x, nowapoz_y, self._oznaczenie)
                    self.utworzLogUcieczka(atakujacy)
                    #print( f"{self.nazwa} uciekła na ({self.polozenie_x + 1}, {self.polozenie_y + 1}) "
                    #       f"przed {atakujacy.getNazwa()} z ({atakujacy.getPolozenie_x() + 1}, {atakujacy.getPolozenie_y() + 1})")
                    break

    def akcja(self):
        ruch_x = [2, -2, 0, 0, 1, 1, -1, -1]
        ruch_y = [0, 0, 2, -2, 1, -1, 1, -1]
        wykonano = False
        while not wykonano and self._wiek > 0:
            rand = random.Random()
            losuj = rand.randint(0, 7)
            nowapoz_x = self._polozenie_x + ruch_x[losuj]
            nowapoz_y = self._polozenie_y + ruch_y[losuj]
            if 0 <= nowapoz_x < self._swiat.getRozmiar_x() and 0 <= nowapoz_y < self._swiat.getRozmiar_y():
                przeciwnik = self._swiat.coStoi(nowapoz_x, nowapoz_y)
                if przeciwnik is None:  # Nic nie stoi tam
                    self._swiat.usunOznaczenie(self._polozenie_x, self._polozenie_y)
                    self._polozenie_x = nowapoz_x
                    self._polozenie_y = nowapoz_y
                    self._swiat.ustawOznaczenie(self._polozenie_x, self._polozenie_y, self._oznaczenie)
                else:
                    if przeciwnik.getNazwa() == self._nazwa:  # Rozmnażanie
                        if przeciwnik.getWiek() != 0:
                            self.rozmnazanie()
                    else:  # Walka
                        self.kolizja(przeciwnik)
                wykonano = True
        self._wiek += 1

    def wstawMlode(self, x, y, swiat):
        swiat.dodajOrganizm(Antylopa(x, y, swiat))