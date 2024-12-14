org = int(input())
up = int(input())
days = int(input())
for i in range(days):
    print(i+1, org)
    org = org + (org * (up/100))