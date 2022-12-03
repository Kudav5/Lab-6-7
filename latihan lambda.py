# Ubahlah kode dibawah ini menjadi fungsi menggunakan lambda
import math
'''
def a(x):
    return x**2         # jika x = 5 maka outputnya 25
'''
a = lambda x : x**2
print(a(5))             # jika x = 5 maka outputnya 25

'''
def b(x, y):
    return math.sqrt(x**2 + y**2)       # jika x,y = 5 maka outputnya 7.0710678118654755
'''
b = lambda x, y : math.sqrt(x**2 + y**2)
print(b(5,5))                           # jika x,y = 5 maka outputnya 7.0710678118654755

'''
def c(*args):
    return sum(args)/len(args)          # Jika args = 5.0 maka outputnya tetap
'''
c = lambda *args : sum(args)/len(args)
print(c(5.0))                           # Jika args = 5.0 maka outputnya tetap

'''
def d(s):
    return "".join(set(s))              # jika s = 'aiueo' maka outputnya secara acak
'''
d = lambda s : "".join(set(s))
print(d('aiueo'))                       # jika s = 'aiueo' maka outputnya secara acak