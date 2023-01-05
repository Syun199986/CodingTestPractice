k = int(input())
a, b = map(str, input().split())

a_dec = int(a, k)
b_dec = int(b, k)

print(a_dec * b_dec)