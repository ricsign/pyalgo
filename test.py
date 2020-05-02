def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

val = (2**1010)*(23**2020)+1
for i in range(1000,9999):
    if val % i == 0:
        print(i)
        break


print('-----')