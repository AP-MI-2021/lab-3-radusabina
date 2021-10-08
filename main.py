def citire_lista():
    l = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]=")))
    return l


def get_all_even(l):
    """
    Determina daca toate numerele sunt pare.

    :param l: lista de nr intregi
    :return: True, daca toate nr. din l sunt pare, respectiv False in caz contrar
    """
    for x in l:
        if x % 2 != 0:
            return False
    return True


def test_get_all_even():
    assert get_all_even([]) is True
    assert get_all_even([1, 2, 3]) is False
    assert get_all_even([2, 4, 18]) is True


def get_longest_all_even(l):
    """
    Determina cea mai lunga subsecventa de numere pare dintr-o lista data.

    :param l: lista de nr intregi
    :return: cea mai lunga subsecventa de numere pare din l
    """
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if get_all_even(l[i: j + 1]) and len(l[i: j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i: j + 1]
    return subsecventa_max


def test_get_longest_all_even():
    assert get_longest_all_even([]) == []
    assert get_longest_all_even([2, 3, 5]) == [2]
    assert get_longest_all_even([12, 20, 13, 14]) == [12, 20]


def get_prime_digits(l):
    """
    Determina daca numerele sunt formate din cifre prime.

    :param l: lista de nr intregi
    :return: True, daca cifrele numerelor din lista sunt prime; False, in caz contrar
    """
    for x in l:
        while x != 0:
            cifra = x % 10
            if cifra == 1 or cifra == 4 or cifra == 6 or cifra == 8 or cifra == 9:
                return False
            x = x // 10
    return True


def test_get_prime_digits():
    assert get_prime_digits([13]) is False
    assert get_prime_digits([66, 527, 72, 888]) is False
    assert get_prime_digits([35, 577, 3333]) is True


def get_longest_prime_digits(l):
    """
    Determina cea mai lunga subsecventa din l care are numerele formate di  cifre prime

    :param l: lista de numere intregi
    :return: cea mai lunga subsecventa din l care are numerele formate di  cifre prime
    """
    subsecventa_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if get_prime_digits(l[i: j + 1]) and len(l[i: j + 1]) > len(subsecventa_max):
                subsecventa_max = l[i: j + 1]
    return subsecventa_max


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([13, 27, 32, 55, 44]) == [27, 32, 55]
    assert get_longest_prime_digits([44, 68, 999, 1024]) == []
    assert get_longest_prime_digits([233, 752, 7532]) == [233, 752, 7532]


def test_all():
    test_get_longest_all_even()
    test_get_all_even()
    test_get_prime_digits()
    test_get_longest_prime_digits()


def main():
    # interfata de tip consola aici
    test_all()
    l = []
    while True:
        print("1. Citire lista")
        print("2. Determină cea mai lungă subsecvență care are toate numerele sunt pare")
        print("3. Determina cea mai lunga subsecventa care are toate numerele formate din cifre prime")
        print("4. Iesire")
        optiune = int(input("Introduceti optiunea: "))
        if optiune == 1:
            l = citire_lista()
        elif optiune == 2:
            print(get_longest_all_even(l))
        elif optiune == 3:
            print(get_longest_prime_digits(l))
        elif optiune == 4:
            break
        else:
            print("Optiune gresita. Reincercati.")


if __name__ == "__main__":
    main()
