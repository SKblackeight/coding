#pip install apscheduler

import time
from apscheduler.schedulers.background
import BackgroundScheduler
sched = BackgroundScheduler()

# 매일 12시 30분에 실행
@sched.scheduled_job('cron', hour='9,12,18', minute='00', id='test_2')
def job2():
    print(f'job2 : {time.strftime("%H:%M:%S")}')

print('sched before~')
sched.start()
print('sched after~')

while True:
    time.sleep(1)
