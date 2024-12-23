from Zwierze import Zwierze
class Czlowiek(Zwierze):

    def __init__(self, polx, poly, swiat, sila=5, inicjatywa=4, oznaczenie='C', wiek=0, nazwa="Czlowiek", zyje=True,ile_jeszcze=0):
        super().__init__(polx, poly, swiat, sila, inicjatywa, oznaczenie, wiek, nazwa, zyje)
        self.__ile_jeszcze_mocy=ile_jeszcze

    def akcja(self):
        kierunek = self._swiat.getKierunekCzlowieka()
        self.specjalnaUmiejetnosc()
        ruch_x, ruch_y = 0, 0
        if kierunek == "gora":
            ruch_x, ruch_y = 0, -1
        elif kierunek == "dol":
            ruch_x, ruch_y = 0, 1
        elif kierunek == "lewo":
            ruch_x, ruch_y = -1, 0
        elif kierunek == "prawo":
            ruch_x, ruch_y = 1, 0

        nowapoz_x = self._polozenie_x + ruch_x
        nowapoz_y = self._polozenie_y + ruch_y

        if (0 <= nowapoz_x < self._swiat.getRozmiar_x() and
                0 <= nowapoz_y < self._swiat.getRozmiar_y() and
                ruch_x != ruch_y):
            przeciwnik = self._swiat.coStoi(nowapoz_x, nowapoz_y)
            if przeciwnik is None:  # nic nie stoi tam (lub organizm trup)
                self._swiat.usunOznaczenie(self._polozenie_x, self._polozenie_y)
                self._polozenie_x = nowapoz_x
                self._polozenie_y = nowapoz_y
                self._swiat.ustawOznaczenie(self._polozenie_x, self._polozenie_y, self._oznaczenie)
            else:
                self.kolizja(przeciwnik)
        self._wiek += 1

    def getIleJeszczeMocy(self):
        return self.__ile_jeszcze_mocy

    def specjalnaUmiejetnosc(self):
        if self.__ile_jeszcze_mocy == 0 and self._swiat.getCooldownMoc() == 10:
            self._sila = 10
            self.__ile_jeszcze_mocy = 5
        elif self.__ile_jeszcze_mocy > 0:
            self._sila -= 1
            self.__ile_jeszcze_mocy -= 1

        if self._swiat.getCooldownMoc() > 0:
            self._swiat.setCooldownMoc(self._swiat.getCooldownMoc() - 1)

    def wstawMlode(self, x, y, swiat):
        swiat.dodajOrganizm(Czlowiek(x, y, swiat))