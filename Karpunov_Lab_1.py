# Лабораторная работа № 1. Вариант 6 (832, 64)
g = 1.62
a_max = 29.43
V_g = 3660
V_p = 3
M = 2150
m = 200
H = float(input("Высота H = "))
V = float(input("Вертикальная скорость V = "))
t = 0
e = 0

while V >= 0:
    e = 180
    k = 10
    a = g + (((V_g - V) * k) / M)
    if t == 0:
        print(V, H, e, k, t, sep="  ")
    while a > a_max:
        k = k - 0.1
        a = g + (((V_g - V) * k) / M)
    a = g + (((V_g - V) * k) / M)
    V = V - a * 0.1
    t = t + 0.1
    H = H + V * 0.1
    m = m - (k * 0.1)
    M = M + (k * 0.1)
    print(V, H, e, m, t, sep="  ")
    t = t + 0.1

if (V_g * m / (M * g)) > (H / V_p):
    e = 0
    while H > 0:
        V = V_p
        H = H - V_p * 0.1
        m = m - ((M * g) / (10 * V_g))
        M = M - ((M * g) / (10 * V_g))
        print(V, H, e, m, t, sep="  ")
        t = t + 0.1
    print("success")

V = 0
q = 0

while (((V_g - V) * m) / (M * g)) + (((a_max + g) * (V_p - V)) / (a_max - g)) + ((V_p - V) / (a_max - g)) < (H / V_p):
    if m < 0 or (H < 0 and V > V_p):
        print("failed")
        q = 1
        break
    elif H < 0 and V <= V_p:
        print("success")
        break
    if V == 0:
        print(V, H, e, m, t, sep="  ")
    V = V + (g * 0.1)
    H = H - (V * 0.1)
    t = t + 0.1
    print(V, H, e, m, t, sep="  ")

while V > V_p:
    e = 0
    if q == 1:
        break
    V = V - (a_max * 0.1)
    H = H - (V * 0.1)
    m = m - ((M * (a_max + g)) / (10 * V_g))
    M = M - ((M * (a_max + g)) / (10 * V_g))
    t = t + 0.1
    print(V, H, e, m, t, sep="  ")
    if m < 0:
        print("failed")
        break

V = V_p

while H > 0:
    e = 0
    if q == 1:
        break
    V = V_p
    H = H - V_p * 0.1
    m = m - ((M * g) / (10 * V_g))
    M = M - ((M * g) / (10 * V_g))
    print(V, H, e, m, t, sep="  ")
    t = t + 0.1
    if m < 0:
        print("success")
        break

if (H < 0 and V > V_p) or m < 0 or q == 1:
    print("failed")
else:
    print("success")
