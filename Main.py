
import sched, time

def trade():
    print("period " + str(time.time()))

def main():
    period = 2

    while(True):
        trade()
        time.sleep(period)

main()