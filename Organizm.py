from abc import ABC, abstractmethod

class Organizm(ABC):
    def __init__(self, polx, poly, swiat, sila, inicjatywa, ozn, wiek, nazwa,zyje):
        self._polozenie_x = polx
        self._polozenie_y = poly
        self._wiek = wiek
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._oznaczenie = ozn
        self._nazwa = nazwa
        self._swiat = swiat
        self._zyje = zyje


    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, broniacy):
        pass

    def czyOdbilAtak(self, atakujacy):
        return False

    def czyMozeUciec(self):
        return False

    def efektPoZjedzeniu(self, atakujacy):
        pass

    def rozmnazanie(self):
        pass

    def ucieczka(self, atakujacy):
        pass

    @abstractmethod
    def wstawMlode(self, x, y, swiat):
        pass
    def getPolozenie_x(self):
        return self._polozenie_x

    def getPolozenie_y(self):
        return self._polozenie_y

    def setPolozenie_x(self, pozx):
        self._polozenie_x = pozx

    def setPolozenie_y(self, pozy):
        self._polozenie_y = pozy

    def getWiek(self):
        return self._wiek

    def getNazwa(self):
        return self._nazwa

    def getInicjatywa(self):
        return self._inicjatywa

    def getSila(self):
        return self._sila

    def setSila(self, nowasila):
        self._sila = nowasila

    def getZyje(self):
        return self._zyje

    def setZyje(self, zycie):
        self._zyje = zycie

    def getOznaczenie(self):
        return self._oznaczenie

    def wypiszOrganizm(self):
        print(f"{self._nazwa} {self._polozenie_x + 1} {self._polozenie_y + 1} "
              f"{self._wiek} {self._sila} {self._inicjatywa} {self._oznaczenie} {self._zyje}")
