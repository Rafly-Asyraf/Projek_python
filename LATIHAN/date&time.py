import datetime as dt

print("masukan tangal \nbulan dan tahun lahir anda \n")
tangal = int(input("Tangal \t: "))
bulan = int (input("Bulan \t: " ))
tahun = int(input("Tahun \t: "))
print("")

tangal_lahir = dt.date(tahun,bulan,tangal)
print(f"tangal lahir anda adalah : {tangal_lahir}")

hari_ini= dt.date.today()
print(f"hari ini tangal : {hari_ini}")
umur_hari = hari_ini - tangal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"harinya adalah : {tangal_lahir:%A}")
print(f"umur anda adalah : {umur_tahun} tahun ,{umur_bulan_sisa} bulan")