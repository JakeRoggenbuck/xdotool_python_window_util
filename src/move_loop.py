from main import Move

for a in range(100):
    for x in range(0, 40):
        a = Move(True, x, 0)
        a.move_win()

    for y in range(0, 20):
        a = Move(True, 0, y)
        a.move_win()

    for x in range(-40, 0):
        a = Move(True, x, 0)
        a.move_win()

    for y in range(-20, 0):
        a = Move(True, 0, y)
        a.move_win()
