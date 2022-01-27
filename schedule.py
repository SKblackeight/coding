#pip install schedule

import schedule 
import time 
import datetime 

#스케쥴 모듈이 동작시킬 코드 : 현재 시간 출력 
def test_fuction(): 
    now = datetime.datetime.now() 
    print("test code- 현재 시간 출력하기") 
    print(now) 
    
    #하루에 3번 test_fuction을 동작시키자 
    schedule.every().day.at("09:00", "12:00", "18:00").do(test_fuction) 
    
    #무한 루프를 돌면서 스케쥴을 유지한다. 
    while True: 
        schedule.run_pending() 
        time.sleep(1)

