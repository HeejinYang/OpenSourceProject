import time
import threading


class add:   #합 계산 클래스

    sum=0
    def runadd(self,value):
        #for i in range(0,value,1):
        #   print("%d+"%i,end='') 출력까지 하는 코드, 실행하면 수가 커지면 너무 오래걸림
        for i in range(0,value+1,1):
            add.sum+=i


        print("1+2+3+.....+%d"%value,'=',"%d"%add.sum)

sum1=add()
sum2=add()
sum3=add()

th1=threading.Thread(target=sum1.runadd(100))
th2=threading.Thread(target=sum1.runadd(100000))
th3=threading.Thread(target=sum1.runadd(10000000))

th1.start()
th2.start()
th3.start()