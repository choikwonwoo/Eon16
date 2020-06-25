num = int(input("번호 입력")) # 원하는 숫자 입력
arr = [[0]*num for i in range(num)] # 원하는 숫자의 정사각형 배열 생성

n=0
row =0
col = -1
sf =1


def snail(n,row,col,sf,arr,num):

    for i in range(1,num+1):
        n= n+1
        col = col + sf
        arr[row][col] = n    
    num = num -1
    for j in range(1,num+1):
        n = n+1
        row = row + sf
        arr[row][col] = n
    sf = sf*-1
    if n == num*num:
        return    
    snail(n,row,col,sf,arr,num)

snail(n,row,col,sf,arr,num)

print (arr)
