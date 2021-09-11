import time


def printCycle(a):
    while a != 10:
        print("I'm the loop")
        time.sleep(1)
        a = a + 1
        if a == 10:
            break

printCycle(5)
