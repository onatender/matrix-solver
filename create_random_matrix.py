
import random

degiskenler = []
for i in range(0,4):
    degiskenler.append(random.randint(-10, 10))
    print(f"x{i+1}={degiskenler}")

for i in range(4):
    toplam = 0
    print("[", end="")
    for r in range(4):
        rand = random.randint(-10, 10)
        toplam += rand * degiskenler[r]
        print(rand, ",", end="")
    print(toplam, end="")
    print("],", end="")
    print()
