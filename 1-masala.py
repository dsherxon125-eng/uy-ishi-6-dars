import os
os.system("cls")

def nollarni_oxiriga_otkaz(lst):
    yangi_list = []
    nol_soni = 0

    for son in lst:
        if son == 0:
            nol_soni += 1
        else:
            yangi_list.append(son)

    yangi_list.extend([0] * nol_soni)
    return yangi_list


lst = [3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]
print(nollarni_oxiriga_otkaz(lst))
