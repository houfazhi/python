# 开发时间：2023/8/14 10:48
import schedule
import time
def fun():
    print('距离比赛结束还剩1秒')

schedule.every(1).seconds.do(fun)
while True:
    schedule.run_pending()
    time.sleep(1)


