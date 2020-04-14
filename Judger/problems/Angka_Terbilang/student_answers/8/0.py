import random
import time
wait = time.sleep

def rangefloat():
    angka = 0
    while True:
        angka += 1
        nilai = random.randint(32 , 98)
        print("suhu fahrenheit", angka ,":", nilai)
        cara = (nilai - 32) * 5 / 9
        print("suhu celcius", angka ,":", cara)
        wait(.25)
        print()
        if angka == 1000:
            break
rangefloat()
