n = int(input())
s = input()

a_count = s.count('A')
t_count = s.count('T')

if(a_count > t_count):
    print('A')
elif(a_count < t_count):
    print('T')
else:
    if(s[n-1] == 'A'):
        print('T')
    else:
        print('A')