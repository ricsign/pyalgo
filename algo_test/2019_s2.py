def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solve(num):
    for i in range(num,1,-1):
        j = num*2-i
        if is_prime(i) and is_prime(j):
            return (i,j)

num = int(input())
ret = []
for _ in range(num):
    ret.append(solve(int(input())))

for a in ret:
    print(str(a[0])+" "+str(a[1]))
