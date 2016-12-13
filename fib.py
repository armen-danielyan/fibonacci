def Fib(n):
    Q = [[1, 1], [1, 0]]
    return pow(Q, n)[0][1] % 10**6

def mul(F, _F):
    x = F[0][0] * _F[0][0] + F[0][1] * _F[1][0]
    y = F[0][0] * _F[0][1] + F[0][1] * _F[1][1]
    z = F[1][0] * _F[0][0] + F[1][1] * _F[1][0]
    k = F[1][0] * _F[0][1] + F[1][1] * _F[1][1]

    return [[x, y], [z, k]]

def pow(F, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return [row[:] for row in F]
    else:
        d, r = divmod(n, 2)
        _F = pow(F, d)
        _F = mul(_F, _F)
        if r > 0:
            _F = mul(_F, F)
        return _F

n = Fib(100)

print(n)