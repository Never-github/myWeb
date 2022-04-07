import sys
import gc



class a:
    c = 1
x = a()
x1= x
print(sys.getrefcount(x1))
del x1
print(sys.getrefcount(x))


