from bisect import bisect_left as bl
N = int(input())
A = list(map(int, input().split()))
lis = []
for a in A:
    if not lis or lis[-1] < a:
        lis.append(a)
    else:
        lis[bl(lis, a)] = a
print(len(lis))