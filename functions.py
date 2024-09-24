
def double(n):
    return 2*n
def triple(n):
    return 3*n
def quadruple(n):
    return double(double(n))
def funky(n,m):
    return n*3 + double(double(m))

n = 3
m = 14
d1 = double(n)       # 6
d2 = double(m)       # 28

t1 = triple(n)       # 9
t2 = triple(m)       # 42

q1 = quadruple(n)    # 12
q2 = quadruple(m)    # 56

f1 = funky(n, m)     # 65
f2 = funky(m, m)     # 98

