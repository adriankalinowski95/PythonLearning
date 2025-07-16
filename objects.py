#obiekty i zmienne
# zmienna jest tak na prawde aliasem na obiekt. Posiada ona referencje do obiektu, ktory jest w pamieci. Mozna wiec zmieniac zmienne, ale nie mozna zmieniac obiektow, ktore sa immutable.
# obiekty posiadaja typ, wartosc oraz counter referencji. ZMIENNIE NIE MAJA TYPU tylko REFERENCJE DO OBIEKTU.

# jezeli do zmiennej przypisywany jest inny obiekt, to poprzedni obiekt jest uwauny z pamieci zap omoca garbage collectora.
# dzieje sie tka, poniewaz refrence counter jest zmneisjzany o 1, a jezeli jest rowny 0, to obiekt jest usuwany z pamieci.
# trzeba uwazac na reference loops, bo wtedy obiekty moga nigdy sie nie zwonlci

# zmienne sa twak na prawde potworzne w momencie wywolania, gdy interpeter do nich przyjdzie. Wtedy tworzy sie dany obiekt i przypisuje referencje do zmienne

# jezeli przypiszemy zmienna
# a = 1
# b = a
# to zmienna b bedzie wskazywac na ten sam obiekt co a, - jest to refernecja wspodzielona
# w PYTHON ZAWSZE zmienne sa WSKAZNIKAMI do obiektow, a nie obiektami samymi w sobie.

# Kopiowanie obiektow: 
# L1 = [1, 2, 3]
# L2 = L1  # L2 jest referencja do tego samego ob
# L3 = L1.copy()   L3 jest nowym obiektem, ktory jest kopia L1
# L4 = list(L1)   L4 jest nowym obiektem, ktory jest kopia L1
# L5 = L1[:]   L5 jest nowym obiektem, ktory jest kopia L1

# import copy
# x = copy.copy(Y)
# x = copy.deepcopy(Y)  # deepcopy tworzy nowy obiekt, ktory jest kopia Y, ale nie jest referencja do Y

# W pamieci podrecznej umeiszczamy: 
# liczby calokwoite i napisy
# Przez to czasami np. dla liczb zostane one umieszczone w tabli podrecznej i nie bedzie potrzeby tworzenia nowego obiektu, bo zostanie on pobrany z pamieci podrecznej. - po uwolnieinu nie zostnaie zwolniony z pamieci, bo jest w pamieci podrecznej.

# POROWNyWNAIE OBIEKTGOW
# L == M poroywanyie wartosic
# L is M porownywanie referencji

# smiesz sparaw - 
# X = 42
# Y = 42
# X is Y  # True, bo 42 jest w pamieci podrecznej
# X = 43
# Y is X  # True - pamieci podreczena dziala
# mozna to srpawdic za pomoca sys.getrefcount(1) - zwraca licznik referencji do obiektu, czyli ile zmiennych wskazuje na ten obiekt.

# dziala to dla obiektow niemutwoalnych

# weak referencese - podobne do weak ptr - czasami trzeba uzyc tak jak w c++