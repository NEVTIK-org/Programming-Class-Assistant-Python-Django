def decor(rip):
    def inner(*error1, **error2):
        print("Zzz----------Zzz")
        rip(*error1, **error2)
        print("Zzz----------Zzz\n\n")
    return inner

@decor
def testimoni(text):
    print(": ", text, " :")

def main_text(text):
    print(text)

def main():
    testimoni("Tapi Nama Ane Bukan Mulia Tolong")
    testimoni("I'am MULIA")
    main_text("I'am XXX")

main()
