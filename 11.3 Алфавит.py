abcd = []
count = 1
last_digit = ord('a')
for i in range(26):
    abcd.append(chr(last_digit) * count)
    last_digit += 1
    count += 1
print(abcd)