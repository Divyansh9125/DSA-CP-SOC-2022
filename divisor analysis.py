n= int(input())
num = 1
for i in range (n):
    x, k = map(int,input().split())
    num  = num * (x**k)
    def no_of_div(y):
        count = 0
        for j in range (1,y+1):
            if (y%j == 0):
                count = count + 1
            count = count
        print(count)

    def sum_of_div(y):
        sum = 0
        for j in range (1,y+1):
            if (y%j == 0):
                sum = sum + j
            sum = sum
        print(sum)

    def pro_of_div(y):
        pro = 1
        for j in range (1,y+1):
            if (y%j == 0):
                pro = pro * j
            pro = pro
        print(pro)

print(no_of_div(num))
print(sum_of_div(num))
print(pro_of_div(num))
    


