from main import Size
from random import randint
from time import sleep

for x in range(1000):
    a = Size(randint(0, 90), randint(0, 90))
    a.size_win()
    sleep(0.2)
