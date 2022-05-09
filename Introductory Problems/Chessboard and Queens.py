def check(queen):
    for i in range(len(queen)-1):
        for j in range(i+1,len(queen)):
            if i==j:
                continue
            if queen[i]==queen[j] or abs(queen[i]-queen[j])==abs(i-j):
                return False
    return True

arr = []
for i in range(8):
    reserved = []
    s = input()
    for j in range(len(s)):
        if s[j]=='*':
            reserved.append(j)
    arr.append(reserved)
count = 0
queen = []
for i1 in range(8):
    if not check(queen):
        break
    if i1 in arr[0]:
        continue
    queen.append(i1)
    for i2 in range(8):
        if not check(queen):
            break
        if i2 in arr[1]:
            continue
        queen.append(i2)
        for i3 in range(8):
            if not check(queen):
                break
            if i3 in arr[2]:
                continue
            queen.append(i3)
            for i4 in range(8):
                if not check(queen):
                    break
                if i4 in arr[3]:
                    continue
                queen.append(i4)
                for i5 in range(8):
                    if not check(queen):
                        break
                    if i5 in arr[4]:
                        continue
                    queen.append(i5)
                    for i6 in range(8):
                        if not check(queen):
                            break
                        if i6 in arr[5]:
                            continue
                        queen.append(i6)
                        for i7 in range(8):
                            if not check(queen):
                                break
                            if i7 in arr[6]:
                                continue
                            queen.append(i7)
                            for i8 in range(8):
                                if not check(queen):
                                    break
                                if i8 in arr[7]:
                                    continue
                                queen.append(i8)
                                if check(queen):
                                    count = count+1
                                queen.pop(len(queen)-1)
                            queen.pop(len(queen)-1)
                        queen.pop(len(queen)-1)
                    queen.pop(len(queen)-1)
                queen.pop(len(queen)-1)
            queen.pop(len(queen)-1)
        queen.pop(len(queen)-1)
    queen.pop(len(queen)-1)
print(count)