import os
os.system("cls")

def dublikatlarni_olib_tashlash(lst):
    natija = []
    korilgan = set()
    
    for i in lst:
        t = tuple(i)   
        if t not in korilgan:
            korilgan.add(t)
            natija.append(i)
    
    return natija



input = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
output = dublikatlarni_olib_tashlash(input)
print(output)
