f = 0
for a in range(1, 151):
    if f == 1:
        break
    for b in range(a, 151):
        if f == 1:
            break
        for c in range(b, 151):
            if f == 1:
                break
            for d in range(c, 151):
                e = (a**5 + b**5 + c**5 + d**5)**0.2
                ie = int(e)
                if round(e,10) == ie:
                    print(a,b,c,d,e)
                    print(a+b+c+d+e)
                    f = 1
                    break
print("END")