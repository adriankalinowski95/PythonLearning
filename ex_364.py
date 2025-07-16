import copy
from collections import namedtuple

def ex_1():
    print("ex_1")
    
    print(2 ** 16) # 65536
    
    div_1 = 2 / 5
    print("float, becouse result is float " + str(div_1))
    
    div_2 = 2 / 5.0
    print("same float " + str(div_2))
    
    S = "Szynka"
    
    print(S * 5) # 5 times of Szynka
    print(S[:0]) # i don't know 
    
    # Formatowanie
    
    # C-Style 
    print("zielone: %s i %s" % ("abc", "Cde"))
    
    #format
    print("zielone_2: {0} i {1}".format("abc",543))
    
    # copy
    S_cpy_1 = S[:]
    S_cpy_2 = copy.copy(S)
    
    # List MUTABLE
    list_1 = [1, 2, 3, 4]
    print("List_1 " + str(list_1))
    
    # Dict MUTABLE
    dict_1 = {"a": 54, "b": 65}
    print("dict_1 type: {0}".format(type(dict_1)))
    print("Dict_1 " + str(dict_1))
    
    # keys (iterable view) -> list -> str
    print("Dict_1 keys: " + str(list(dict_1.keys())))
    
    iterator = 0
    for key in dict_1:
        print("index: {0} key_for_dict: {1} value: {2}".format(iterator, key, dict_1[key]))
        # number is not mutable, so we need to create new object and pass to veriable
        iterator = iterator + 1
    
    # same like upper
    iterator = 0
    for key in dict_1.keys():
        print("index: {0} key_for_dict: {1} value: {2}".format(iterator, key, dict_1[key]))
        # number is not mutable, so we need to create new object and pass to veriable
        iterator = iterator + 1
        
    
    # Tuple NON MUTABLE
    tuple_1 = (1,)
    print("tuple_1 type: {0}".format(type(tuple_1)))
    
    print("Tuple_1: " + str(tuple_1))
    
    tuple_2 = (1,3,4)
    print("Tuple_2:" + str(tuple_2))
    
    # Set MUTABLE
    set_1 = {1,2,3}
    print("set_1 type: {0}".format(type(set_1)))
    set_1.add(6)
    
    print(set)
    
    # NONE - its a empty object, type of none - relevant to NULL in C
    
def ex_2():
    L = [1,2,3,4]
    #print(L)
    
    # Crash? 
    #print(L[4])
    
    #crash
    # print(L[-1000:100])
    # dziwne, dodaje po prostu item w miejscu 3
    L[3:1] = ['?']
    
    print(L)
    
def ex_3():
    # dodaje tablice w miejsce o indeksie 2
    L = [1,2,3,4]
    L[2] = []
    print(L)
    
    # Usuwa element w miejscu o indeksie 2 
    L = [1,2,3,4]
    L[2:3] = []
    print(L)
    
    # Usuwa elelemnt
    L = [1,2,3,4]
    del L[2]
    print(L)
    
    # Usuwa 2,3
    L = [1,2,3,4]
    del L[1:3]
    print(L)
    
    # Usuwa wszystko po za pierwszym elementem
    L = [1,2,3,4]
    del L[1:]
    print(L)
    
def ex_5():
    D = {}
    D[1] = 'a'
    D[2] = 'b'
    D[(1,2,3)] = 'c'
    
    # Po porstu w slowinku mozna robic wiele kluczy, ale w troche inny sposob - powinny byc one tworzonez elementow niemutowalnych takich jak krotka, liczba, string
    print(D)
    
def ex_6():
    D = {}
    D['a'] = 1
    D['b'] = 2
    D['c'] = 3
    
    try:
        # powinien tu polecie wyjatek
        print(D['d'])
    except Exception as e:
        print(e)
        
    # dodanie elementu
    D['d'] = "abc123"
    print(D)
    
    if 'd' in D:
        print("D have a key 'd'")
        
def ex_7():
    # dodawanie dwoch roznych typow
    
    list = [1,2,3]
    dir = {'a':53, 'b':64}

    # exception?
    try:
        res = list + dir
        print(res)
    except Exception as e:
        print(e)
        
    num = 1
    str_val = "abc"
    
    try:
        res = num + str_val
        print(res)
    except Exception as e:
        print(e)
    
def ex_9():
    first_str = "jajo"
    
    result = first_str[0:3] + first_str[1:2]
    print(result)
    
def ex_10():
    obj = namedtuple('obj', ['name', 'surname', 'age', 'number'])
    instance_1 = obj('adrian', 'k', 15, 66543322)
    
    print("Instance_1: " + str(instance_1))
    
    instance_2 = obj(name="Adrian", surname="K", age=53, number=997)
    print("Instnace_2: " + str(instance_2))
    
    dict_1 = {"name":"Tomasz", "surname": "Babiasz", "age":53, "number":112}
    print("Dict_1: " + str(dict_1))
    
    dict_2 = dict(name="Tomasz_2", surname="Babiasz_2", age=97, number=153)
    print("Dict_2: " + str(dict_2))