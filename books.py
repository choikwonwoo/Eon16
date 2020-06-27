import re
import os

    
class funtion:




    def Add_book(self,Bls):

        self.book = str(input("추가할 책정보 입력\nEx) 제목 저자 발행년도 출판사 카테고리 순서로 입력하시오.\n:"))
        self.book_info = self.book.split()
        print(self.book_info)
        Q = int(input("제목 : %s 저자 : %s 발행년도 : %s 출판사 : %s 카테고리 : %s \n 저장하시겠습니까?(yes = 1, no = 2)"%(self.book_info[0],[1],[2],[3],[4])))
        if Q == 1:
            Bls.append(self.book+'\n')
            print("추가되었습니다.")
        
        elif Q == 2:
            print("취소하셨습니다. 메인으로 돌아갑니다.")
        return Bls

    def search_book(self,Bls):
        Sr = str(input("검색어를 입력 하세요"))
        for i in range(0,len(Bls),1):
            if Sr in Bls[i]:
                print(Bls[i])
        print("검색완료")

    def book_refair(self,Bls):
        for i in range(len(Bls)):
            print(i)
            print(Bls[i])
        num = int(input("대상 번호를 입력하세요"))
        Bls[num] = str(input("수정할 책정보를 입력하세요.\nEx) 제목 저자 발행년도 출판사 카테고리 순서로 입력하시오.\n:"))
        print("수정되었습니다.")
        return Bls


    def delete(self,Bls):
        for i in range(len(Bls)):
            print(i)
            print(Bls[i])
        num = int(input("삭제할 책 번호를 입력하세요"))
        Bls.pop(num)
        print("삭제되었습니다.")
        return Bls

    def out_list(self,Bls):
        print ("현재 책 목록은 다음과 같습니다.")
        print (Bls)
    
    def save(self,Bls):
        save_book = ''.join(Bls)
        TF = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(TF,'input.txt')
        wr = open(my_file,'w')
        wr.write(save_book)
        wr.close
        print("저장되었습니다.")

    def fin(self,Bls):
        last_book = ''.join(Bls)
        TF = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(TF,'input.txt')
        wr = open(my_file,'w')
        wr.write(last_book)
        wr.close 
        print("자동저장")
