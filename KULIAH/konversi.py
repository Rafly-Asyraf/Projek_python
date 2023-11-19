print('1. Desimal > Hexa')
print('2. Desimal > Octal') 
print('3. Desimal > Biner ') 
print('4. Biner > Hexa') 
print('5. Biner > Octal') 
print('6. Biner > Desimal ') 
print('7. Octal > Hexa') 
print('8. Octal > Desimal') 
print('9. Octal > Biner ') 
print('10. Hexa > Desimal') 
print('11. Hexa > Octal') 
print('12. Hexa > Biner\n') 
print('') 
angka = int(input('Masukkan Pilihan = ')) 
if angka == 1: 
    x=int(input('Masukan angka Desimal : ')) 
    print(hex(x).replace('0x','')) 
elif angka == 2: 
    x=int(input('Masukan angka Desimal : ')) 
    print(oct(x).replace('0o','')) 
elif angka == 3: 
    x=int(input('Masukan angka Desimal : ')) 
    print(bin(x).replace('0b','')) 
elif angka == 4: 
    x=int(input('Masukan angka Biner : '),2) 
    print(hex(x).replace('0x','')) 
elif angka == 5: 
    x=int(input('Masukan angka Biner : '),2) 
    print(oct(x).replace('0o','')) 
elif angka == 6: 
    x=int(input('Masukan angka Biner : '),2) 
    print(x) 
elif angka == 7: 
    x=int(input('Masukan angka Octal : '),8) 
    print(hex(x).replace('0x','')) 
elif angka == 8: 
    x=int(input('Masukan angka Octal : '),8) 
    print(x) 
elif angka == 9: 
    x=int(input('Masukan angka Octal : '),8) 
    print(bin(x).replace('0b','')) 
elif angka == 10: 
    x=int(input('Masukan angka Hexa : '),16) 
    print(x) 
elif angka == 11: 
    x=int(input('Masukan angka Hexa : '),16) 
    print(oct(x).replace('0o','')) 
elif angka == 12: 
    x=int(input('Masukan angka Hexa : '),16) 
    print(bin(x).replace('0b',''))
