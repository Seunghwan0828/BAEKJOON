while True:
    A,B = input().split()
    A,B = int(A),int(B)
    if 0<A and B<10:
        break
print(A/B)