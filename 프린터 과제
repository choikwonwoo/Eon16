n, m = list(map(int, input("작업 수와 작업 번호를 입력 : ").split()))
while ((0>n)or(100<n))or((0>m)or(n-1<m)):
    print("범위초과 다시 입력")       
    n, m = list(map(int, input("작업 수와 작업 번호를 입력 : ").split()))
    if (0<=n<=100)and(0<=m<=n-1):
        break
priority = list(map(int, input("우선순위를 입력 :").split())) 
maximum = list(range(len(priority)))
maximum[m] = 'first'

time = 0
while True:
    if priority[0] == max(priority):
        time =+1       
        if maximum[0] == 'first':
            print (time,"분")
            break
        else:
            priority.pop(0)
            maximum.pop(0)
    else:
        priority.append(priority.pop(0))
        maximum.append(maximum.pop(0))
