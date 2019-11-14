while True:
    A,B = input().split()
    A,B = int(A),int(B)
    if -10000<=A and B<=10000:
        if A > B:
            print(">")
            break
        elif A < B:
            print("<")
            break
        else:
            print("==")
            break