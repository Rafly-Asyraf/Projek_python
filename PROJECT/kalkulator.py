while(True):
    print("1. Tambah ")
    print("2. Kurang")
    print("3. Kali ")
    print("4. Bagi")
    print("5. sisa bagi ")
    print("6. exit")
    print("")

    print("=====================================")
    nomer =int(input("MASUKAN ANGKA 1/2/3/4/5/6 = "))
    print("=====================================")

    if nomer == 1 :
        i=int(input('Masukan Angka ke 1 = '))
        x=int(input('Masukan Angka ke 2 = '))
        z=i+x
        print('hasil =',z)
        print("")

    elif nomer == 2 :
        i=int(input('Masukan Angka ke 1 = '))
        x=int(input('Masukan Angka ke 2 = '))
        z=i-x
        print('hasil =',z)
        print("")

    elif nomer == 3 :
        i=int(input('Masukan Angka ke 1 = '))
        x=int(input('Masukan Angka ke 2 = '))
        z=i*x
        print('hasil =',z)
        print("")

    elif nomer == 4 :
        i=int(input('Masukan Angka ke 1 = '))
        x=int(input('Masukan Angka ke 2 = '))
        z=i/x
        print('hasil =',z)
        print("")

    elif nomer == 5 :
        i=int(input('Masukan Angka ke 1 = '))
        x=int(input('Masukan Angka ke 2 = '))
        z=i%x
        print('hasil =',z)
        print("")

    
    else:
        break

print("bye")
