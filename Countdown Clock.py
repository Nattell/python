
### Countdown Clock ###

import datetime as dt
now = dt.datetime.now()
new = dt.datetime(2025, 1,1)

print(now)

diff = new - now
while diff.seconds >= 0:
   
    # update now with the new date
    now = dt.datetime.now()

    # update diff to know the new difference
    diff = new - now 
    
    # print "there´s X seconds left, X minutes, X hours and X days"
    print(f"there are {diff.seconds} seconds left, there are {diff.seconds / 60} minutes left, there are {diff.seconds /3600} hours left, there are {diff.days} days left") 
