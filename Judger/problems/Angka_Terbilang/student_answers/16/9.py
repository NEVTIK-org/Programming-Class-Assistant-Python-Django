import random, sys

anggota = {"kevin": [], "rama":[], "rian":[]}
soal = list(range(1, 13))
del soal[0]
del soal[0]
del soal[4]
perorang = len(soal)/len(anggota)

for i in anggota:
 for a in range(int(perorang)):
  s = random.choice(soal)
  anggota[i].append(s)
  
  del soal[soal.index(s)]
 print(i+": ", str(anggota[i]))
 

