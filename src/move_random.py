from main import Move
from random import randint
from time import sleep

for x in range(1000):
    a = Move(False, randint(0, 800), randint(0, 800))
    a.move_win()
    sleep(0.2)
