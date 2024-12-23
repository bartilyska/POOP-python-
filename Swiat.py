import random
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import font, scrolledtext
from Organizm import Organizm
from Wilk import Wilk
from Owca import Owca
from Lis import Lis
from Zolw import Zolw
from Antylopa import Antylopa
from Trawa import Trawa
from Mlecz import Mlecz
from Guarana import Guarana
from WilczeJagody import WilczeJagody
from BarszczSosnowskiego import BarszczSosnowskiego
from CyberOwca import CyberOwca
from Czlowiek import Czlowiek
from collections import namedtuple
class Swiat:
    def __init__(self, rozmiar_x, rozmiar_y):
        self.__rozmiar_x = rozmiar_x
        self.__rozmiar_y = rozmiar_y
        self.__plansza = [['.' for _ in range(rozmiar_x)] for _ in range(rozmiar_y)]
        self.__organizmy = []
        self.__logi = []
        self.__kierunek_czlowieka = ''
        self.__cooldown_mocy = 0

        #self.__organizmy.append(Owca(0, 4, self))
        #self.__organizmy.append(CyberOwca(0,0,self))
        #self.__organizmy.append(CyberOwca(0, 1, self))
        #self.__organizmy.append(WilczeJagody(3, 1, self))
        #self.__organizmy.append(BarszczSosnowskiego(5, 0, self))
        #self.__organizmy.append(BarszczSosnowskiego(0, 5, self))
        Pair = namedtuple('Pair', ['first', 'second'])
        rand = random.Random()
        pozycje = [Pair(i, j) for i in range(self.__rozmiar_y) for j in range(self.__rozmiar_x)]
        ileorg = self.__rozmiar_x * self.__rozmiar_y // 50
        indeks = rand.randint(0, len(pozycje) - 1)
        para = pozycje.pop(indeks)
        self.__organizmy.append(Czlowiek(para.second, para.first, self))
        wylosowane = []
        for i in range(ileorg):
            for j in range(11):
                indeks = rand.randint(0, len(pozycje) - 1)
                wylosowane.append(pozycje.pop(indeks))

            self.__organizmy.append(Antylopa(wylosowane[0].second, wylosowane[0].first, self))
            self.__organizmy.append(BarszczSosnowskiego(wylosowane[1].second, wylosowane[1].first, self))
            self.__organizmy.append(Guarana(wylosowane[2].second, wylosowane[2].first, self))
            self.__organizmy.append(Lis(wylosowane[3].second, wylosowane[3].first, self))
            self.__organizmy.append(Mlecz(wylosowane[4].second, wylosowane[4].first, self))
            self.__organizmy.append(Owca(wylosowane[5].second, wylosowane[5].first, self))
            self.__organizmy.append(Trawa(wylosowane[6].second, wylosowane[6].first, self))
            self.__organizmy.append(WilczeJagody(wylosowane[7].second, wylosowane[7].first, self))
            self.__organizmy.append(Wilk(wylosowane[8].second, wylosowane[8].first, self))
            self.__organizmy.append(Zolw(wylosowane[9].second, wylosowane[9].first, self))
            self.__organizmy.append(CyberOwca(wylosowane[10].second, wylosowane[10].first, self))

            wylosowane.clear()

        self.init_gui()

    def init_gui(self):
        self.__root = tk.Tk()
        self.__root.focus_force()
        self.__root.title("Bartosz Lyskanowski 198051")
        ROZMIARX, ROZMIARY = 1100, 780
        self.__root.geometry(f"{ROZMIARX}x{ROZMIARY}")
        self.wysrodkujEkran(1100,780)
        self.__mapa = tk.Frame(self.__root, bg='darkgray')
        self.__mapa.grid(row=0, column=0, sticky='nsew')

        self.__zdarzenia = tk.Frame(self.__root, bg='white')
        self.__zdarzenia.grid(row=0, column=1, sticky='nsew', padx=5)

        self.__logi_plansza = scrolledtext.ScrolledText(self.__zdarzenia, bg='black', fg='white', wrap=tk.WORD)
        self.__logi_plansza.config(font=font.Font(family="Sans Serif", size=10, weight='bold'))
        self.__logi_plansza.pack(expand=True, fill='both')

        self.__panel_na_sterowanie = tk.Frame(self.__root, bg='gray')
        self.__panel_na_sterowanie.grid(row=1, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=3,minsize=750)
        self.__root.grid_columnconfigure(1, weight=1)

        self.__pola = [[None for i in range(self.__rozmiar_x)] for j in range(self.__rozmiar_y)]
        for i in range(self.__rozmiar_y):
            for j in range(self.__rozmiar_x):
                guzik = tk.Button(self.__mapa, text='', bg='#3A271B', fg='darkblue',
                                   font=font.Font(family="Dialog", size=10, weight='bold'))
                guzik.grid(row=i, column=j, sticky='nsew')
                self.__pola[i][j]=guzik
                self.__mapa.grid_rowconfigure(i, weight=1)
                self.__mapa.grid_columnconfigure(j, weight=1)
                self.__pola[i][j].config(command=lambda i=i, j=j: self.dodajOrganizmPoKliku(j, i))
        self.__panel_na_sterowanie.grid_columnconfigure(0, weight=1)
        self.__panel_na_sterowanie.grid_columnconfigure(4, weight=1)
        self.__guziki_sterowania = []
        for i in range(3):
            button = tk.Button(self.__panel_na_sterowanie, font=font.Font(family="Dialog", size=13, weight='bold'),
                               bg='#6441A5', fg='cyan', width=12, height=2)
            self.__guziki_sterowania.append(button)
            button.grid(row=0, column=i+1, padx=5, pady=5)

        self.__guziki_sterowania[0].config(text="Zapisz", command=self.zapiszDoPliku)
        self.__guziki_sterowania[1].config(text="Wczytaj",command=self.wczytZPliku)
        self.__guziki_sterowania[2].config(text="Moc",command=self.guzikMocy)

        self.__root.bind("<KeyPress>", self.handleKeypress)
        self.OgarniajMainLoop()

    def OgarniajMainLoop(self):
        self.wykonajTure()
        self.aktualizujPlansze()
        self.aktualizujFrame()
        self.wypiszLogiIUsun()
        self.__root.focus_force()
        self.__root.mainloop()
    def wysrodkujEkran(self,szer, wys):
        screen_szer = self.__root.winfo_screenwidth()
        screen_wys = self.__root.winfo_screenheight()
        x = (screen_szer - szer) // 2
        y = (screen_wys - wys) // 2
        self.__root.geometry(f'{szer}x{wys}+{x}+{y-40}')
    def wykonajTure(self):
        self.__organizmy.sort(key=lambda org: (-org.getInicjatywa(), -org.getWiek()))
        for organizm in self.__organizmy:
            if organizm.getZyje():
                organizm.akcja()

        for organizm in reversed(self.__organizmy):
            if not organizm.getZyje():
                self.__organizmy.remove(organizm)

    def coStoi(self, x, y):
        if self.__plansza[y][x] == '.':
            return None
        for organizm in self.__organizmy:
            if (organizm.getPolozenie_y() == y and
                    organizm.getPolozenie_x() == x and
                    organizm.getZyje()):
                return organizm
        return None

    def dodajOrganizmPoKliku(self,x,y):
        przeciwnik = self.coStoi(x, y)
        if przeciwnik is None:
            okienko = tk.Tk()
            okienko.title("Dodaj Organizm")
            rozx,rozy=300,300
            okienko.geometry(f"300x300+1000+300")
            pokaz = tk.StringVar(okienko)
            pokaz.set("Wilk")
            wybor = tk.OptionMenu(okienko, pokaz,"Wilk", "Owca", "Lis", "Zolw", "Antylopa", "Trawa", "Mlecz", "Guarana", "WilczeJagody",
                       "BarszczSosnowskiego","CyberOwca")
            wybor.pack()

            def potwierdz():
                wybrana = pokaz.get()
                if wybrana == "Wilk":
                    org = Wilk(x, y, self)
                    self.__logi.append("Dodano Wilka")
                elif wybrana == "Owca":
                    org = Owca(x, y, self)
                    self.__logi.append("Dodano Owce")
                elif wybrana == "Lis":
                    org = Lis(x, y, self)
                    self.__logi.append("Dodano Lisa")
                elif wybrana == "Zolw":
                    org = Zolw(x, y, self)
                    self.__logi.append("Dodano Zolwia")
                elif wybrana == "Antylopa":
                    org = Antylopa(x, y, self)
                    self.__logi.append("Dodano Antylope")
                elif wybrana == "Trawa":
                    org = Trawa(x, y, self)
                    self.__logi.append("Dodano Trawe")
                elif wybrana == "Mlecz":
                    org = Mlecz(x, y, self)
                    self.__logi.append("Dodano Mlecz")
                elif wybrana == "Guarana":
                    org = Guarana(x, y, self)
                    self.__logi.append("Dodano Guarane")
                elif wybrana == "WilczeJagody":
                    org = WilczeJagody(x, y, self)
                    self.__logi.append("Dodano WilczeJagody")
                elif wybrana == "BarszczSosnowskiego":
                    org = BarszczSosnowskiego(x, y, self)
                    self.__logi.append("Dodano BarszczSosnowskiego")
                elif wybrana == "CyberOwca":
                    org = CyberOwca(x, y, self)
                    self.__logi.append("Dodano CyberOwce")

                self.dodajOrganizmNaPlansze(org)
                self.dodajOrganizm(org)
                self.dodajOrganizmNaWidocznaPlansze(org)
                okienko.destroy()

            potwiedzguzik = tk.Button(okienko, text="Potwierdz", command=potwierdz)
            potwiedzguzik.pack(pady=10)
            okienko.mainloop()
        else:
            return

    def dodajOrganizmNaPlansze(self, org):
        self.__plansza[org.getPolozenie_y()][org.getPolozenie_x()] = org.getOznaczenie()

    def aktualizujPlansze(self):
        for i in range(self.getRozmiar_y()):
             for j in range(self.getRozmiar_x()):
                self.__plansza[i][j] = '.'

        for organizm in self.__organizmy:
            self.dodajOrganizmNaPlansze(organizm)

    def dodajOrganizmNaWidocznaPlansze(self, org):
        y = org.getPolozenie_y()
        x = org.getPolozenie_x()
        self.__pola[y][x].config(text=org.getOznaczenie())
        if isinstance(org, Wilk):
            self.__pola[y][x].config(bg='lightgray')
        elif isinstance(org, Owca):
            self.__pola[y][x].config(bg='white')
        elif isinstance(org, Lis):
            self.__pola[y][x].config(bg='orange')
        elif isinstance(org, Zolw):
            self.__pola[y][x].config(bg='#006400')
        elif isinstance(org, Antylopa):
            self.__pola[y][x].config(bg='#D3B683')
        elif isinstance(org, Czlowiek):
            self.__pola[y][x].config(bg='#FFE5B4')
        elif isinstance(org, Trawa):
            self.__pola[y][x].config(bg='#90ee90')
        elif isinstance(org, Mlecz):
            self.__pola[y][x].config(bg='yellow')
        elif isinstance(org, Guarana):
            self.__pola[y][x].config(bg='red')
        elif isinstance(org, WilczeJagody):
            self.__pola[y][x].config(bg='black')
        elif isinstance(org, BarszczSosnowskiego):
            self.__pola[y][x].config(bg='#E1D9D1')
        elif isinstance(org,CyberOwca):
            self.__pola[y][x].config(bg='purple')

    def aktualizujFrame(self):
        for i in range(self.__rozmiar_y):
            for j in range(self.__rozmiar_x):
                if self.__plansza[i][j] == '.':
                    self.__pola[i][j].config(bg='#3A271B', text="")

        if self.getCooldownMoc() != 0:
            self.__guziki_sterowania[2].config(state='disabled')
        else:
            self.__guziki_sterowania[2].config(state='normal')

        for organizm in self.__organizmy:
            self.dodajOrganizmNaWidocznaPlansze(organizm)

    def wypiszLogiIUsun(self):
        self.__logi_plansza.delete('1.0', tk.END)
        for log in self.__logi:
            self.__logi_plansza.insert(tk.END, log + "\n")
        self.__logi.clear()

    def dodajOrganizm(self,org):
        self.__organizmy.append(org);
    def usunOrganizm(self,org):
        org.setZyje(False);
    def getRozmiar_x(self):
        return self.__rozmiar_x

    def setRozmiar_x(self, rozmiarx):
        self.__rozmiar_x = rozmiarx

    def getRozmiar_y(self):
        return self.__rozmiar_y

    def setRozmiar_y(self, rozmiary):
        self.__rozmiar_y = rozmiary
    def getKierunekCzlowieka(self):
        return self.__kierunek_czlowieka
    def getCooldownMoc(self):
        return self.__cooldown_mocy
    def setCooldownMoc(self,ile):
        self.__cooldown_mocy=ile
    def getOrganizmy(self):
        return self.__organizmy
    def usunOznaczenie(self, x, y):
        self.__plansza[y][x] = '.'

    def ustawOznaczenie(self, x, y, oznaczenie):
        self.__plansza[y][x] = oznaczenie
    def dodajLog(self,log):
        self.__logi.append(log)
    def rysujSwiat(self):
        print("Bartosz Lyskanowski s198051")
        for i in range(self.getRozmiar_y()):
            for j in range(self.getRozmiar_x()):
                print(self.__plansza[i][j], end='')
            print()

    def wypiszOrganizmy(self):
        for organizm in self.__organizmy:
            organizm.wypiszOrganizm()

    def handleKeypress(self, event):
        self.__kierunek_czlowieka = ""
        if event.keysym == 'Left':
            self.__kierunek_czlowieka = "lewo"
        elif event.keysym == 'Right':
            self.__kierunek_czlowieka = "prawo"
        elif event.keysym == 'Up':
            self.__kierunek_czlowieka = "gora"
        elif event.keysym == 'Down':
            self.__kierunek_czlowieka = "dol"

        if self.__kierunek_czlowieka:
            self.wykonajTure()
            # self.rysujSwiat()
            self.aktualizujFrame()
            self.wypiszLogiIUsun()
            #self.wypiszOrganizmy()
    def guzikMocy(self):
        if self.getCooldownMoc() == 0:
            self.__guziki_sterowania[2].config(state="disabled")
            self.setCooldownMoc(10)
    def zapiszDoPliku(self):
        nazwa = simpledialog.askstring("Input", "Podaj nazwe pliku: ")
        try:
            with open(nazwa, 'w') as plik:
                plik.write(f"{self.__rozmiar_x} {self.__rozmiar_y} {self.__cooldown_mocy}\n")
                for organizm in self.__organizmy:
                    if isinstance(organizm, Czlowiek):
                     plik.write(
                           f"{organizm.getNazwa()} {organizm.getPolozenie_x()} {organizm.getPolozenie_y()}"
                           f" {organizm.getWiek()} {organizm.getSila()}"
                           f" {organizm.getInicjatywa()} {organizm.getOznaczenie()} {organizm.getIleJeszczeMocy()}\n")
                    else:
                        plik.write(
                           f"{organizm.getNazwa()} {organizm.getPolozenie_x()} {organizm.getPolozenie_y()} {organizm.getWiek()} "
                           f"{organizm.getSila()} {organizm.getInicjatywa()} {organizm.getOznaczenie()}\n")
                plik.close()
                self.__logi.append("Zapisano plansze do pliku")
                self.wypiszLogiIUsun()
        except IOError as e:
            print(f"Blad przy zapisie: {e}")
    def wczytZPliku(self):
        nazwapliku = simpledialog.askstring("Input", "Podaj nazwe pliku do zapisu")
        try:
            with open(nazwapliku, 'r') as wczyt:
                self.__organizmy.clear()
                self.__plansza.clear()
                self.__logi.clear()
                self.__logi_plansza.delete('1.0', tk.END)
                linia1 = wczyt.readline().strip()
                rozbicie = linia1.split(" ")
                self.__rozmiar_x = int(rozbicie[0])
                self.__rozmiar_y = int(rozbicie[1])
                self.__cooldown_mocy = int(rozbicie[2])
                for i in range(self.__rozmiar_y):
                    self.__plansza.append(['.' for j in range(self.__rozmiar_x)])

                self.__mapa.destroy()
                self.__mapa = tk.Frame(self.__root, bg='darkgray')
                self.__mapa.grid(row=0, column=0, sticky='nsew')
                self.__pola = [[None for i in range(self.__rozmiar_x)] for j in range(self.__rozmiar_y)]
                for i in range(self.__rozmiar_y):
                    for j in range(self.__rozmiar_x):
                        guzik = tk.Button(self.__mapa, text='', bg='#3A271B', fg='darkblue',
                                          font=font.Font(family="Dialog", size=10, weight='bold'))
                        guzik.grid(row=i, column=j, sticky='nsew')
                        self.__pola[i][j] = guzik
                        self.__mapa.grid_rowconfigure(i, weight=1)
                        self.__mapa.grid_columnconfigure(j, weight=1)
                        self.__pola[i][j].config(command=lambda i=i, j=j: self.dodajOrganizmPoKliku(j, i))

                for linia in wczyt:
                    dane = linia.strip().split(" ")
                    nazwa = dane[0]
                    x = int(dane[1])
                    y = int(dane[2])
                    wiek = int(dane[3])
                    sila = int(dane[4])
                    inicjatywa = int(dane[5])
                    oznaczenie = dane[6]
                    if nazwa == "Czlowiek":
                        ile_jeszcze_mocy = int(dane[7])
                        self.__organizmy.append(
                            Czlowiek(x, y, self,sila, inicjatywa, oznaczenie, wiek, nazwa,  True, ile_jeszcze_mocy))
                    elif nazwa == "Wilk":
                        self.__organizmy.append(Wilk(x, y, self,sila, inicjatywa, oznaczenie, wiek, nazwa,  True))
                    elif nazwa == "Owca":
                        self.__organizmy.append(Owca(x, y,self, sila, inicjatywa, oznaczenie, wiek, nazwa,  True))
                    elif nazwa == "Zolw":
                        self.__organizmy.append(Zolw(x, y, self,sila, inicjatywa, oznaczenie, wiek, nazwa,  True))
                    elif nazwa == "Lis":
                        self.__organizmy.append(Lis(x, y, self,sila, inicjatywa, oznaczenie, wiek, nazwa,  True))
                    elif nazwa == "Antylopa":
                        self.__organizmy.append(Antylopa(x, y,  self,sila, inicjatywa, oznaczenie, wiek, nazwa, True))
                    elif nazwa == "Trawa":
                        self.__organizmy.append(Trawa(x, y, self, sila, inicjatywa, oznaczenie, wiek, nazwa, True))
                    elif nazwa == "Mlecz":
                        self.__organizmy.append(Mlecz(x, y, self,sila, inicjatywa, oznaczenie, wiek, nazwa,  True))
                    elif nazwa == "Guarana":
                        self.__organizmy.append(Guarana(x, y,self, sila, inicjatywa, oznaczenie, wiek, nazwa,  True))
                    elif nazwa == "WilczeJagody":
                        self.__organizmy.append(WilczeJagody(x, y,self, sila, inicjatywa, oznaczenie, wiek, nazwa,  True))
                    elif nazwa == "BarszczSosnowskiego":
                        self.__organizmy.append(
                            BarszczSosnowskiego(x, y,self, sila, inicjatywa, oznaczenie, wiek, nazwa,  True))
                    elif nazwa == "CyberOwca":
                        self.__organizmy.append(
                            CyberOwca(x,y,self,sila,inicjatywa,oznaczenie,wiek,nazwa,True))

            self.__logi.append("Wczytano z pliku")
            self.wypiszLogiIUsun()
            self.aktualizujPlansze()
            self.aktualizujFrame()
        except IOError as e:
            print(f"Cos nie tak z plikiem: {e}")
