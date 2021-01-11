num = int(input())

for i in range(1, num + 1):
    if i != 1 and num % i == 0:
        print(i)
        break
