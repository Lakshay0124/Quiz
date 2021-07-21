
num=int(input())
Prime=True
for i in range(2,num):
    if (num%i==0):
        Prime=False
        break

if Prime:
        print("Yes it is prime-",num)
else:
            print("no it is no prime-")