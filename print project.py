
n, m = list(map(int, input("작업 수와 작업 번호를 입력 : ").split()))
# map을 이용하여 입력 수 실수형으로 만듦, list.split를 이용하여 n과m을 공백기준으로 입력
while ((0>n)or(100<n))or((0>m)or(n-1<m)):
    print("범위초과 다시 입력")       
    n, m = list(map(int, input("작업 수와 작업 번호를 입력 : ").split()))
    if (0<=n<=100)and(0<=m<=n-1):
        break
 #조건문을 이용하여 주어진 범위가 아니라면 재입력 
priority = list(map(int, input("우선순위를 입력 :").split()))
#입력 우선순위를 리스트로
maximum = list(range(len(priority)))
#우선순위 배열 생성 (n개의 배열?)
print (maximum)
print (n,m)
print (len(priority))
maximum[m] = 'first'
#원하는 결과를 우선순위 첫번째로 설정
time = 0
#처음 시간
while True:
    if priority[0] == max(priority):
        time =+1
        #목표치와 만날 때 까지 시간증가
        print (priority)
        if maximum[0] == 'first':
            print (time,"분")
            break
        #목표치와 같으면 반복문 탈출하며 프린트
        else:
            priority.pop(0)
            maximum.pop(0)
            #원하는 목표가 아니라면 0번째를 제거
    else:
        priority.append(priority.pop(0))
        maximum.append(maximum.pop(0))
        #제거한 0번째를 다시 요소추가
    
