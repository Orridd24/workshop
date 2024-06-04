import random
#mengimport kod random ke dalam atur cara

def main():
    #Kod aturcara bagi meneka nombor antara 1 hingga 100
    print("Cubaan teka nombor!")
    x=random.randint(1, 100)
    guess=None
    #mengesetkan guess kepada None

    #Struktur kawalan ulangan bagi user meneka sehingga berjaya
    while x!=guess:
        guess=int(input("Pilih satu nombor dari 1 hingga 100: "))
        if x==guess:
            print("Tahniah! Anda hebat")
        elif x>guess:
            print("Cuba teka nombor yang lebih besar.")
        elif x<guess:
            print("Cuba teka nombor yang lebih kecil.")

main()