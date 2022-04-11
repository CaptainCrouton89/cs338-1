import math

def encode(str, exp, mod):
    asci = []
    for x in str:
        asci.append(ord(x))
    
    code = []
    code.append((x**exp) % mod)
    return code

def decode(code, exp, mod):
    str = []
    for x in code:
        str.append(chr((x**exp) % mod))
    return str
    
def findPrimeFactors(product):
    for i in range(2, product):
        if product % i == 0:
            return i, product // i
    return 0, 0

def bruteForceTheBIGD(e, lcm):
    THEBIGD = 1
    while((THEBIGD*e) % lcm != 1):
        THEBIGD += 1
    return THEBIGD


# def bruteforce(integer):
    
e = 13

# de mod(lstm) = 1
p, q = findPrimeFactors(5561) # = 67, 83

lcm = math.lcm(p-1, q-1)

print(lcm)
THEBIGD = bruteForceTheBIGD(e, lcm)
print(THEBIGD)

code = [1516, 3860, 2891, 570, 3483, 4022, 3437, 299,
 570, 843, 3433, 5450, 653, 570, 3860, 482,
 3860, 4851, 570, 2187, 4022, 3075, 653, 3860,
 570, 3433, 1511, 2442, 4851, 570, 2187, 3860,
 570, 3433, 1511, 4022, 3411, 5139, 1511, 3433,
 4180, 570, 4169, 4022, 3411, 3075, 570, 3000,
 2442, 2458, 4759, 570, 2863, 2458, 3455, 1106,
 3860, 299, 570, 1511, 3433, 3433, 3000, 653,
 3269, 4951, 4951, 2187, 2187, 2187, 299, 653,
 1106, 1511, 4851, 3860, 3455, 3860, 3075, 299,
 1106, 4022, 3194, 4951, 3437, 2458, 4022, 5139,
 4951, 2442, 3075, 1106, 1511, 3455, 482, 3860,
 653, 4951, 2875, 3668, 2875, 2875, 4951, 3668,
 4063, 4951, 2442, 3455, 3075, 3433, 2442, 5139,
 653, 5077, 2442, 3075, 3860, 5077, 3411, 653,
 3860, 1165, 5077, 2713, 4022, 3075, 5077, 653,
 3433, 2442, 2458, 3409, 3455, 4851, 5139, 5077,
 2713, 2442, 3075, 5077, 3194, 4022, 3075, 3860,
 5077, 3433, 1511, 2442, 4851, 5077, 3000, 3075,
 3860, 482, 3455, 4022, 3411, 653, 2458, 2891,
 5077, 3075, 3860, 3000, 4022, 3075, 3433, 3860,
 1165, 299, 1511, 3433, 3194, 2458]

out_text = "".join(decode(code, THEBIGD, 5561))
print(out_text)