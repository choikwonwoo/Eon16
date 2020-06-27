import os
import books 

TF = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(TF,'input.txt')
f = open(my_file,'r')
Bls = f.readlines()

class user:
    
    def __init__(self):
        self.funtion_clss = books.funtion()
    
    def Menu_List(self):
        print("1. 도서추가")
        print("2. 도서검색")
        print("3. 도서 정보 수정")
        print("4. 도서삭제")
        print("5. 도서 목록 출력")
        print("6. 저장")
        print("7. 종료")

    def Menu (self,Bls):
        self.Menu_List()
        Sel_Num = int(input("메뉴를 선택하세요"))

        if Sel_Num ==1:
            self.funtion_clss.Add_book(Bls)
            #도서 추가 클래스 입력 (시스템 클라스)
            
            self.Menu(Bls)
        
        elif Sel_Num ==2:
            self.funtion_clss.search_book(Bls)
            #도서 검색 (시스템 클라스)
            
            self.Menu(Bls)
        
        elif Sel_Num ==3:
            self.funtion_clss.book_refair(Bls)
            #정보 수정
        
            self.Menu(Bls)
        
        elif Sel_Num ==4:
            self.funtion_clss.delete(Bls)
            #도서 삭제
        
            self.Menu(Bls)
        
        elif Sel_Num ==5:
            self.funtion_clss.out_list(Bls)
            # 도서 목록 출력
        
            self.Menu(Bls)
        
        elif Sel_Num ==6:
            self.funtion_clss.save(Bls)
            #저장?
        
            self.Menu(Bls)
        
        elif Sel_Num ==7:
            self.funtion_clss.fin(Bls)
            #종료
            
            print("프로그램을 마칩니다.")

b=user()
b.Menu(Bls)
