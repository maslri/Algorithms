def gcd(m, n):
    fm = []
    for i in range(1, m + 1):
        if m % i == 0:
            fm.append(i)
    fn = []
    for j in range(1, n + 1):
        if n % j == 0:
            fn.append(j)
    fc = []
    for k in fm:
        if k in fn:
            fc.append(k)
    return max(fc)


def gcd_2(m, n):
    i = min(m, n)
    while i > 0:
        if m % i == 0 and n % i == 0:
            return i
        else:
            i -= 1
    else:
        return 0

print("GCD(1024 , 128) = " + str(gcd(1024, 128)))
print("GCD_2(1024 , 128) = " + str(gcd_2(1024, 128)))
