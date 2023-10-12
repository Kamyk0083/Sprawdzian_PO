import math


def czy_pierwsza(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def liczby_pierwsze_do_n(n):
    if n <= 1:
        return []
    liczby_pierwsze = []
    for i in range(2, n + 1):
        if czy_pierwsza(i):
            liczby_pierwsze.append(i)
    return liczby_pierwsze


if __name__ == "__main__":
    n = int(input("Podaj liczbę całkowitą: "))
    liczby_pierwsze = liczby_pierwsze_do_n(n)
    for liczba in liczby_pierwsze:
        print(liczba, end=", ")
