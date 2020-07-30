from main import Size

for j in range(1000):
    for a in range(0, 90):
        q = Size(a, 0)
        q.size_win()

    for b in range(0, 90):
        w = Size(0, b)
        w.size_win()
