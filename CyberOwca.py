from Zwierze import Zwierze
class CyberOwca(Zwierze):

    def __init__(self, polx, poly, swiat, sila=11, inicjatywa=4, oznaczenie='Y', wiek=0, nazwa="CyberOwca", zyje=True):
        super().__init__(polx, poly, swiat, sila, inicjatywa, oznaczenie, wiek, nazwa, zyje)

    def akcja(self):
        from BarszczSosnowskiego import BarszczSosnowskiego
        czy_jest_barszcz = False
        poz_x_naj=-9999
        poz_y_naj=-9999
        min_odleglosc=9999
        if self._wiek>0: # dla wieku 0 i tak niech wykona sie normalna akcja (czyli tylko zwieksz wiek)
            for organizm in self._swiat.getOrganizmy():
                if isinstance(organizm,BarszczSosnowskiego):
                     czy_jest_barszcz=True
                     if abs(self._polozenie_x-organizm.getPolozenie_x())+abs(self._polozenie_y-organizm.getPolozenie_y())<min_odleglosc:
                        min_odleglosc=abs(self._polozenie_x-organizm.getPolozenie_x())+abs(self._polozenie_y-organizm.getPolozenie_y())
                        poz_y_naj=organizm.getPolozenie_y()
                        poz_x_naj=organizm.getPolozenie_x()
                
        if czy_jest_barszcz:
            ruch_x = [1, -1, 0, 0]
            ruch_y = [0, 0, -1, 1]
            wykonano = False
            while not wykonano and self._wiek > 0:
                nowapoz_x=-9999
                nowapoz_y=-9999
                for i in range(4):
                    poz_x = self._polozenie_x + ruch_x[i]
                    poz_y = self._polozenie_y + ruch_y[i]
                    if 0 <= poz_x < self._swiat.getRozmiar_x() and 0 <= poz_y < self._swiat.getRozmiar_y():
                        if abs(poz_x-poz_x_naj)+abs(poz_y-poz_y_naj)<=min_odleglosc:
                             min_odleglosc=abs(poz_x-poz_x_naj)+abs(poz_y-poz_y_naj)
                             nowapoz_y=poz_y
                             nowapoz_x=poz_x
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
        else:
            super().akcja()


    def kolizja(self, broniacy):
        from BarszczSosnowskiego import BarszczSosnowskiego
        if broniacy.czyOdbilAtak(self):
            self.utworzLogOdbicie(broniacy)
        elif broniacy.czyMozeUciec():
            broniacy.ucieczka(self)
        elif self._sila >= broniacy.getSila() or isinstance(broniacy,BarszczSosnowskiego):
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

    def wstawMlode(self, x, y, swiat):
        swiat.dodajOrganizm(CyberOwca(x, y, swiat))