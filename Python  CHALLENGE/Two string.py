def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"
for _ in range(int(input())):
    print(twoStrings(input(), input()))