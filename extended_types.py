# Liczby zmiennioprzecinkowe w python sa zaimplementowane jako double w C.
# // - Operator dzielenia bez reszty

# [..] - listy skladane / listy
# (...) - korktki / generatory
# {...} - zbiory / slowniki


#indeksowanie:
# [:] - od 0 do n(gdzie n jest pominjany) [0:len(tab)]
# [n:] - od n do konca
# [n:m] - od n do m (m jest pomijany)
# [n:m:k] - od n do m z krokiem k
# [:-1] - wszystkie rlementy z wyjatkiem ostatniego
# [1:3] - elementy od 1 do 3 (3 jest pomijany)
# s[-1] = s[len(s) - 1] - ostatni element
# s[1:] - wszystkie elementy od 1 do konca

# sorted - zwraca klucze w posortowanej kolejnosci

# operator precedence 

# dodowanie obiektow np. 3 + 3.1 zawsze idzie w gore, czyli do obiektu, ktory jest bardziej szcezgolowy

# w python nie mozna tworzyc zmiennych, ktore nie maja w sobie obiektow - niezainicjalizowanych. Dopiero stworzenie obiektu powoduje zainicvajlziwaonie zmiennej.

# a ** 2 = a * a - potegowanie

# Pytrhon posiada metody wbudowane np. pow(2,4) - potegowanie, ale mozna tez uzyc operatora **. Mozna tez zaimprotowac math do teog, zeby wywolac math.pow()...

# zwykle typy liczbowe w python jak int i float sa po prostu tworzone albo za pomoca inicjalziacji(liczba stala albo z kropka) lub. w przypadku dzielenia przez liczbe zmiennoprzecinkowa.
# te bardziej zlozozone trzeba deklarowac: 

# Decimal - stala precyzja (np. zmiennoprzeciwknowa) - lepszacustomizacja
# import decimal

# mozna nadac kontkest tylko dal danego scopu:
# with decimal.localcontext() as ctx:
#     ctx.prec = 2  # Ustawia precyzję na 2
#     a = decimal.Decimal('1.2345')

#Fraction
# from fractions import Fraction
# to licznik i mianownik - ulamek. np Fraction(1,3) - tworzy ułamek 1/3. Fraction(1, 2) + Fraction(1, 3) - dodaje ułamki i zwraca wynik jako ułamek.

# set - nieuporzadtkowany zbior elementow, niemutowalny. Pozwala na wykonywanie na nim operacji an zbiorach
# set('abcdef') - tworzy zbior z liter a, b, c, d, e, f
# set([1, 2, 3]) - tworzy zbior z liczb

# a = set('abcdef')
# b = set('defgh')
# c = a | b  # suma zbiorów
# d = a & b  # część wspólna zbiorów
# e = a - b  # różnica zbiorów
# nadzbior # f = a > b  # a jest nadzbiorem b
# Zbiory sa niemutowalne w takim sensie, ze elementy, ktore tam sa nie moga byc zmieniane, ale mozna dodawac i usuwac elementy z zbioru.
# frozenset - niemutowalny zbior, ktory nie pozwala na dodawanie i usuwanie elementow - mozna w taki sposob dodawac zbior do zbioru, bo nie mozna go zmieniac.

# konwersje pomiedzy set a lista = list(set(a)) - tworzy liste z elementow zbioru a
# set(L) - tworzy zbior z elementow listy L

# Boolean - klassa bool - wartosci logczien True i False sa tak naprawde instanacjami tej klasy. ODpowiedinja wartosci 1 i 0, bo tym w zasadzie sa, ale z dodatkiem wyswietlania (maja pewnie napidsane metody str)
