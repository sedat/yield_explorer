import schedule
import time
from yield_explorer import main

schedule.every().hour.do(main)

while 1:
    n = schedule.idle_seconds()
    if n is None:
        break
    elif n > 0:
        time.sleep(n)
    schedule.run_pending()
