def mul(A, B):
    x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    k = A[1][0] * B[0][1] + A[1][1] * B[1][1]

    return [[x, y], [z, k]]

def pow(A, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return [row[:] for row in A]
    else:
        d, r = divmod(n, 2)
        B = pow(A, d)
        B = mul(B, B)
        if r > 0:
            B = mul(B, A)
        return B

def Fib(n):
    Q = [[1, 1], [1, 0]]
    return pow(Q, n)[0][1]

n = Fib(10)

print(n % 10**6)