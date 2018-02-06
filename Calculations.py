import math as m

def p_star(r, a, b):
    return (r-a)/(b-a)

def combination(n, k):
    return m.factorial(n) / (m.factorial(k) * m.factorial(n - k))

def f(x, n, a, b, p, k):
    res = [max(x * ((1 + b) ** i) * ((1 + a) ** (n - i)) - k, 0) * combination(int(n), i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(int(n) + 1)]
    return sum(res)
# print(f(100,2,-0.3,0.4,4/7,110))

def gamma(r, n_big, n, s, a, b, p, k):
    return (1 + r) ** (n - n_big) * (f(s*(1+b),n_big-n,a,b,p,k) - f(s*(1+a),n_big-n,a,b,p,k)) / (s * (b - a))

def c(r, n, s, a, b, p, k):
    return (1 + r) ** -n * f(s,n,a,b,p,k)

def beta(x, gamma, s, b):
    return (x - gamma * s) / b

n = 1
b_big = 1
r = 0
s = 150
k = 150
a = -2/5
b = 1/5
p = p_star(r,a,b)
x = c(r,n,s,a,b,p,k)
print(x)
g = gamma(r,n,n,s,a,b,p,k)
print(g)
bet = beta(x,g,s,b_big)
print(bet)