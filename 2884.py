H = 0
M = 0
while True:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if 0 <= a <= 23 and 0 <= b <= 59:
        H = H + a
        M = M + b
        if M - 45 < 0:
            H = H - 1
            if H < 0:
                H = H + 24
            M = M - 45
            M = 60 + M
        else:
            M = M - 45
        break
    else: continue
print(H,M)