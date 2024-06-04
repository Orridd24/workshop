import random

def main():
    print("===============================================================")
    print("Selamat datang ke mainan teka alat tulis (dalam satu perkataan)")
    print("===============================================================")
    
    #Senarai (list) alat tulis
    alattulis =["pen","pensel","pemadam","gunting","pembaris","gam","buku"]

    x =random.choice(alattulis)

    #Setkan bilanngan tekaan
    max_cubaan=3

    #Setkan nilai awal cubaan kepada 0
    cubaan=0

    teka=None
    #kod ulangan tekaan alat tulis
    while cubaan<max_cubaan:
        #Masukkan tekaan
        teka = str(input("Cuba teka! Apakah alatan tulis dalam satu perkataan yang dipilih oleh saya? "))
        
        #Jika tekaan sama dengan nilai x
        if x == teka:
            print(f"Tahniah! Tekaan anda tepat sekali".format(teka))
            break

        #Jika tekaan salah. Paparan bilangan peluang tekaan yang tinggal dipaparkan
        else:
            print(f"Maaf! Jawapan anda tidak tepat. Cuba lagi!".format(teka))
            max_cubaan -=1
            print(f"Anda masih tinggal {max_cubaan} kali cubaan.")

        #Jika bilangan teka telah habis    
        if max_cubaan == 0:
            print(f"Cubaan tamat. Jawapan sebenarnya ialah {x}.".format(teka))

#Panggil function main()        
main()