
cdef extern from "clib.h":
    double test(double a, double b)
    int add(int a, int b)
    int sub(int a, int b)

def wrap_test(a,b):
    return test(a,b)

def wrap_add(a,b):
    return add(a, b)

def wrap_sub(a,b):
    return sub(a,b)
