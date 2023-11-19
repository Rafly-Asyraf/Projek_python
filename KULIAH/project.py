print("========== (PROGRAM PENJUALAN MARTABAK) ==========")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

total1=0
jenis1=""
porsi=0
gelas=0

def fungsimakanan():
   global total1
   global porsi
   global jenis1
   print("==================================================")
   print("\n\t\tMENU MARTABAK MANIS\n")
   print("==================================================")
   print("1.  Coklat                     -      Rp20000")
   print("2.  Keju                       -      Rp20000")
   print("3.  Coklat Keju                -      Rp25000")
   print("4.  Pisang keju                -      Rp27000")
   print("5.  Coklat Kacang Susu         -      Rp30000")
   print("6.  Pisang coklat keju         -      Rp30000")
   print("7.  Coklat Keju susu           -      Rp33000")
   print("8.  Blueberry/Strawberry       -      Rp35000")
   print("9.  Silverqueen                -      Rp37000")
   print("10. Coklat wijen keju susu     -      Rp40000")
   print("==================================================")
   print("\n\t\tMENU MARTABAK ASIN\n")
   print("==================================================")
   print("11. Biasa[ 1 Telur]            -      Rp20000")
   print("12. Special[ 2 Telur]          -      Rp25000")
   print("13. Istimewa[ 3 Telur]         -      Rp32000")
   print("14. Super[ 4 Telur]            -      Rp38000")
   print("15. Jumbo[ 5 Telur]            -      Rp45000")
   print("==================================================")
   nomor =int(input("Masukan Pilihan: "))
   porsi =int(input("Berapa Porsi   : "))

   if nomor==1:
       total1 = porsi * 20000
       print(porsi," Porsi Coklat = Rp", total1)
       jenis1=("Coklat")
   elif nomor==2:
       total1 = porsi * 20000
       print(porsi," Porsi keju = Rp", total1)
       jenis1=("Keju")
   elif nomor==3:
       total1 = porsi * 25000
       print(porsi," Porsi Coklat Keju = Rp", total1)
       jenis1=("Coklat Keju")
   elif nomor==4:
       total1 = porsi * 27000
       print(porsi," Porsi Pisang Keju = Rp", total1)
       jenis1=("Pisang Keju")
   elif nomor==5:
       total1 = porsi * 30000
       print(porsi," Porsi Coklat Kacang Susu = Rp", total1)
       jenis1=("Coklat Kacang Susu")
   elif nomor==6:
       total1 = porsi * 30000
       print(porsi," Porsi Pisang Coklat Susu = Rp", total1)
       jenis1=("Pisang Coklat Susu")
   elif nomor==7:
       total1 = porsi * 33000
       print(porsi," Porsi Coklat Keju Susu = Rp", total1)
       jenis1=("Coklat Keju Susu")
   elif nomor==8:
       total1 = porsi * 35000
       print(porsi," Porsi Blueberry/Strawberry = Rp", total1)
       jenis1=("Blueberry/Strawberry")
   elif nomor==9:
       total1 = porsi * 37000
       print(porsi," Porsi Silverqueen = Rp", total1)
       jenis1=("Silverqueen")
   elif nomor==10:
       total1 = porsi * 40000
       print(porsi," Porsi Coklat Wijen Keju Susu = Rp", total1)
       jenis1=("Coklat Wijen Keju Susu")
   elif nomor==11:
       total1 = porsi * 20000
       print(porsi," Porsi Biasa[ 1 Telur] = Rp", total1)
       jenis1=("Biasa[ 1 Telur]")
   elif nomor==12:
       total1 = porsi * 25000
       print(porsi," Porsi Special[ 2 Telur] = Rp", total1)
       jenis1=("Porsi Special[ 2 Telur]")
   elif nomor==13:
       total1 = porsi * 32000
       print(porsi," Porsi Istimewa[ 3 Telur] = Rp", total1)
       jenis1=("Porsi Istimewa[ 3 Telur]")
   elif nomor==14:
       total1 = porsi * 38000
       print(porsi," Porsi Super[ 4 Telur] = Rp", total1)
       jenis1=("Porsi Super[ 4 Telur]")
   elif nomor==15:
       total1 = porsi * 45000
       print(porsi," Porsi Jumbo[ 5 Telur] = Rp", total1)
       jenis1=("Porsi Jumbo[ 5 Telur]")
   else:
       print("Pilihan tidak ada, silahkan masukan lagi!!")
       
total2=0
jenis2=""

def fungsiminuman():
   global total2
   global jenis2
   global gelas
   print("==================================================")
   print("\n\t\t MENU MINUMAN\n")
   print("==================================================")
   print("1. Es teh Manis   -     Rp5000")
   print("2. Es jeruk       -     Rp8000")
   print("3. Es kopi        -     Rp4000")
   print("4. Aqua Botol     -     Rp4500")
   print("5. Teh Botol      -     Rp6000")
   print("==================================================")
  
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas/Botol: "))

   if nomor==1:
       total2= gelas * 5000
       print (gelas," Es Teh Manis = Rp", total2)
       jenis2=(" Gelas Es Teh Manis")
   elif nomor==2:
       total2= gelas * 8000
       print (gelas, " Gelas Es Jeruk = Rp", total2)
       jenis2=("Es Jeruk")
   elif nomor==3:
       total2= gelas * 4000
       print (gelas, " Gelas Es Kopi = Rp", total2)
       jenis2=("Es Kopi")
   elif nomor==4:
       total2= gelas * 4000
       print(gelas," Gelas Aqua Botol = Rp", total2)
       jenis2=("Aqua Botol")
   elif nomor==5:
       total2= gelas * 6000
       print(gelas," Gelas Teh Botol = Rp", total2)
       jenis2=("Teh Botol")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      
def tanya2():
    print('')
    print('~~~~~~')
    tanya2 = input(' Apakah anda ingin memesan minuman ..? (y/n):')
    print('~~~~~~')
    if tanya2 == 'y':
        fungsiminuman()
    else:
        print('')

def jumlah():
     totalsemua=0
     totalsemua=total1+total2
     print("\nTotal harus Dibayar: Rp",totalsemua)
     uang=int(input("Uang Tunai Pembeli: Rp."))
     kembalian=int(uang-totalsemua)
     print("Kembalian :",kembalian)
     print("============================================")
     print("========== S T R U K   B E L I =============")
     print("============================================")
     print (" Nama         :",pembeli)
     print (" Beli         :",porsi,jenis1,"-", total1)
     print ("               ",gelas,jenis2,"-", total2)
     print (" Tagihan      : Rp.",totalsemua)
     print (" Uang         : Rp.",uang)
     print (" Kembalian    : Rp.",kembalian)
     print("============================================")
     print("============================================")
     print('')

jawab='y'
while (jawab=='y') :
    fungsimakanan()
    tanya2 ()
    jumlah()
    print('~~~~~~')
    jawab = input('Apakah anda ingin memesan kembali ..? (y/n):')
    print('~~~~~~')

print('~ TERIMAKASIH SUDAH MEMESAN MARTABAK KAMI ~')