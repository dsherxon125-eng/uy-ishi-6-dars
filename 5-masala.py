import os
os.system("cls")

N = int(input("N ni kiriting: "))
sonlar = list(map(int, input("Sonlarni kiriting (bo‘sh joy bilan ajrating): ").split()))

from collections import Counter
count = Counter(sonlar)

sonlar = [x for x in sonlar if count[x] > 1]

print("Natija:", sonlar)
