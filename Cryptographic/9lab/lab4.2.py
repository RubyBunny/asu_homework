import math
import sys
import random

sys.set_int_max_str_digits(8096)

def get_text_from_file(filename: str) -> str:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        return text

def write_text_in_file(filename: str, text: str):
        with open(filename, "w+", encoding="utf-8") as file:
            file.write(str(text))

def foo(a, z ,n):
    '''return a^z mod n'''

    if z == 0:
        return 1
    
    t = int(math.log2(z))

    lst1 = []
    for i in range(0, t+1):
       lst1.append(pow(a, 2**i, n))
    lst1.reverse()

    zbin = list(bin(z))
    zbin = zbin[2:]

    for i in range(0, t+1):
        if int(zbin[i]) == 0:
            lst1[i] = 1
        
    x = 1
    for i in lst1:
        x *= int(i)

    return x % n

def str2bin(text: str, encoding='utf_8') -> str:
    return ''.join(bin(c)[2:].rjust(8, '0') for c in text.encode(encoding))


# def choosing_g(p, g):
#     '''Проверка выбора примитивного элемeнта g'''

#     p_list = []
#     for i in range(1, p):
#         p_list.append(i)

#     g_list = []
#     for i in range(0, p-1):

#         k = foo(g, i, p)
#         if k not in g_list:

#             g_list.append(k)

#     for i in p_list:
#         if i not in g_list:
#             raise ValueError(f"g = {g} не является примитивным для p = {p}")
        
def is_primitive_root(p, g):
    if pow(g, (p - 1) // 2, p) == 1:
        raise ValueError(f"g = {g} не является примитивным для p = {p}")
    if pow(g, (p - 1) // 3, p) == 1:
        raise ValueError(f"g = {g} не является примитивным для p = {p}")
    return True
        

def get_key(x, gymodp, p, g):

    gxmodp = foo(g, x, p)

    if gxmodp | gymodp == 1:
        raise ValueError(f"gxmodp = {gxmodp}, gymodp = {gymodp}")

    key = foo(gymodp, x, p)

    return key

def main():

    p = 30803
    g = 6
    
    print(is_primitive_root(p, g))

    a = random.randint(1, p)
    b = random.randint(1, p)

    gamodp = foo(g, a, p)

    write_text_in_file('gamodp.txt', gamodp)

    gbmodp = foo(g, b, p)

    write_text_in_file('gbmodp.txt', gbmodp)

    A_k = get_key(a, int(get_text_from_file('gbmodp.txt')), p, g)

    write_text_in_file('A_key.txt', A_k)
    
    B_k = get_key(b, int(get_text_from_file('gamodp.txt')), p, g)

    write_text_in_file('B_key.txt', B_k)


main()
