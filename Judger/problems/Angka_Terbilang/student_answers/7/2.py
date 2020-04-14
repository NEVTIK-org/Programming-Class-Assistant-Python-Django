
satuan = ['', 'satu ', 'dua ', 'tiga ', 'empat ', 'lima ',
          'enam ', 'tujuh ', 'delapan ', 'sembilan ', 'sepuluh ', 'sebelas ', 'dua belas ', 'tiga belas ', 'empat belas ', 'lima belas ', 'enam belas ', 'tujuh belas ', 'delapan belas ', 'sembilan belas ']


def tulis(angka, kelipatan):
    terbilang = satuan[angka] + kelipatan
    return terbilang


def ratus_puluh_satuan(angka):
    ratus = angka // 100
    sisa_ratus = angka % 100
    puluh = sisa_ratus // 10
    satuan = angka % 10
    terbilang = ''

    if(ratus == 1):
        terbilang += tulis(0, "seratus ")
    elif(ratus != 1 and ratus >= 1):
        terbilang += tulis(ratus, "ratus ")
    if (sisa_ratus >= 20):
        terbilang += tulis(puluh, "puluh ")
        terbilang += tulis(satuan, "")
    elif(sisa_ratus < 20):
        terbilang += tulis(sisa_ratus, "")

    return terbilang


def milyar_juta_ribu(angka):
    milyar = angka // 1000000000
    sisa_milyar = angka % 1000000000
    juta = sisa_milyar // 1000000
    sisa_juta = sisa_milyar % 1000000
    ribu = sisa_juta // 1000
    sisa_ribu = sisa_juta % 1000
    terbilang = ''

    if(milyar >= 1):
        terbilang += ratus_puluh_satuan(milyar)
        terbilang += "milyar "
    if(juta >= 1):
        terbilang += ratus_puluh_satuan(juta)
        terbilang += "juta "
    if(ribu > 1):
        terbilang += ratus_puluh_satuan(ribu)
        terbilang += "ribu "
    elif(ribu == 1):
        terbilang += "seribu "
    terbilang += ratus_puluh_satuan(sisa_ribu)

    return terbilang

def teriliun(angka):
    triliyun = angka // 1000000000000
    sisa_triliyun = angka % 1000000000000
    terbilang = ''

    if(triliyun >= 1):
        terbilang += milyar_juta_ribu(triliyun)
        terbilang += 'triliyun '    
    terbilang += milyar_juta_ribu(sisa_triliyun)

    return terbilang
        


angka = int(input(""))
terbilang = teriliun(angka)
print(terbilang)
    

        
        
