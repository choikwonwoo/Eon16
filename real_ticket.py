import copy
class Train_ticket:
    def __init__(self):
        file = open("C:/Users/이정희/Downloads/TrainList.txt",'r')
        self.line = file.read()
        self.List_Train = self.line.splitlines()
        self.sub_List = []
        self.a = 0
        for i in range(len(self.List_Train)):
            self.sub_List.append(self.List_Train[i].split())
     
    def main (self):
        while True:
            sel=int(input("1)빠른시간 기차 검색 및 예매\n2)전체 기차 리스트 출력\n3)나의 예매 현황 출력 및 취소\n4)프로그램 종료"))
            if sel == 1:
                print("예매를 선택 하셨습니다")
                self.a = self.a +1
                self.ticketing()
                
            elif sel==2:
                print("리스트 출력")
                for i in range(1,len(self.List_Train), 1):
                    print(self.sub_List[i])
            elif sel == 3:

                
                if self.a == 0:
                    print ("예매된 표가 없습니다.")
                    self.main()
                else:

                    print("현재 예매된 표는 아래와 같습니다")
                    print(self.sub_List[self.time_adress])
                    self.Dont_Want()

            elif sel == 4:
                print("프로그램을 종료합니다.")
                break

    def ticketing(self):
        self.copy_List = []
        # self.List_Train = self.copy_List
        self.copy_List = copy.deepcopy(self.List_Train)

        Want_time =input("원하는 시간을 입력하세요 ex)HH:MM")
        Start = str(input("출발역을 입력하세요"))
        Arrived = str(input("도착역을 입력하세요"))
        Train = str(input("열차종류를 입력하세요"))
        

        for i in range(1,len(self.List_Train), 1):
            if Start != self.sub_List[i][1]:
                self.copy_List[i] = 0
            else: 
                pass

                
        for i in range(1,len(self.List_Train), 1):
            if Arrived != self.sub_List[i][3]:
                self.copy_List[i] = 0
            else:
                pass

        for i in range(1,len(self.List_Train), 1):
            if Train != self.sub_List[i][4]:
                self.copy_List[i] = 0

            else:
                pass
        temp = 0
        for i in range(1,len(self.copy_List),1):
            if self.copy_List[i] == 0:
                temp = temp + 0
            else:
                temp = temp + 1
        if temp == 0:
            print("입력이 잘못되었거나 해당 열차가없습니다. 메인화면으로 돌아갑니다")
            self.main()
        elif temp != 0:
            W_result_time =int(Want_time[0:2])*60+(int(Want_time[3:]))
            


            List_time =[1000]
            
            for i in range(1,len(self.List_Train), 1): 
                if self.copy_List[i] == 0:
                    List_time.append(0)                  
                else:
                    List_time.append(int(self.copy_List[i][0:2])*60+int(self.copy_List[i][3:5]))
            self.ftime = []
            for i in range(len(List_time)):
                if self.copy_List[i] == 0:
                    self.ftime.append(1000)
                else:
                    self.ftime.append(abs(List_time[i] - W_result_time))

            
            self.time_adress = self.ftime.index(min(self.ftime))
            self.sub_List[self.time_adress][-1]=int(self.sub_List[self.time_adress][-1])-1
            print("예매완료")
            return self.sub_List
            
                

    def Dont_Want(self):
        while True:
            DW = int(input("취소 하시겠습니까? Y=1/N=2 : "))
            if DW == 1:
                self.sub_List[self.time_adress][-1]=int(self.sub_List[self.time_adress][-1])+1
                print("취소 되었습니다.")
                self.a = self.a - 1
                break
            if DW == 2:
                print("메인화면으로 돌아갑니다")
                
                break
            else:
                print("다시입력하세요")  

if __name__ == "__main__":
    t = Train_ticket()
    t.main()
