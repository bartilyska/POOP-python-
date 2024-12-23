import tkinter as tk
from tkinter import simpledialog, messagebox
from Swiat import Swiat

def main():
    rozmiar_x, rozmiar_y = 0, 0

    while rozmiar_x <= 7 or rozmiar_y <= 7:
        rozmiar_x = simpledialog.askinteger("Input", "Podaj rozmiar x>7:")
        rozmiar_y = simpledialog.askinteger("Input", "Podaj rozmiar y>7:")
        if rozmiar_x is None or rozmiar_y is None:
            return
        if rozmiar_x <= 7 or rozmiar_y <= 7:
            messagebox.showinfo("Jeszcze raz", "Podaj liczby wieksze niz 7")

    #rozmiar_x, rozmiar_y=15,15
    swiat=Swiat(rozmiar_x,rozmiar_y)


if __name__ == "__main__":
    main()
