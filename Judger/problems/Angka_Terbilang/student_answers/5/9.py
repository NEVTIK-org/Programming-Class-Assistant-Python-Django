def terbilang(bil):
    angka = ["","satu","dua","tiga","empat","lima","enam",
             "tujuh","delapan","sembilan","sepuluh","sebelas"]
    hasil = ""
    n = int(bil)
    if n >= 0 and n <= 11:
        hasil = angka[n]
    elif n < 20:
        hasil = terbilang(n-10) + "belas"
    elif n < 100:
        hasil = terbilang(n/10) + "puluh" + terbilang(n%10)
    elif n < 200:
        hasil = "seratus" + terbilang(n-100)
    elif n < 1000:
        hasil = terbilang(n/100) + "ratus" + terbilang(n%100)
    elif n < 2000:
        hasil = "seribu" + terbilang(n-1000)
    elif n < 1000000:
        hasil = terbilang(n/1000) + "ribu" + terbilang(n%1000) 
    elif n < 1000000000:
        hasil = terbilang(n/1000000) + "juta" + terbilang(n%1000000)
    elif n < 1000000000000:
        hasil = terbilang(n/1000000000) + "milyar" + terbilang(n%1000000000)
    elif n < 1000000000000000:
        hasil=terbilang(n/1000000000000) + "triliyun"+ terbilang(n%1000000000000)
    elif n < 1000000000000000000:
        hasil=terbilang(n/1000000000000000) + "kuadriliun"+ terbilang(n%1000000000000000)
    elif n < 1000000000000000000000:
        hasil=terbilang(n/1000000000000000000) + "kuantiliun"+ terbilang(n%1000000000000000000)
    elif n < 1000000000000000000000000:
        hasil=terbilang(n/1000000000000000000000) + "sekstiliun"+ terbilang(n%1000000000000000000000)
        
    return hasil

a = input()
huruf = terbilang(a)
print(huruf)
