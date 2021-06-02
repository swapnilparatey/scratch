from time import sleep
import random

while True:
    x = random.randint(0, 800)
    print(x)
    sleep(x/100)