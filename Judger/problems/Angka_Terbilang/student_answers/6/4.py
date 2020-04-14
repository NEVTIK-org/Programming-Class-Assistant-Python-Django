def terbilang(bilangan):
    angka =["","satu","dua","tiga","empat","lima","enam","tujuh","delapan","sembilan","sepuluh","sebelas"]
    hasil =("")
    n = int(bilangan)
    #bilangan satuan
    if n>=0 and n<=11:
        hasil = angka[n]
    #bilangan belasan
    elif n<20:
        hasil = (terbilang(n-10)+"belas")
    #bilangan puluhan
    elif n<100:
        hasil = (terbilang(n/10)+" puluh"+" "+(terbilang(n%10)))
    #bilangan ratusan khusus sepuluh,sebelas,satu
    elif n<200:
        hasil = "seratus" + terbilang(n-100)
    #bilangan ratusan
    elif n<1000:
        hasil = terbilang(n/100)+ "ratus"+ terbilang(n%100)
    #bilangan ribuan khusus sepuluh,sebelas,satu
    elif n<2000:
        hasil = "seribu" + terbilang(n-1000)
    #bilangan ribuan
    elif n<100000:
        hasil = terbilang(n/1000) + "ribu"+ terbilang(n%1000)
    #bilangan jutaan
    elif n<1000000000:
        hasil = terbilang(n/1000000) + "juta"+ terbilang(n%1000000)
    #bilangan miliaran
    elif n<1000000000000:
        hasil = terbilang(n/1000000000) +"miliyar" + terbilang(n%1000000000)
    #bilangan triliunan
    elif n<100000000000000:
        hasil = terbilang(n/1000000000000) +"triliyun" + terbilang(n%1000000000000)
    #diatas 10 triliun maks 10 ribu triliun
    elif n<=10000000000000000:
        hasil = terbilang(n/1000000000000) +"triliyun" + terbilang(n%1000000000000)
    return hasil
a =int(input())
huruf = terbilang(a)
print(huruf)
